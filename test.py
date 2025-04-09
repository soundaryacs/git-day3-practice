import linux
import boto3

def lambda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instances(
    ImageId='ami-0614680123427b75e',
    InstanceType='t2.medium',
    KeyName='cust-key',
    MaxCount=10,
    MinCount=1
)
