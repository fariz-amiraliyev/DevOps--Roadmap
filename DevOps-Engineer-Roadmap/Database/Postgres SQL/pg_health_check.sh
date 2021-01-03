#!/bin/bash
# **README**
#1. Copy script on Amazon EC2 Linux instance with AWS CLI configured, and psql client installed with accessibility to RDS/Aurora Postgres instance
#2. Make script executable: chmod +x pg_health_check.sh
#3. Run the script: ./ pg_health_check.sh
#4. It will take around 2-3 mins to run (depending on size of instance), and generate html report:  <Database identifier>_report_<date>.html
#5. Share the report with your AWS Technical Account Manager
#################
# Author: Vivek Singh, Postgres Specialist Technical Account Manager, AWS
# V-13 : 4/10/2020
#################
clear
echo -n -e "RDS/Aurora PostgreSQL Endpoint URL: "
read EP
echo -n -e "Database Name: "
read DBNAME
echo -n -e "Port: "
read RDSPORT
echo -n -e "RDS Master User Name: "
read MASTERUSER
echo -n -e "Password: "
read -s  MYPASS
echo  ""
echo -n -e "Company Name: "
read COMNAME
RDSNAME="${EP%%.*}"

#SQLs Used In the Script:

#Idele Connections
SQL1="select count(*) from pg_stat_activity where state='idle';"

#Size of all databases
SQL2="SELECT pg_database.datname,
pg_database_size(pg_database.datname) as "DB_Size",
pg_size_pretty(pg_database_size(pg_database.datname)) as "Pretty_DB_size"
 FROM pg_database ORDER by 2 DESC limit 5;"

#Size only of all databases
SQL3="SELECT pg_database_size(pg_database.datname)  FROM pg_database"

#Top 10 biggest tables
SQL4="Select schemaname as table_schema,
     relname as table_name,
     pg_size_pretty(pg_total_relation_size(relid)) as "Total_Size",
     pg_size_pretty(pg_relation_size(relid)) as "Data_Size",
     pg_size_pretty(pg_total_relation_size(relid) - pg_relation_size(relid))
       as "Index_Size"
 from pg_catalog.pg_statio_user_tables
 order by pg_total_relation_size(relid) desc,
          pg_relation_size(relid) desc
 limit 10;"

#Duplticate Indexes
SQL5="SELECT pg_size_pretty(SUM(pg_relation_size(idx))::BIGINT) AS SIZE,
       (array_agg(idx))[1] AS idx1, (array_agg(idx))[2] AS idx2,
       (array_agg(idx))[3] AS idx3, (array_agg(idx))[4] AS idx4
FROM (
    SELECT indexrelid::regclass AS idx, (indrelid::text ||E'\n'|| indclass::text ||E'\n'|| indkey::text ||E'\n'||
                                         COALESCE(indexprs::text,'')||E'\n' || COALESCE(indpred::text,'')) AS KEY
    FROM pg_index) sub
GROUP BY KEY HAVING COUNT(*)>1
ORDER BY SUM(pg_relation_size(idx)) DESC;"

#Unused Indexes
SQL6="SELECT s.schemaname,
       s.relname AS tablename,
       s.indexrelname AS indexname,
       pg_size_pretty(pg_relation_size(s.indexrelid)) AS index_size
FROM pg_catalog.pg_stat_user_indexes s
   JOIN pg_catalog.pg_index i ON s.indexrelid = i.indexrelid
WHERE s.idx_scan = 0      -- has never been scanned
  AND 0 <>ALL (i.indkey)  -- no index column is an expression
  AND NOT EXISTS          -- does not enforce a constraint
         (SELECT 1 FROM pg_catalog.pg_constraint c
          WHERE c.conindid = s.indexrelid)
ORDER BY pg_relation_size(s.indexrelid) DESC limit 15;"

#Database Age
SQL7="select datname, ltrim(to_char(age(datfrozenxid), '999,999,999,999,999')) age from pg_database where datname not like 'rdsadmin';"

#Most Bloated Tables
SQL8="SELECT
  current_database(), schemaname, tablename, /*reltuples::bigint, relpages::bigint, otta,*/
  ROUND((CASE WHEN otta=0 THEN 0.0 ELSE sml.relpages::FLOAT/otta END)::NUMERIC,1) AS tbloat,
  CASE WHEN relpages < otta THEN 0 ELSE bs*(sml.relpages-otta)::BIGINT END AS wastedbytes,
  iname, /*ituples::bigint, ipages::bigint, iotta,*/
  ROUND((CASE WHEN iotta=0 OR ipages=0 THEN 0.0 ELSE ipages::FLOAT/iotta END)::NUMERIC,1) AS ibloat,
  CASE WHEN ipages < iotta THEN 0 ELSE bs*(ipages-iotta) END AS wastedibytes
