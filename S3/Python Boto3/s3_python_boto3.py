import boto3

# Using AWS S3
s3 = boto3.resource('s3')
bucket_name = "eng84-william-bucket"
region = "eu-west-1"

# Create S3 bucket
def create_bucket():
    location = {"LocationConstraint": region}
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

# Upload file to bucket
def upload_file(filename):
    # First param is the file location of the filename
    s3.meta.client.upload_file(filename, bucket_name, filename)

# Fetch file from S3
def download_file(filename):
    # Third param is the file location to save the file
    s3.meta.client.download_file(bucket_name, filename, filename)

# Delete content from the bucket
def delete_file(filename):
    s3.meta.client.delete_object(Bucket=bucket_name, Key=filename)

# Delete the bucket
def delete_bucket():
    s3.meta.client.delete_bucket(Bucket=bucket_name)

# Shows the names of all the buckets
def list_buckets():
    for bucket in s3.buckets.all():
        print(bucket.name)


# Run main program
if __name__ == "__main__":
    # create_bucket()
    # upload_file("WSM-2010-2020.txt")
    # download_file("WSM-2010-2020.txt")
    # delete_file("WSM-2010-2020.txt")
    # delete_bucket()
    list_buckets()
