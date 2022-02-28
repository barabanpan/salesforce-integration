import os
from dotenv import load_dotenv

project_root = os.getcwd()
load_dotenv(os.path.join(project_root, '.env'))


class Config(object):
    username = os.getenv("SALESFORCE_USERNAME")
    password = os.getenv("SALESFORCE_PASSWORD")
    security_token = os.getenv("SALESFORCE_SECURITY_TOKEN")

