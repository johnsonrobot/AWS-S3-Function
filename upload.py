import boto3

bucket_name = ['johnson-test-s3', 'johnsonelblog', 'johnsontestendpoint']

file_data = open("test.txt", "rb").read()
class S3():
    def __init__(self):
        self.client = boto3.client('s3')
        self.buckets_str = "Buckets"
        self.buckets_name = "Name"

    def list_buckets(self):
        super().__init__()
        buckets = self.client.list_buckets().get(self.buckets_str)
        for num in range(len(buckets)):
            print(buckets[num][self.buckets_name])

    def list_objects(self):
        super().__init__()
        
# # response = client.list_objects(Bucket = bucket_name[0])['Contents']
# # for i in response:
# #     print(i['Key'])

# response = client.put_object(
#     Bucket=bucket_name[0],
#     Body=file_data,
#     Key="APItest/test.txt"
# )

if __name__ == '__main__':
    S3().list_buckets()
    # print(a)