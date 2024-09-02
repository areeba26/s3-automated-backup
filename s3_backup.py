import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3, bucket_name, region):
    s3.create_bucket(Bucket= bucket_name,CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    })
    
    print("Bucket created successfully")


def upload_backup(s3, file_name, bucket_name, key_name):
    
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("backup uploaded successfully")
bucket_name ="first-python-bucket"
region= "us-east-2"
key_name= "my-backup.tar.gz"
#show_buckets(s3, bucket_name, region)
#create_bucket(s3)
file_name = "D:\Python For DevOps/backups/backup_2024-09-02.tar.gz"
upload_backup(s3,file_name,bucket_name,key_name)