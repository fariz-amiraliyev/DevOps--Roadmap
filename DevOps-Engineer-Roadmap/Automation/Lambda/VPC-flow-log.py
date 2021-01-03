Enabling AWS VPC Flow Logs with Automation

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

test-event.json is a sample CloudTrail event that can be used with the
              Lambda function, as it contains the VPC ID


https://github.com/linuxacademy/la-aws-security_specialty/tree/master/Enabling-VPC-Flow-Logs-with-Automation
lambda_function.py creates VPC Flow Logs for the VPC ID in the event

import boto3
import os


def lambda_handler(event, context):
    '''
    Extract the VPC ID from the event and enable VPC Flow Logs.
    '''

    try:
        vpc_id = event['detail']['responseElements']['vpc']['vpcId']

        print('VPC: ' + vpc_id)

        ec2_client = boto3.client('ec2')

        response = ec2_client.describe_flow_logs(
            Filter=[
                {
                    'Name': 'resource-id',
                    'Values': [
                        vpc_id,
                    ]
                },
            ],
        )

        if len(response[u'FlowLogs']) != 0:
            print('VPC Flow Logs are ENABLED')
        else:
            print('VPC Flow Logs are DISABLED')

            print('FLOWLOGS_GROUP_NAME: ' + os.environ['FLOWLOGS_GROUP_NAME'])
            print('ROLE_ARN: ' + os.environ['ROLE_ARN'])

            response = ec2_client.create_flow_logs(
                ResourceIds=[vpc_id],
                ResourceType='VPC',
                TrafficType='ALL',
                LogGroupName=os.environ['FLOWLOGS_GROUP_NAME'],
                DeliverLogsPermissionArn=os.environ['ROLE_ARN'],
            )

            print('Created Flow Logs: ' + response['FlowLogIds'][0])

    except Exception as e:
        print('Error - reason "%s"' % str(e))
