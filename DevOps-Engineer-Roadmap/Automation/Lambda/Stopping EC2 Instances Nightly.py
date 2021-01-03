Task: Stop m4.large instances nightly to save 2000$ monthly

1. Create lambda function
2. Choose run time as a python for using Boto
3. Create IAM role for Lambda to get access ec2 and do make operations ?
4. write lambda function with boto ?


    import boto3
    def lambda_handler (event,context):

        ec2_client=boto3.client('ec2')
        regions=[region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

        for region in regions :

           ec2=boto3.resource('ec2', region_name=region)

           print("Region: ", region)


        # get only running instances

        instances=ec2.instances.filter(
          Filter=[{'Name': 'instance_state_name' , 'Value' : ['running']}])

        #Stop the instances

        for instance in instances:
           instance.stop()

           print('Stoped instances:', instance_id )


5. Setting up timeout for running function.
6. Create CloudWatch rule: shcedul rule running time with cron.
7. Add Lambda function as a Target to this CloudWatch rule.
8. How to see Lambda function execution: When Lambda is running it creates CloudWatch log groups for each function.
