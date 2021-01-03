import boto3

def lambda_handler (event,context):
    ec2_client=boto3.client('ec2')
    regions=[region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions :
        ec2=boto3.resource('ec2', region_name=region)

        print("Region: ", region)
       # get only running instance
       instances=ec2.instances.filter(Filter=[{'Name': 'instance_state_name' , 'Value' : ['running']}])
    for instance in instances:
        instance.stop()

        print('Stoped instances:', instance_id )
