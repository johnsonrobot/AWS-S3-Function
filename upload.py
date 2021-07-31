import boto3

bucket_name = ['johnson-test-s3', 'johnsonelblog', 'johnsontestendpoint']

file_data = open("test.txt", "rb").read()

client = boto3.client('s3')
# # for i in range(len(client.list_buckets().get('Buckets'))):
# #     print(client.list_buckets().get('Buckets')[i])

# # response = client.list_objects(Bucket = bucket_name[0])['Contents']
# # for i in response:
# #     print(i['Key'])

response = client.put_object(
    Bucket=bucket_name[0],
    Body=file_data,
    Key="APItest/test.txt"
)