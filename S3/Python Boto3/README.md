# S3 using Python Boto3
## Install Boto3
1. Follow the configuration steps in the S3 `README.md`
2. Execute `pip install boto3`

## Tasks
### Initial connection
First, import Boto3 and create an S3 resource.
```python
import boto3

s3 = boto3.resource('s3')
```

### Creating a bucket
To create a bucket, state the name of the bucket explicitly and create a dictionary to hold the region. In this case, we are using Ireland.
```python
location = {"LocationConstraint": "eu-west-1"}
s3.create_bucket(Bucket="eng84-william-bucket", CreateBucketConfiguration=location)
```

### Uploading files
To upload a file, you must state the file directory of the file to upload, the bucket and the file name. Keep the first parameter as the file name if the file is in the current directory.
```python
s3.meta.client.upload_file("files/WSM-2010-2020.txt", "eng84-william-bucket", "WSM-2010-2020.txt")
```

### Downloading files
To download a file, state the bucket, file name and file directory to save the file in. Keep the directory as the file name if you want to save it in the current directory. If the file already exists in your local machine, it will be overwritten.
```python
s3.meta.client.download_file("eng84-william-bucket", "WSM-2010-2020.txt", "files/WSM-2010-2020.txt")
```

### Deleting files
To delete a file from a bucket, state the bucket and use the file name as the key.
```python
s3.meta.client.delete_object(Bucket="eng84-william-bucket", Key="WSM-2010-2020.txt")
```

### Deleting a bucket
The following command will delete the specified bucket. The bucket must be empty before executing this command.
```python
s3.meta.client.delete_bucket(Bucket="eng84-william-bucket")
```

## Notes
* The script (`s3_python_boto3.py`) can be run on both your local machine and an EC2 instance
* Use `python s3_python_boto3.py` to execute the script (on the terminal)
* All changes made will be applied locally and remotely
* `WSM-2010-2020.txt` holds the World's Strongest Man winners between 2010 and 2020 