# Salesforse integration with Flask

# Used urls
1. https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart.htm
2. https://www.sfdcstop.com/2019/01/how-to-connect-to-salesforce-with.html


# Structure
GET /  - index page


# How to run it
1. pip install -r requirements.txt
2. From root:
```gunicorn "run:create_app()"```
3. Open openapi docs: https://127.0.0.1:5000/swagger to test the API
