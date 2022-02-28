from simple_salesforce import Salesforce

from config import Config


sf = Salesforce(username=Config.username,
                password=Config.password,
                security_token=Config.securty_token)


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
    pass


# create_users()

