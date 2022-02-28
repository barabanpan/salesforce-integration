# Salesforse integration

# Used urls
1. https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart.htm
2. https://www.sfdcstop.com/2019/01/how-to-connect-to-salesforce-with.html

# Technology used
 - Python 3.9 
 - simple-salesforce library for salesforce
 - boto3 library for aws s3

# How to run it
1. Create .env file by the .env.example example
2. ```pip install -r requirements.txt```
3. From root:
```python run.py to_s3``` to save contacts.csv to s3 OR<br>
```python run.py``` to save contacts.csv locally

