Create DynamoDB Table

aws dynamodb create-table --table-name Message  --attribute-definitions AttributeName=MessageId,AttributeType=S --key-schema AttributeName=MessageId,KeyType=HASH  --billing-mode=PAY_PER_REQUEST

aws sqs create-queue --queue-name Messages

import json
import os
from datetime import datetime

import boto3

QUEUE_NAME = os.environ['QUEUE_NAME']
MAX_QUEUE_MESSAGES = os.environ['MAX_QUEUE_MESSAGES']
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']

sqs = boto3.resource('sqs')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):

    # Receive messages from SQS queue
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

    print("ApproximateNumberOfMessages:",
          queue.attributes.get('ApproximateNumberOfMessages'))

    for message in queue.receive_messages(
            MaxNumberOfMessages=int(MAX_QUEUE_MESSAGES)):

        print(message)

        # Write message to DynamoDB
        table = dynamodb.Table(DYNAMODB_TABLE)

        response = table.put_item(
            Item={
                'MessageId': message.message_id,
                'Body': message.body,
                'Timestamp': datetime.now().isoformat()
            }
        )
        print("Wrote message to DynamoDB:", json.dumps(response))

        # Delete SQS message
        message.delete()
        print("Deleted message:", message.message_id)

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
        "dynamodb:PutItem"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Message"
    },
    {
      "Action": [
        "sqs:Describe*",
        "sqs:Get*",
        "sqs:List*",
        "sqs:DeleteMessage",
        "sqs:ReceiveMessage"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:sqs:us-east-1:123456789012:Messages"
    }
  ]
}


#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import argparse
import logging
import sys
from time import sleep

import boto3
from faker import Faker

parser = argparse.ArgumentParser()
parser.add_argument("--queue-name", "-q", required=True,
                    help="SQS queue name")
parser.add_argument("--interval", "-i", required=True,
                    help="timer interval", type=float)
parser.add_argument("--message", "-m", help="message to send")
parser.add_argument("--log", "-l", default="INFO",
                    help="logging level")
args = parser.parse_args()

if args.log:
    logging.basicConfig(
        format='[%(levelname)s] %(message)s', level=args.log)

else:
    parser.print_help(sys.stderr)

sqs = boto3.client('sqs')

response = sqs.get_queue_url(QueueName=args.queue_name)

queue_url = response['QueueUrl']

logging.info(queue_url)

while True:
    message = args.message
    if not args.message:
        fake = Faker()
        message = fake.text()

    logging.info('Sending message: ' + message)

    response = sqs.send_message(
        QueueUrl=queue_url, MessageBody=message)

    logging.info('MessageId: ' + response['MessageId'])
    sleep(args.interval)
