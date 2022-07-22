import boto3
client = boto3.client('resourcegroupstaggingapi')
client.get_resources()