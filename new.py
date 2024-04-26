import streamlit as st
from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd
from requests_html import HTMLSession
import urllib.request
from urllib.parse import urljoin
from email.message import EmailMessage
from passw import password
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore


import os


firebase_credentials = {
    "type": st.secrets["firebase"]["type"],
    "project_id": st.secrets["firebase"]["project_id"],
    "private_key_id": st.secrets["firebase"]["private_key_id"],
    "private_key": st.secrets["firebase"]["private_key"],
    "client_email": st.secrets["firebase"]["client_email"],
    "client_id": st.secrets["firebase"]["client_id"],
    "auth_uri": st.secrets["firebase"]["auth_uri"],
    "token_uri": st.secrets["firebase"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
}

firebase_credentials['private_key'] = firebase_credentials['private_key'].replace("\\n", "\n")

cred = credentials.Certificate(firebase_credentials)
app = firebase_admin.initialize_app(cred)
from requests_html import HTMLSession

session = HTMLSession()

#use session to get the page
r = requests.get('https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en')

soup = BeautifulSoup(r.content, 'html.parser')

l = []
t = []
web_url = 'http://news.google.com'

# create empty dictisonary to store links and text
link_dict = {}

# loop through each anchor tag in the div tag
for link_tag in soup.find_all('a', {"class": "WwrzSb"}):
    link = urljoin(web_url, link_tag.get('href'))
    # find the next h4 tag after the current anchor tag
    text_tag = link_tag.find_next('a', {"class": "gPFEn"})
    # extract the text from the h4 tag
    text = text_tag.string if text_tag is not None else ''
    # add the link and text to the dictionary
    link_dict[link] = text

# print the dictionary

f = []
count = 0
for key, value in link_dict.items():
    if count == 4:
        break
    f.append((key, value))
    count += 1

k = '{f}'
print(f)
def send_email():

 
   

    store = firestore.client()
    doc_ref = store.collection('mail').limit(2)
    mail_ids = []
    try:
        docs = doc_ref.get()
        for doc in docs:
            mail_id = doc.to_dict().get('text')
            if mail_id:
                mail_ids.append(mail_id)
            print(u'Doc Data:{}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'Missing data')


    email_sender = 'the.ideaism08@gmail.com'
    email_password = password
    # email_reciever = st.text_input("Enter recipient email addresses (separated by commas):")
    email_reciever = ','.join(mail_ids)
    if email_sender and email_password and email_reciever:
        email_sender = email_sender.strip()
        email_password = email_password.strip()
        email_reciever = [email.strip() for email in email_reciever.split(',')]

        msg = MIMEMultipart("alternatives")
        body = '''
        <html>
        <head></head>
        <body>
            <p>Hello,</p>
            <p>Here are todays top headlines:</p>
            <ul> '''

        for key, value in link_dict.items():
            body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"

        body += """
            </ul>
            <p>visit out website <a href="https://ideaism.in">click here</a></p>
            <p>Click <a href="https://www.youtube.com/channel/UC3AxbWaYSn9c57izkVQhTGA">here</a> for more information.</p>
        </body>
        </html>
        """
        msg.attach(MIMEText(body, 'html'))

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = ",".join(email_reciever)
        em['subject'] = "Today's news headlines just for you"
        em.set_content(msg)

        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())


schedule.every(12).hours.do(send_email)

while True:
    # check whether the scheduled task is due to run
    schedule.run_pending()
    time.sleep(1)