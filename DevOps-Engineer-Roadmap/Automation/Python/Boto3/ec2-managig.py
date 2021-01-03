import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

#Monitor and unmonitor instances
import sys
import boto3

ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)


#Start and stop instances

import sys
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')


if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)


#Reboot instances

import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)

    
