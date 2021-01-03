import boto3
from data_source.aws_credentials import *

def gen_credential():
    credential = boto3.session.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)
    return credential


def get_regions(service):
    credential = gen_credential()
    return credential.get_available_regions(service)


def list_ec2_servers(region):
    credential = gen_credential()
    ec2 = credential.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    for reservations in instances['Reservations']:
        for instance in reservations['Instances']:
            tags = parse_keyvalue_sets(instance['Tags'])
            state = instance['State']['Name']
            print(f"{region}\t{instance['InstanceId']}\t{tags['Name']}\t{state}")


def parse_keyvalue_sets(tags):
    result = {}
    for tag in tags:
        key = tag['Key']
        val = tag['Value']
        result[key] = val
    return result


if __name__ == "__main__":

    regions = get_regions('ec2')
    for region in regions:
        list_ec2_servers(region)
