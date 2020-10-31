'''
Title: Gravedigger - V1

Author: Amanda Givens

Credits: Angelica Dietzel from medium.com
'''

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime

url = "https://www.findagrave.com/cemetery/39286/memorial-search?page=1#sr-57050141"
results = requests.get(url)

soup = BeautifulSoup(results.text, 'html.parser')

#storage initialization
names = []
birthdays = []

#grave_div finds each grave's memorial info
grave_div = soup.find_all('div', class_='memorial-item---grave')

#loop through each grave and extract name and birthday
for container in grave_div:
    
    name = container.h2.i.text
    names.append(name)

    bday = container.find('b',class_='birthDeathDates').text
    if (len(bday) <= 17): #year only
        bday = bday[0:4]
    elif (len(bday) <= 22): #month year only
        bday = bday[0:8]
    elif (len(bday) <= 25): #normal format
        bday = bday[0:11]
    birthdays.append(bday)

    
#build dataframe
graves = pd.DataFrame({
    'Name': names,
    'Birthdays': birthdays,
    })


#save data to CSV file
graves.to_csv(r'C:\Users\glute\OneDrive\Documents\CIS 210\gravesite.csv', index = False, header = True)