FROM (
  SELECT
    schemaname, tablename, cc.reltuples, cc.relpages, bs,
    CEIL((cc.reltuples*((datahdr+ma-
      (CASE WHEN datahdr%ma=0 THEN ma ELSE datahdr%ma END))+nullhdr2+4))/(bs-20::FLOAT)) AS otta,
    COALESCE(c2.relname,'?') AS iname, COALESCE(c2.reltuples,0) AS ituples, COALESCE(c2.relpages,0) AS ipages,
    COALESCE(CEIL((c2.reltuples*(datahdr-12))/(bs-20::FLOAT)),0) AS iotta -- very rough approximation, assumes all cols
  FROM (
    SELECT
      ma,bs,schemaname,tablename,
      (datawidth+(hdr+ma-(CASE WHEN hdr%ma=0 THEN ma ELSE hdr%ma END)))::NUMERIC AS datahdr,
      (maxfracsum*(nullhdr+ma-(CASE WHEN nullhdr%ma=0 THEN ma ELSE nullhdr%ma END))) AS nullhdr2
    FROM (
      SELECT
        schemaname, tablename, hdr, ma, bs,
        SUM((1-null_frac)*avg_width) AS datawidth,
        MAX(null_frac) AS maxfracsum,
        hdr+(
          SELECT 1+COUNT(*)/8
          FROM pg_stats s2
          WHERE null_frac<>0 AND s2.schemaname = s.schemaname AND s2.tablename = s.tablename
        ) AS nullhdr
      FROM pg_stats s, (
        SELECT
          (SELECT current_setting('block_size')::NUMERIC) AS bs,
          CASE WHEN SUBSTRING(v,12,3) IN ('8.0','8.1','8.2') THEN 27 ELSE 23 END AS hdr,
          CASE WHEN v ~ 'mingw32' THEN 8 ELSE 4 END AS ma
        FROM (SELECT version() AS v) AS foo
      ) AS constants
      GROUP BY 1,2,3,4,5
    ) AS foo
  ) AS rs
  JOIN pg_class cc ON cc.relname = rs.tablename
  JOIN pg_namespace nn ON cc.relnamespace = nn.oid AND nn.nspname = rs.schemaname AND nn.nspname <> 'information_schema'
  LEFT JOIN pg_index i ON indrelid = cc.oid
  LEFT JOIN pg_class c2 ON c2.oid = i.indexrelid
) AS sml
ORDER BY wastedbytes DESC LIMIT 10;"

#Top 10 biggest tables last vacuumed
SQL9="SELECT
schemaname, relname,last_vacuum, cast(last_autovacuum as date), cast(last_analyze as date), cast(last_autoanalyze as date),
pg_size_pretty(pg_total_relation_size(table_name)) as table_total_size
from pg_stat_user_tables a, information_schema.tables b where a.relname=b.table_name ORDER BY pg_total_relation_size(table_name) DESC limit 10;"

#Memory Parameters
SQL10="select name, setting, source, context from pg_settings where name like '%mem%' or name ilike '%buff%'; "

#Performance Parameters
SQL11="select name, setting from pg_settings where name IN ('shared_buffers', 'effective_cache_size', 'work_mem', 'maintenance_work_mem', 'default_statistics_target', 'random_page_cost', 'rds.logical_replication','wal_keep_segments');"

#pg_stat_statements top queries
#Top 10 short queries consuming CPU
SQL12="SELECT substring(query, 1, 50) AS short_query,
              round(total_time::numeric, 2) AS total_time,
              calls,
              round(mean_time::numeric, 2) AS mean,
              round((100 * total_time /
              sum(total_time::numeric) OVER ())::numeric, 2) AS percentage_cpu
FROM    pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;"

#Top 10 short queries causing high Read IOPS
SQL13="SELECT
  left(query, 50) AS short_query
  ,round(total_time::numeric, 2) AS total_time
  ,calls
  ,shared_blks_read
  ,shared_blks_hit
  ,round((100.0 * shared_blks_hit/nullif(shared_blks_hit + shared_blks_read, 0))::numeric,2) AS hit_percent
FROM  pg_stat_statements
ORDER BY total_time DESC LIMIT 10;"

#Top 10 short queries causing high write IOPS
SQL14="SELECT
    left(query, 50) AS short_query
   ,calls
   ,round(total_time::numeric, 2) AS total_time
   ,rows
   ,calls*total_time*rows as Volume
   FROM pg_stat_statements
