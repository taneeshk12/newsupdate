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
from streamlit_autorefresh import st_autorefresh
import time

# send_email = st_autorefresh(interval=2000, limit=1)


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
# Initialize the Firebase app only if it's not already initialized
if not firebase_admin._apps:
    app = firebase_admin.initialize_app(cred)

# app = firebase_admin.initialize_app(cred)
from requests_html import HTMLSession

session = HTMLSession()

#use session to get the page
# r = requests.get('https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en')
#use session to get the page
r = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')

# india = requests.get('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')

business = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')

tech = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')

ent = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')

sports = requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')

soup = BeautifulSoup(r.content, 'html.parser')
# soup_india = BeautifulSoup(india.content, 'html.parser')
soup_business = BeautifulSoup(business.content, 'html.parser')
soup_tech = BeautifulSoup(tech.content, 'html.parser')
soup_ent = BeautifulSoup(ent.content, 'html.parser')
soup_sports = BeautifulSoup(sports.content, 'html.parser')
l=[]
t=[]
web_url = 'http://news.google.com'


# create empty dictisonary to store links and text
link_dict = {}
# link_dict_india = {}
link_dict_business={}
link_dict_tech = {}
link_dict_ent = {}
link_dict_sports ={}

# loop through each anchor tag in the div tag
for link_tag in soup.find_all('a',{"class":"WwrzSb"}):
        link = urljoin(web_url,link_tag.get('href'))
        # find the next a tag after the current anchor tag
        text_tag = link_tag.find_next('a',{"class":"gPFEn"})
        # extract the text from the a tag
        text = text_tag.text if text_tag is not None else ''
        # add the link and text to the dictionary
        link_dict[link] = text

# for link_tag in soup_india.find_all('a',{"class":"WwrzSb"}):
#         link = urljoin(web_url,link_tag.get('href'))
#         # find the next a tag after the current anchor tag
#         text_tag = link_tag.find_next('a',{"class":"gPFEn"})
#         # extract the text from the a tag
#         text = text_tag.text if text_tag is not None else ''
#         # add the link and text to the dictionary
#         link_dict_india[link] = text

for link_tag in soup_business.find_all('a',{"class":"WwrzSb"}):
        link = urljoin(web_url,link_tag.get('href'))
        # find the next a tag after the current anchor tag
        text_tag = link_tag.find_next('a',{"class":"gPFEn"})
        # extract the text from the a tag
        text = text_tag.text if text_tag is not None else ''
        # add the link and text to the dictionary
        link_dict_business[link] = text

for link_tag in soup_tech.find_all('a',{"class":"WwrzSb"}):
        link = urljoin(web_url,link_tag.get('href'))
        # find the next a tag after the current anchor tag
        text_tag = link_tag.find_next('a',{"class":"gPFEn"})
        # extract the text from the a tag
        text = text_tag.text if text_tag is not None else ''
        # add the link and text to the dictionary
        link_dict_tech[link] = text

for link_tag in soup_ent.find_all('a',{"class":"WwrzSb"}):
        link = urljoin(web_url,link_tag.get('href'))
        # find the next a tag after the current anchor tag
        text_tag = link_tag.find_next('a',{"class":"gPFEn"})
        # extract the text from the a tag
        text = text_tag.text if text_tag is not None else ''
        # add the link and text to the dictionary
        link_dict_ent[link] = text

for link_tag in soup_sports.find_all('a',{"class":"WwrzSb"}):
        link = urljoin(web_url,link_tag.get('href'))
        # find the next a tag after the current anchor tag
        text_tag = link_tag.find_next('a',{"class":"gPFEn"})
        # extract the text from the a tag
        text = text_tag.text if text_tag is not None else ''
        # add the link and text to the dictionary
        link_dict_sports[link] = text
 

soup = BeautifulSoup(r.content, 'html.parser')

l = []
t = []
web_url = 'http://news.google.com'

# create empty dictisonary to store links and text
# link_dict = {}

