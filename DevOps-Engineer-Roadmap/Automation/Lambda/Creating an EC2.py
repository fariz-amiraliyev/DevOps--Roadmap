Navigate to Lambda.
Click Create a function.
Choose Author from scratch and use the following settings:
Name: CreateEC2
Runtime: Python 3.7
Role: Create a custom role
Expand Choose or create an execution role.
Set Execution role to Create a new role with basic Lambda permissions.
Copy the execution role name that appears.
Click Create function.
Navigate to IAM.
Search for and select your newly created role.
Edit the policy to replace its existing policy with this file on GitHub.

{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Action": [
        "ec2:RunInstances"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
Back in the Lambda console, scroll to the Function code section and paste in the Python source code from this file on GitHub.
Set four environment variables:
AMI: The ami- value of an Amazon Linux 2 instance
INSTANCE_TYPE: t2.micro
KEY_NAME: The name of your EC2 key pair
SUBNET_ID: The ID of one of the public subnets in your VPC
Save the Lambda function.


import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)