WHERE
    (query ilike '%update%'
    or query ilike '%insert%'
    or query ilike '%delete%')
    and query not like '%aurora_replica_status%'
    and query not like '%rds_heartbeat%'
ORDER BY Volume DESC LIMIT 10;"

#Top 10 UPDATE/DELETE tables
SQL15="SELECT relname
,round(upd_percent::numeric, 2) AS update_percent
,round(del_percent::numeric, 2) AS delete_percent
,round(ins_percent::numeric, 2) AS insert_percent
 from (
SELECT relname
,100*cast(n_tup_upd AS numeric) / (n_tup_ins + n_tup_upd + n_tup_del) AS upd_percent
,100*cast(n_tup_del AS numeric) / (n_tup_ins+ n_tup_upd + n_tup_del) AS del_percent
,100*cast(n_tup_ins AS numeric) / (n_tup_ins + n_tup_upd + n_tup_del) AS ins_percent
FROM pg_stat_user_tables
WHERE (n_tup_ins + n_tup_upd + n_tup_del) > 0
ORDER BY coalesce(n_tup_upd,0)+coalesce(n_tup_del,0) desc ) a limit 10;"

#Top 10 Read IO tables
SQL16="SELECT
relname
,round((100.0 * heap_blks_hit/nullif(heap_blks_hit + heap_blks_read, 0))::numeric,2) AS hit_percent
,heap_blks_hit
,heap_blks_read
FROM pg_statio_user_tables
WHERE (heap_blks_hit + heap_blks_read) >0
ORDER BY coalesce(heap_blks_hit,0)+coalesce(heap_blks_read,0) desc limit 10;"

html=${RDSNAME}_report_$(date +"%m-%d-%y").html
#Generating HTML file
echo "<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">" > $html
echo "<html>" >> $html
echo "<link rel="stylesheet" href="https://unpkg.com/purecss@0.6.2/build/pure-min.css">" >> $html
echo "<body style="font-family:'Verdana'" bgcolor="#F8F8F8">" >> $html
echo "<fieldset>" >> $html
echo "<table><tr> <td width="20"></td> <td>" >>$html
echo "<h1><font face="verdana" color="#0099cc"><center><u>PostgreSQL Health Report For $COMNAME</u></center></font></h1>" >> $html
echo "<h3><font face="verdana">Vivek Singh, PostgreSQL Specialist, AWS Enterprise Support - `date +%m-%d-%Y`</h3></color>" >> $html
echo "</fieldset>" >> $html

echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Instance Details:  </font>" >>$html
echo "<br>" >> $html
echo "Postgres Endpoint URL: $EP" >> $html
echo "<br>" >> $html


PSQLCL="psql -h $EP  -p $RDSPORT -U $MASTERUSER $DBNAME"
if [ "$?" -gt "0" ]; then
INSTSTAT=("Not Running")
exit
else

echo "Instance is running. Creating Report..."
fi
echo "Postgres Engine Version: " >>$html
echo `PGPASSWORD=$MYPASS $PSQLCL -c "SELECT version()" | awk 'FNR== 3'  `  >>$html
echo "<br>" >> $html
echo "Maximum Connections :" >>$html
echo  `PGPASSWORD=$MYPASS $PSQLCL -c "show max_connections" | awk 'FNR== 3'`  >>$html
echo "<br>" >> $html
echo "Curent Active Connections: " >>$html
echo `PGPASSWORD=$MYPASS $PSQLCL -c "select count(*) from pg_stat_activity;" | awk 'FNR== 3'`  >>$html
echo "<br>" >> $html
echo "Idle Connections : `PGPASSWORD=$MYPASS $PSQLCL -c "$SQL1" | awk 'FNR== 3'` " >>$html
echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Instance Configuration: </font>" >>$html
aws rds describe-db-instances --db-instance-identifier $RDSNAME | grep 'Allocated\|Public\|MonitoringInterval\|MultiAZ\|\StorageType\|\BackupRetentionPeriod\|DBInstanceClass'|sed "s/\"//g"|sed "s/\,//g"| sed "s/\PubliclyAccessible/<br>Publicly Accessible/g"| sed "s/\MonitoringInterval/<br>EM Monitoring Interval/g" | sed "s/\MultiAZ/<br>Multi AZ Enabled?/g" | sed "s/\AllocatedStorage/<br>Allocated Storage (GB)/g" |  sed "s/\DBInstanceClass/<br>DB Instance Class/g" | sed "s/\BackupRetentionPeriod/<br>Backup Retention Period/g" | sed "s/\StorageType/<br>Storage Type/g" |  sed "s/\ B//g"|sed "s/\gp2/GP2/g" >>$html
echo "<br>" >> $html
echo "<br>" >> $html
#Total Log Size
TLS=`aws rds describe-db-log-files --db-instance-identifier $RDSNAME | grep "Size" | grep -o '[0-9]*' | awk '{n += $1}; END{print n}'`
AGB=1073741824
echo "<font face="verdana" color="#ff6600">Total Size of Log Files:  </font>" >>$html
echo $TLS | sed 's/$/ Bytes/' >>$html
#echo "<br>" >> $html
echo : $((ERT / AGB)) | sed 's/$/ GB/' >>$html
echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Total Size of ALL Databases:  </font>" >>$html
PGPASSWORD=$MYPASS $PSQLCL -c "$SQL3" |  sed '$d' | sed '$d'| tail -n +3 > ret.txt
ADB=`awk '{ sum += $1 } END { print sum }' ret.txt`
rm ret.txt
echo $ADB  | sed 's/$/ Bytes/' >>$html
#echo "<br>" >> $html
echo : $((ADB / AGB)) | sed 's/$/ GB/' >>$html

