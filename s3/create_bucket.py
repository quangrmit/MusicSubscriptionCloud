import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region='us-east-1'):
    try:
        if region is None or region == 'us-east-1':
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def main():
    bucket_name = "s3927198-music-images"
    s3 = boto3.client('s3')
    if bucket_name in s3.list_buckets()['Buckets']:
        print("Bucket name already existed")
        return 
    

    if (create_bucket(bucket_name=bucket_name)):
        print("Create bucket " + bucket_name + " successfully")
    else:
        print("Create bucket failed")
    print("End of run")

if __name__ == "__main__":
    main()