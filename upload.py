import boto3
from os import listdir

bucket_name = ['johnson-test-s3', 'johnsonelblog', 'johnsontestendpoint']
# file_name = "test.txt"
Path = "APItest/"
file_path = "file/"
data = []
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

    def put_object(self, bucket_name, file_data, key_path, key_file):
        if len(key_file) > 1:
            for i in range(len(key_file)):
                self.client.put_object(
                    Bucket = bucket_name,
                    Body = file_data[i],
                    Key = key_path + key_file[i]
                )
                print("No.i\nBucket: {}\n Content: {}\n Path: {}" .format(i, bucket_name, file_data[i], key_path + key_file[i]))

# response = client.put_object(
#     Bucket=bucket_name[0],
#     Body=file_data,
#     Key="APItest/test.txt"
# )
def files(fpath):
    return listdir(fpath)

def read_files(f, path):
    if len(f) > 1:
        fd = []
        for num in range(len(f)):
            with open(path + f[num], "r") as ff:
                fd.append(ff.read())
        return fd
    else:
        with open(path + f[-1], "r") as ff:
            return ff.read()

if __name__ == '__main__':
    # with open(file_name, "r") as f:
    #     data = f.read()
    file = files(file_path)
    body = read_files(file, file_path)
    # print(data)
    # print(file)
    S3().put_object(bucket_name[0], body, Path, file)
    # S3().list_buckets()
    # S3().list_objects(bucket_name[0])
    # print(a)