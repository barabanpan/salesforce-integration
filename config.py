import os
from dotenv import load_dotenv

project_root = os.getcwd()
load_dotenv(os.path.join(project_root, '.env'))


class Config(object):
    # for salesforce
    username = os.getenv("SALESFORCE_USERNAME")
    password = os.getenv("SALESFORCE_PASSWORD")
    security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")

    # for aws
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_REGION")
    aws_s3_bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

