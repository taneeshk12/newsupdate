from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd
from requests_html import HTMLSession
import urllib.request
from urllib.parse import  urljoin
# import smtplib as s
from email.message import EmailMessage
from pass import password
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



from requests_html import HTMLSession
session = HTMLSession()

#use session to get the page
r = requests.get('https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en')




soup = BeautifulSoup(r.content, 'html.parser')

l=[]
t=[]
web_url = 'http://news.google.com'


# create empty dictisonary to store links and text
link_dict = {}



# loop through each anchor tag in the div tag
for link_tag in soup.find_all('a',{"class":"WwrzSb"}):
        link = urljoin(web_url,link_tag.get('href'))
        # find the next h4 tag after the current anchor tag
        text_tag = link_tag.find_next('h4',{"class":"gPFEn"})
        # extract the text from the h4 tag
        text = text_tag.text if text_tag is not None else ''
        # add the link and text to the dictionary
        link_dict[link] = text

# print the dictionary



# link_tags = soup.find_all('div', {"class":"WwrzSb"})

# # create empty dictionary to store links and text
# link_dict = {}

# # loop through each link tag and extract the link and text
# for link_tag in link_tags:
#     link = (urljoin(web_url,link_tag.get('href')))
#     text = link_tag.find('h4',{"class":""}).text
#     link_dict[link] = text

# for souop in soup:

#     for title in soup.find_all('a',{"class":"WwrzSb"}):
       
        
#         l.append(urljoin(web_url,title.get('href')))
#         t.append(soup.find('h4').text)
        
#     # for title in soup.find_all('h4',{"class":"gPFEn"}):
       

#     #     t.append(title.text)

# m=len(t)

# # for i in range(m):   
# #     q={
                
# #             'title':t[i],
# #             'link':l[i]
# #         }
# q={}
# for key in t:
#     for value in l:
#         q[key] = value
#         l.remove(value)
#         break
 

f=[]
count = 0
for key, value in link_dict.items():
    if count == 4:
        break
    f.append((key, value))
    count += 1

k='{f}'
# print(f)

email_sender='the.ideaism08@gmail.com'
email_password= password

email_reciever = ['taneeshkpatel08@gmail.com','jdrashti8@gmail.com','21bt04089@gsfcuniversity.ac.in']

subject = "Today's news headlines just for you"
# body = "title: {} ---------->   {}".format(link_dict.keys(),link_dict.values())
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

# print(link_dict.keys())
body += """
    </ul>
    <p>Click <a href="https://www.youtube.com/channel/UC3AxbWaYSn9c57izkVQhTGA">here</a> for more information.</p>
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

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
