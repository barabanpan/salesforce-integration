import sys

from app.salesforce_script import download_as_csv, create_users


if __name__ == "__main__":
    # create_users()

    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    to_s3 = True if arg.lower() == "to_s3" else False
    download_as_csv(to_s3)

