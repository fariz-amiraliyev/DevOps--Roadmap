Enabling VPC Flow Logs

 we creat Trust role for VPC flow logs service and policy to this role:
1. to create assume Role for VPC flow logs

  aws iam create-role --role-name=VPC-Flow-logs --asume-role-policy-document file://trust-policy.json

2. Grant this Role permission to access CloudWatch Logs:
   aws iam put-role-policy --role-name VPCFlowLogsRole --policy-name VPCFlowLogsPolicy --policy-document file://vpc-flow-logs-iam-role.json

3. Create the Lambda Function

Name: EnableVPCFlowLogs
Runtime: Python 3.7
Role: Create a custom role (use lambda_execution_role.json)
Code: lambda_function.py


4. Create a CloudWatch Event Rule to Trigger Lambda
   Select Event Pattern.

Service Name: EC2
Event Type: AWS API Call via CloudTrail
Specific operation(s): CreateVpc
Event Pattern:

{
 "source": [
     "aws.ec2"
 ],
 "detail-type": [
     "AWS API Call via CloudTrail"
 ],
 "detail": {
     "eventSource": [
         "ec2.amazonaws.com"
     ],
     "eventName": [
         "CreateVpc"
     ]
 }
}
Click Add target and select the EnableVpcFlowLogs Lambda function.

Click Configure details.


4. Create a New VPC:
   aws ec2 create-vpc --cidr-block 172.20.0.0/16 --region us-east-2
