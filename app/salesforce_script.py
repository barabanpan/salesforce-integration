from simple_salesforce import Salesforce
import pandas as pd

from app.s3_script import save_to_s3
from config import Config


sf = Salesforce(username=Config.username,
                password=Config.password,
                security_token=Config.security_token)


def create_users():
    r1 = sf.Contact.create({
        "LastName": "First", 
        "Email": "info@repsly.com",
        "MailingCity": "Boston",
        "MailingCountry": "USA",
        "MailingState": "MA",
        "MailingStreet": "55 Summer Street, 3rd Floor",
        "MobilePhone": "1-617-356-8125"})
    r2 = sf.Contact.create({
        "LastName": "Second",
        "Email": "info@repsly.com",
        "MailingCity": "Zagreb",
        "MailingCountry": "Croatia",
        "MailingStreet": "Petračićeva 4",
        "MobilePhone": "1-617-356-8125"})
    print(r1)
    print(r2)


def download_as_csv(to_s3=False):
    query = """SELECT Id, LastName, Email, MobilePhone, MailingCity, MailingState, MailingCountry, MailingStreet
               FROM Contact WHERE LastName IN ('First', 'Second')"""
    res = sf.query(query).get("records", [{}])
    
    columns = list(res[0].keys())
    data = [list(record.values()) for record in res]
    df = pd.DataFrame(data=data, columns=columns)
    df = df.drop(["attributes"], axis=1)
    
    if to_s3:
        if save_to_s3(df):
            print("Saved Contacts to AWS S3 successfully")
    else:
        df.to_csv("app/downloads/contacts.csv", index=False)
        print("Downloaded Contacts to 'app/downloads' folder successfully")

