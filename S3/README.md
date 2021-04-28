# Simple Storage Service (S3)
## What is S3?
S3 is provided by AWS and is used to store and retrieve any amount of data, at anytime, from around the world. These are in the form of 'buckets' and you can have any number of buckets. One can control the security access of the bucket and its contents. We can also host our static website on S3. 

## Who uses it? 
* Trello stored images on S3
* Netflix, Airbnb
* Social Media platforms (Pintrest)
* Globally available service

## S3 Configurations
* In order to have AWSCLI, we need to install the required dependencies:
  * Python
  * Pip
* Configure AWSCLI with AWS keys to authenticate the access from our machine to S3
* Enter `aws configure`
* You will be prompt to enter your:
  * AWS Access Key ID
  * AWS Secret Access Key
  * Default region name (same as instance, usually Ireland)
  * Default output format: json

## S3 Commands
* Create bucket: `aws s3 mb s3://eng84-william-s3 --region eu-west-1`
* Add things to a bucket: `aws s3 cp README.md s3://eng84-william-s3`
* Download README.md from the remote bucket (adjust permissions first): `aws s3 sync s3://eng84-william-s3 README.md`
* Delete README.md from bucket: `aws s3 rm s3://eng84-william-s3/README.md`
* Delete the bucket: `aws s3 rb s3://eng84-william-s3`
* Delete the bucket AND its contents: `aws s3 rb s3://eng84-william-s3 --force`
