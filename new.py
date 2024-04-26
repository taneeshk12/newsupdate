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

# firebase_credentials = credentials.Certificate({
#     "type": os.environ["service_account"],
#     "project_id": os.environ["ideaism-blog"],
#     "private_key_id": os.environ["f03ffb0eb89a99cc50cc0645915e10ab175e8377"],
#     "private_key": os.environ["-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8VM1ibTVeOzGR\n2b8KW+v96/DXDbP5JmZLEnqKjFxwCiaW+YTnEYJZ8WdErdnrzdXBKqgHZ/j3Fo+Z\n+YKbFFTQdVT6OMyFjrNSPmle2Xkhd8mV1mhGTvE0ytZrwpzDDEQA44Z+QVisP9Wv\n33DCkPPNLzKqSCGSq6mgXWjqds55uy1TRb8zLI/QzriDii71TR1seSOuLCxwd2mE\nj/fq8TaK8PxyVW0EWp/X0FjkYfqiFUgDMCKCfBW5eNZDGIcZT6KTfAwwzhwVPh/u\nXbIopQzIj5GacFBndFToRmUkRkVpzK2hI1eTcSKiSXlSWioBgFBgQHnMBDAA62r0\nn9ZXy459AgMBAAECggEAUHsy6/F8gYDtTYVOgRhIMNJvsQ8/jmUNCN7kNCoIZK7J\nz/HgjDhsypABkBV1T7I+OxbGCKgzejAPfP7mA+y70/uYLXgxWo/hbO+T6v8npxhA\nMsKV/BnHNUbLO/DGOgoXU4Pn2TOGt9FtuYNUdikortIRJji99CZczlWsvKm50cXh\n70FvtQFEDb5dYv9o34CrABRYvkjALthW08C6njTWPEmVCDHextP4MzmyO1RYRSQ8\ncODfsN3jPHQ34qStJv+Upo5sU27YRKdOyjTZ9SHeB03sshO4bGD4BjM8Abdt+h3j\nfxFYERkDUJudnN0Zfy6Bhv+GxJbMdUXUTh7wT6+ORwKBgQDpvmzWcUsiqCJq3eD2\nzPU/zfTXTCvQIpb0JLAgHKf0YcjScTRju8iX383IMr7vlH6vbGAow9/LU7uzlZYp\n9zJzHdLCpmohXkVrFEB9Cc3RzaIVU19q8nTe7KB5BYmahIHBlpcnigbbAoY4imxV\nT0UF1o8ZcMeiNs7l10tCu1qy8wKBgQDOQ26Ud3Kj4TrVZulm99U9cHQVlmVqkBi9\nsfZVv1iWhigJqqGT/zRje+qVuu6sNqhUDQNQWdCdpeqUgQjP6pv9Jv7U+Fjy//3Y\nFIytYXXEDZbDQo0ecIBrU/Mo39lsK+kf0JHDI6Afw8l3e+BMnGdMHVaOYi2mQ16p\nYFbAsla0zwKBgQC1N/e1whxYgDY+2ErjzT+O+iSLDvkg4tBZ9F/AZbcpVu6ViULu\n19XLOa6XOhCiOmSFqOZcdI/7Wa26q4zCeG5apZKTauX5fNchD5B34LP7pwu0sPDX\nP6awdpBrg4mNjJH0/sWt1+s8vRZGm7sl4NFIl3JWbQO5lfiOZX5p/EtzVQKBgBjm\nuyrhYM24G0o4KmVr9ip8sQcKKSQ8UUBVg8/GUgOaHqtMFkWvwbtg8mkxMC9KSfgb\nuhKxRSZDKZbUHSQ8xqhBVPKRKOvtS9ASawljgrwwh8r69d5+5oIOmISOwcj1ZCeb\nHn3YhzROhrwOEH4vQ6lEwXZfE/PGnl8EanTJEv6xAoGBAJzVpP5wBV7Na87Btkte\nfkCJnhgym+AC89TgH/Gb89STDPGauxTV9fBwb9DxzNYp4rlJE+F8gh9WcN/AO8wk\nhEQQyJ+/ypXq/BrVveCOX3BmBJUjZkRoyFGsVOWaxAC81QZaSNB2VrR3pmTND5QJ\njbpAllgAZVKFJjqVCO+4MoHS\n-----END PRIVATE KEY-----\n"].replace("\\n", "\n"),
#     "client_email": os.environ["firebase-adminsdk-zeusk@ideaism-blog.iam.gserviceaccount.com"],
#     "client_id": os.environ["111195026095062633402"],
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": os.environ["https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zeusk%40ideaism-blog.iam.gserviceaccount.com"]
# })



# # cred = credentials.Certificate("./ServiceAccountKey.json")
# app = firebase_admin.initialize_app(firebase_credentials)
# app = firebase_admin.initialize_app(cred)
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