
import boto3
import os

def upload_images_to_s3(bucket_name, local_folder):
    """
    Upload images from a local folder to an S3 bucket.

    Parameters:
    bucket_name (str): Name of the S3 bucket.
    local_folder (str): Path to the folder containing images.

    Returns:
    None
    """
    s3 = boto3.client('s3')
    for file_name in os.listdir(local_folder):
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            s3.upload_file(os.path.join(local_folder, file_name), bucket_name, file_name)
            print(f"Uploaded {file_name} to S3 bucket {bucket_name}")

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in the specified region.

    Parameters:
    bucket_name (str): Name of the S3 bucket to create.
    region (str): AWS region to create the bucket in.

    Returns:
    None
    """
    s3 = boto3.client('s3')
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket {bucket_name} created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def list_s3_buckets():
    """
    List all S3 buckets in the AWS account.

    Returns:
    None
    """
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("Existing buckets:")
    for bucket in response.get('Buckets', []):
        print(f"  {bucket['Name']}")
