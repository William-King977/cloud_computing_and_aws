# Simple Storage Service (S3)
## What is S3?
S3 is provided by AWS and is used to store and retrieve any amount of data, at anytime, from around the world. These are in the form of 'buckets' and you can have any number of buckets. One can control the security access of the bucket and its contents. We can also host our static website on S3. 

## Who uses it? 
* Trello stored images on S3
* Netflix, Airbnb
* Social Media platforms (Pintrest)
* Globally available service

## S3 Configurations
* In order to have AWSCLI, we need to install the required dependencies (inside an EC2 instance):
  * Update Ubuntu with `sudo apt-get update -y`, then `sudo apt-get upgrade -y`
  * Python (`sudo apt-get install python`)
  * Pip (`sudo apt-get install pip`)
  * AWSCLI (`sudo apt-get install awscli`)
* Configure AWSCLI with AWS keys to authenticate the access from our machine to S3
  * Enter `aws configure`
  * You will be prompt to enter your:
    * AWS Access Key ID
    * AWS Secret Access Key
    * Default region name (same as instance, usually Ireland)
    * Default output format: json

## S3 Commands
* `aws s3 ls` - lists all the buckets
* `aws s3 mb s3://eng84-william-s3 --region eu-west-1` - creates a bucket called `eng84-william-s3`. Region isn't necessary.
* `aws s3 cp README.md s3://eng84-william-s3` - adds a `README.md` file to the bucket
* `aws s3 sync s3://eng84-william-s3 README.md` - downloads the `README.md` file from the remote bucket (adjust permissions first)
* `aws s3 rm s3://eng84-william-s3/README.md` - deletes `README.md` from the bucket
* `aws s3 rb s3://eng84-william-s3` - deletes the bucket
* `aws s3 rb s3://eng84-william-s3 --force` - deletes the bucket AND its contents
