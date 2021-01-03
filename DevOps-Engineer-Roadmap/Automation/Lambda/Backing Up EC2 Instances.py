1. Create function for creating Snapshots:
   Name:
   RUntime: python3.7
   Create IAM role for accessing ec2 and EBSs
2. Write function:

    from datetime import datetime
    import boto3

    def lambda_handler(event, context):

        ec2_clinet=boto3.client('ec2')

        regions=[region['RegionName'] for region in ec2_clinet.describe_regions()['Regions']]

        for region in regions:

           print('Instances in region: {0}', format(regions))

           ec2=boto3.resource('ec2', region_name=region)

           instances = ec2.instances_filter(Filters=['Name': 'tag:backup', 'Values':['True']])

           timestamp= datetime.utcnow().replace(microsecond=0,).isoformat()


           for i in instances.all():
              for v in i.volumes.all():
                 desc='Backup of {0}, volume {1}, created {2}'.format(i.id, v.id, timestamp)
                 print(desc)

                 snapshot = v.create_snapshot(Description=desc)

                 print('Created snapshot', snapshot.id)


  3. Create cloudwatch rule and add Lambda functions as a Traget.



  We can create another function to prune  snapshots in a same way, may to save last 3 snapshots.


  from datetime import datetime
  import boto3

  def lambda_handler(event, context):
      account_id = boto3.client('sts').get_caller_identity().get('Account')
      ec2_clinet = boto3.client('ec2')

      regions=[region['RegionName'] for region in ec2_clinet.describe_regions()['Regions']]

      for region in regions:
          print("Region:", region)
          ec2=boto.client('ec2', region_name=region)
          response=ec2.describe_snapshots(Owners_ids=[account_id])


          snapshots =response['Snapshots']

          snapshots.sort(key=lambda x: x x['StartTime'])

          snapshots=snapshot[:-3]

          for snapshot in snapshots:
             id = snapshot['Snapshot_id']
             try:
               print("Deleting :" id)
               ec2.delete_snapshot(Snapshot_id=id)

            except Exception as e:
               if 'InvalidSnapshot.InUse' in e.message:
                   print('Snapshot {} in use, skipping'.format(id)
                   continue 
