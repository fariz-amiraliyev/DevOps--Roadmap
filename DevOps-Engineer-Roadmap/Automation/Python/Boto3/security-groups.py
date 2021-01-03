
#Describe security groups

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
    print(response)
except ClientError as e:
    print(e)


# Create a security group and rules

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
    response = ec2.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                         Description='DESCRIPTION',
                                         VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)



# Delete a security group
import boto3
from botocore.exceptions import ClientError

# Create EC2 client
ec2 = boto3.client('ec2')

# Delete security group
try:
    response = ec2.delete_security_group(GroupId='SECURITY_GROUP_ID')
    print('Security Group Deleted')
except ClientError as e:
    print(e)
