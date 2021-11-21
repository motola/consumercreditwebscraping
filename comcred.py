# importing necessary websraping tools to be used in the project

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

r = requests.get("https://www.consumeraffairs.com/travel/airbnb.html?page=1")

soup = BeautifulSoup(r.text, 'html.parser')

rating=[]
authors=[]
review=[]
date=[]
comment=[]

