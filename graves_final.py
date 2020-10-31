'''
Title: Gravedigger - Final

Author: Amanda Givens

Credits: Angelica Dietzel from medium.com
'''

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint


names = []
birthdays = []

pages = np.arange(1,208,1) #207 pages on this website

page_update = 0 


for page in pages:
    
    page = requests.get('https://www.findagrave.com/cemetery/39286/memorial-search?page=' + str(page))
    soup = BeautifulSoup(page.text, 'html.parser')
                        
    #finds each grave's memorial info
    grave_div = soup.find_all('div', class_='memorial-item---grave')

    #don't overwhelm server!
    sleep(randint(2,10))

    #loop through each grave and extract name and birthday
    for container in grave_div:

        name_object = container.h2.i
        
        if name_object is not None:
            name = name_object.text
            
        names.append(name)

        bday_object = container.find('b',class_= 'birthDeathDates')
        
        if bday_object is not None:
            bday = bday_object.text
            
        if (len(bday) <= 22): #if no month/day listed
            bday = 'unknown'  
        elif (len(bday) <= 25): #removes death day
            bday = bday[0:11].rstrip()
            
        birthdays.append(bday)
        

    page_update += 1 
    print('Page', page_update, 'is done.')


#build dataframe
graves = pd.DataFrame({
    'Names': names,
    'Birthdays': birthdays,
    })

#see dataframe (optional)
print(graves)

#save data to CSV file
graves.to_csv(r'C:\Users\glute\OneDrive\Documents\CIS 210\gravesite_final_final.csv', index = False, header = True)

