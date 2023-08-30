import boto3

region_name = 'us-east-1'
ecr_client = boto3.client('ecr', region_name=region_name)

repository_name = "monitor-app-repo"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)