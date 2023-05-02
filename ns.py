from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd
from requests_html import HTMLSession
import urllib.request
from urllib.parse import  urljoin

# session = HTMLSession()

# #url of the page that we want to Scarpe
# #+str() is used to convert int datatype of the page no. and concatenate that to a URL for pagination purposes.
# URL = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'

# try:
#      # this might throw an exception if something goes wrong.
     
#      pages= requests.get(URL)
#      # this describes what to do if an exception is thrown 
# except Exception as e:    
    
#     # get the exception information
#     error_type, error_obj, error_info = sys.exc_info()      
    
#     #print the link that cause the problem
#     print ('ERROR FOR LINK:',URL)
    
#     #print error info and line that threw the exception                          
#     print (error_type, 'Line:', error_info.tb_lineno)
    

# # r.html.render(sleep=1,scrolldown=0)
# # articles = r.html.find('article')
# # for item in articles:
# #      newsitem = item.find('h3', first=True)
# #      title = newsitem.text
# #      link = newsitem.absolute_link
# #      print(title, link)
# soup = BeautifulSoup(pages.content, 'html.parser')
# q=[]
# for souop in soup:
#     for title in soup.find_all('a',{"class":"WwrzSb"}):
#         q.append(title.text)
#         m=title.absolute_links
# print(m)

#og code

from requests_html import HTMLSession
session = HTMLSession()

#use session to get the page
r = requests.get('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
# r.html.render(sleep=1, scrolldown=5)
# soup = BeautifulSoup(r.content, 'html.parser')
# #find all the articles by using inspect element and create blank list
# articles = soup.find('article')

# newslist = []

# #loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
# for item in articles:
    
#     for newsitem in item.find_all('h4', {"class":'gPFEn'}):
#         # newslist.append(newsitem.text)
#         print(newsitem)
#         # print(newslist)
#         # link = newsitem.absolute_links
#         # newsarticle = {
#         #     'title': title,
#         #     'link': link 
#         # }
#     # newslist.append(newsarticle)
#     # print(newslist)
    
# #print the length of the list
# print(newslist)



soup = BeautifulSoup(r.content, 'html.parser')

l=[]
t=[]
web_url = 'https:news.google.com/'
for souop in soup:

    for title in soup.find_all('a',{"class":"WwrzSb"}):
       
        
        l.append(urljoin(web_url,title.get('href')))
        
    for title in soup.find_all('h4',{"class":"gPFEn"}):
       

        t.append(title.text)

m=len(t)
print(m)
# for i in range(m):   
#     q={
                
#             'title':t[i],
#             'link':l[i]
#         }
q={}
for key in t:
    for value in l:
        q[key] = value
        l.remove(value)
        break
 
print(q)

# print(q)