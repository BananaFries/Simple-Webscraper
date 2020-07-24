#! /usr/env/python3

import requests
from bs4 import BeautifulSoup

url = 'url-here' #the url of the website you want to scraper
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#Using class property of div to identify. You can use any div property to identify. 
item = soup.find(class_='div-identifier-here')   
 
print(item)
print(item.text)

