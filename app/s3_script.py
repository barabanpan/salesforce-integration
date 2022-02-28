from io import StringIO

from boto3.session import Session
from botocore.exceptions import ClientError

from config import Config


session = Session(aws_access_key_id=Config.aws_access_key_id,
                  aws_secret_access_key=Config.aws_secret_access_key,
                  region_name=Config.aws_region)
s3 = session.resource('s3')
BUCKET_NAME = Config.aws_s3_bucket_name


def save_to_s3(df):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    try:
        s3.Object(BUCKET_NAME, "contacts.csv").put(Body=csv_buffer.getvalue())
    except ClientError as e:
        print("ClientError:", e)
        return False
    return True