echo "<br>" >> $html
echo "<br>" >> $html
DBAGE=`PGPASSWORD=$MYPASS $PSQLCL -c "SELECT to_char(max(age(datfrozenxid)),'FM9,999,999,999') FROM pg_database;" | awk 'FNR== 3'|sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'`
echo "<font face="verdana" color="#ff6600">Maximum Used Transaction IDs:</font> $DBAGE" >>$html

echo "<br>" >> $html
echo "<br>" >> $html
TOTALDB=`PGPASSWORD=$MYPASS $PSQLCL -c "SELECT count(*) from pg_database" | awk 'FNR== 3'|sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'`
echo "<font face="verdana" color="#ff6600">Top 5 Databases Size ($TOTALDB):</font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL2
"|sed '$d'|sed '$d' ` " >>$html

echo "<br>" >> $html
echo "<br>" >> $html
TOTALTABLE=`PGPASSWORD=$MYPASS $PSQLCL -c "select count(*) from  pg_stat_user_tables" | awk 'FNR== 3'|sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'`
echo "<font face="verdana" color="#ff6600">Top 10 Biggest Tables ($TOTALTABLE): </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
 $SQL4
"|sed '$d'|sed '$d' ` " >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Duplicate Indexes: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL5
"|sed '$d'|sed '$d' ` " >>$html


echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Unused Indexes: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL6
"|sed '$d'|sed '$d' ` " >>$html


echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Database Age: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL7
"|sed '$d'|sed '$d' ` " >>$html


echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 Most Bloated Tables: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL8
"|sed '$d'|sed '$d' ` " >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 Biggest Tables Last Vacuumed: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL9
"|sed '$d'|sed '$d'` "   >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 UPDATE/DELETE Tables: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL15
"|sed '$d'|sed '$d'` "   >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 Read IO Tables: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL16
"|sed '$d'|sed '$d'` "   >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Vacuum Parameters: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
select name, setting, source, context from pg_settings where name like 'autovacuum%'
"|sed '$d'|sed '$d'` "   >>$html


echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Memory Parameters: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL10
"|sed '$d'|sed '$d' ` "   >>$html
echo "<br>" >> $html
echo "<br>" >> $html

echo "<font face="verdana" color="#ff6600">Performance Parameters: </font>" >>$html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL11
"|sed '$d'|sed '$d' ` "   >>$html

if
PGPASSWORD=$MYPASS $PSQLCL -c "select * FROM pg_extension" | cut -d \| -f 1 | grep -qw pg_stat_statements; then
echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 CPU Consuming SQLs: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL12
"|sed '$d'|sed '$d'` "   >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 Read Queries: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL13
"|sed '$d'|sed '$d'` "   >>$html

echo "<br>" >> $html
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Top 10 Write Queries: </font>" >>$html
echo "<br>" >> $html
echo "`PGPASSWORD=$MYPASS $PSQLCL --html -c "
$SQL14
"|sed '$d'|sed '$d'` "   >>$html

else
echo "<br>" >> $html
echo "<font face="verdana" color="#ff6600">Postgres extension pg_stat_statements is not installed. Installation of this extension is recommended. </font>" >>$html
fi



echo "<br>" >> $html
echo "<br>" >> $html
echo "<br>" >> $html

echo "</td></tr></table></body></html>" >> $html

sleep 1
echo "Report `pwd`/$html created!"
