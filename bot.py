import pandas as pd
from sender import email_sender
import time

dataframe = pd.read_excel('company data.xlsx')


content_message = """Multi line email sending bot checking.
it should not bring any escape characters..."""



for index, row in dataframe.iterrows():
    company_name = dataframe['company name'][index]
    website = dataframe['website'][index]
    emails = dataframe['gmail'][index]
    emails_list = emails.split(',')
    problems = dataframe['problems'][index]

    sender = email_sender(company_name, website, emails_list, problems, content_message)

    if sender:
        print("all emails send successfully....")
    else:
        print("Something is wrong check please. All emails are not sent successfully...")
