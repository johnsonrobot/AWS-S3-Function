import boto3

bucket_name = ['johnson-test-s3', 'johnsonelblog', 'johnsontestendpoint']
file_name = "test.txt"
Path = "APItest/"

# file_data = open("test.txt", "rb").read()
class S3():
    def __init__(self):
        self.client = boto3.client('s3')
        self.buckets_str = "Buckets"
        self.buckets_name = "Name"
        self.object_content = "Contents"
        self.object_key = "Key"

    def list_buckets(self):
        buckets = self.client.list_buckets().get(self.buckets_str)
        for num in range(len(buckets)):
            print(buckets[num][self.buckets_name])

    def list_objects(self, bucket_name):
        objects = self.client.list_objects(Bucket = bucket_name)[self.object_content]
        for object in objects:
            print(object[self.object_key])

    def put_object(self, bucket_name, file_data, key):
        self.client.put_object(
            Bucket = bucket_name,
            Body = file_data,
            Key = key
        )
        print("Bucket: {}\n Content: {}\n Path: {}" .format(bucket_name, file_data, key))

# response = client.put_object(
#     Bucket=bucket_name[0],
#     Body=file_data,
#     Key="APItest/test.txt"
# )

if __name__ == '__main__':
    with open(file_name, "r") as f:
        data = f.read()
    S3().put_object(bucket_name[0], data, Path + file_name)
    # S3().list_buckets()
    # S3().list_objects(bucket_name[0])
    # print(a)