# loop through each anchor tag in the div tag
# for link_tag in soup.find_all('a', {"class": "WwrzSb"}):
#     link = urljoin(web_url, link_tag.get('href'))
#     # find the next h4 tag after the current anchor tag
#     text_tag = link_tag.find_next('a', {"class": "gPFEn"})
#     # extract the text from the h4 tag
#     text = text_tag.string if text_tag is not None else ''
#     # add the link and text to the dictionary
#     link_dict[link] = text

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

        # msg = MIMEMultipart("alternatives")
        # body = '''
        # <html>
        # <head></head>
        # <body>
        #     <p>Hello,</p>
        #     <p>Here are todays top headlines:</p>
        #     <ul> '''

        # for key, value in link_dict.items():
        #     body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"

        # body += """
        #     </ul>
        #     <p>visit out website <a href="https://ideaism.in">click here</a></p>
        #     <p>Click <a href="https://www.youtube.com/channel/UC3AxbWaYSn9c57izkVQhTGA">here</a> for more information.</p>
        # </body>
        # </html>
        # """
        # msg.attach(MIMEText(body, 'html'))

        # em = EmailMessage()
        # em['From'] = email_sender
        # em['To'] = ",".join(email_reciever)
        # em['subject'] = "Today's news headlines just for you"
        # em.set_content(msg)
        subject = "Today's news headlines just for you"
# body = "title: {} ---------->   {}".format(link_dict.keys(),link_dict.values())
        msg = MIMEMultipart("alternatives")
        body = '''
            <html>
            <head>
                <style>
                    body {
                        font-size: small;
                        color: white;
                        background-color: #1a1a1a;
                        padding: 20px;
                        font-family: Arial, sans-serif;
                    }
                    h2 {
                        font-size: 1em;
                        # color: white;
                        
                    }
                    ul {
                        list-style-type: none;
                        padding: 0;
                    }
                    li {
                        margin-bottom: 10px;
                        font:size:small;
                    }
                    a {
                        color: white;
                        text-decoration: none;
                        font:size:small;
                    }
                    a:hover {
                        text-decoration: underline;
                        font:size:small;
                    }
                </style>
            </head>
            <body>
                <p>Hello,</p>
                <p>Here are today's top headlines:</p>
                <h2>Today's Top World News Headlines ------&gt;&gt;&gt;</h2>
                <ul>
            '''
        body += "<h2>todays top world news headlines ------>>>><h2>"

        count = 0
        for i,(key, value) in enumerate(link_dict.items()):
            if count == 6:
                break
            if i % 4 == 0:
                body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"
                count += 1    



        # body += "<h2>todays top India news headlines ------>>>><h2>"



        # count = 0
        # for i,(key, value) in enumerate(link_dict_india.items()):
        #     if count == 6:
        #         break
        #     if i % 4 == 0:
        #         body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"
        #         count += 1   

        body += "<h2>todays top business news headlines ------>>>><h2>"

        count = 0
        for i,(key, value) in enumerate(link_dict_business.items()):
            if count == 6:
                break
            if i % 4 == 0:
                body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"
                count += 1   
            
        body += "<h2>todays top tech news headlines ------>>>><h2>"

        count = 0
        for i,(key, value) in enumerate(link_dict_tech.items()):
            if count == 6:
                break
            if i % 4 == 0:
                body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"
                count += 1   

        body += "<h2>todays top entertainment news headlines ------>>>><h2>"

        count = 0
        for i,(key, value) in enumerate(link_dict_ent.items()):
            if count == 6:
                break
            if i % 4 == 0:
                body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"
                count += 1   

        body += "<h2>todays top sports news headlines ------>>>><h2>"

        count = 0
        for i,(key, value) in enumerate(link_dict_sports.items()):
            if count == 6:
                break
            if i % 4 == 0:
                body += f"<li><h2> <a href=\"{key}\">{value}</a></h2></li> \n \n"
                count += 1   

        # print(link_dict.keys())
        body += """
            </ul>
            <p>Click <a href="https://ideaism.in/">here</a> for more information.</p>
        </body>
        </html>
        """
        msg.attach(MIMEText(body,'html'))

        em= EmailMessage()
        em['From'] = email_sender
        em['To'] = ",".join(email_reciever)
        em['subject'] = subject
        em.set_content(msg)

        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())


# send_email()
# schedule.every(1).seconds.do(send_email)

# while True:
#     # check whether the scheduled task is due to run
#     schedule.run_pending()
#     time.sleep(1)

while True:
    send_email()
    time.sleep(3600)
    