# importing necessary websraping tools to be used in the project

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# getting the url
r = requests.get("https://www.consumeraffairs.com/travel/airbnb.html?page=1")

soup = BeautifulSoup(r.text, 'html.parser')

# structuring things
rating=[]
authors=[]
review=[]
date=[]
comment=[]

# scraping data with soup


for item in soup.findAll('div', {'class':'rvw__hdr-stat'}):
    rating.append(item.find_next('img').get('alt'))

   
for item in soup.findAll('strong', {'class': 'rvw-aut__inf-nm'}):
    authors.append(item.text)

for item in soup.findAll('strong', {'class': 'rvw-aut__inf-ver'}):
    review.append(item.get_text(strip=True))

for item in soup.findAll('span', {'class': 'ca-txt-cpt'}):
    date.append(item.text)

for item in soup.findAll('div', {'class': 'rvw-bd'}):
    comment.append(item.find('p').text)

# append all scraped data into an array

data = []
for items in zip(rating, authors, review, date, comment):
    data.append(items)