Using AWS Config to Monitor for and Respond to Amazon S3 Buckets Allowing Public Access:

AWS Config enables continuous monitoring of your AWS resources, making it simple to assess, audit, and record resource configurations and changes.
AWS Config does this through the use of rules that define the desired configuration state of your AWS resources.
AWS Config provides a number of AWS managed rules that address a wide range of security concerns such as checking if you encrypted your
Amazon Elastic Block Store (Amazon EBS) volumes, tagged your resources appropriately, and enabled multi-factor authentication (MFA) for root accounts.
You can also create custom rules to codify your compliance requirements through the use of AWS Lambda functions.


 How to use AWS Config to monitor our Amazon Simple Storage Service (S3) bucket ACLs and
   policies for violations which allow public read or public write access ?
1. Enable AWS Config to monitor Amazon S3 bucket ACLs and policies for compliance violations.
2. Create an IAM Role and Policy that grants a Lambda function permissions to read S3 bucket policies and send alerts through SNS.
3. Create and configure a CloudWatch Events rule that triggers the Lambda function when AWS Config detects an S3 bucket ACL or policy violation.
4. Create a Lambda function that uses the IAM role to review S3 bucket ACLs and policies, correct the ACLs, and notify your team of out-of-compliance policies.
5. Verify the monitoring solution.


Create and Configure a CloudWatch Rule:
In the AWS Management Console, under Services, select CloudWatch.
On the left-hand side, under Events, select Rules.
Click Create rule.
In Step 1: Create rule, under Event Source, select the dropdown list and select Build custom event pattern.
Copy the following pattern and paste it into the text box:

{
  "source": [
    "aws.config"
  ],
  "detail": {
    "requestParameters": {
      "evaluations": {
        "complianceType": [
          "NON_COMPLIANT"
        ]
      }
    },
    "additionalEventData": {
      "managedRuleIdentifier": [
        "S3_BUCKET_PUBLIC_READ_PROHIBITED",
        "S3_BUCKET_PUBLIC_WRITE_PROHIBITED"
      ]
    }


    Create a Lambda Function:

    import boto3
from botocore.exceptions import ClientError
import json
import os

ACL_RD_WARNING = "The S3 bucket ACL allows public read access."
PLCY_RD_WARNING = "The S3 bucket policy allows public read access."
ACL_WRT_WARNING = "The S3 bucket ACL allows public write access."
PLCY_WRT_WARNING = "The S3 bucket policy allows public write access."
RD_COMBO_WARNING = ACL_RD_WARNING + PLCY_RD_WARNING
WRT_COMBO_WARNING = ACL_WRT_WARNING + PLCY_WRT_WARNING

def policyNotifier(bucketName, s3client):
    try:
        bucketPolicy = s3client.get_bucket_policy(Bucket = bucketName)
        # notify that the bucket policy may need to be reviewed due to security concerns
        sns = boto3.client('sns')
        subject = "Potential compliance violation in " + bucketName + " bucket policy"
        message = "Potential bucket policy compliance violation. Please review: " + json.dumps(bucketPolicy['Policy'])
        # send SNS message with warning and bucket policy
        response = sns.publish(
            TopicArn = os.environ['TOPIC_ARN'],
            Subject = subject,
            Message = message
        )
    except ClientError as e:
        # error caught due to no bucket policy
        print("No bucket policy found; no alert sent.")

def lambda_handler(event, context):
    # instantiate Amazon S3 client
    s3 = boto3.client('s3')
    resource = list(event['detail']['requestParameters']['evaluations'])[0]
    bucketName = resource['complianceResourceId']
    complianceFailure = event['detail']['requestParameters']['evaluations'][0]['annotation']
    if(complianceFailure == ACL_RD_WARNING or complianceFailure == ACL_WRT_WARNING):
        s3.put_bucket_acl(Bucket = bucketName, ACL = 'private')
    elif(complianceFailure == PLCY_RD_WARNING or complianceFailure == PLCY_WRT_WARNING):
        policyNotifier(bucketName, s3)
    elif(complianceFailure == RD_COMBO_WARNING or complianceFailure == WRT_COMBO_WARNING):
        s3.put_bucket_acl(Bucket = bucketName, ACL = 'private')
        policyNotifier(bucketName, s3)
    return 0  # done
