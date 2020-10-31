# Gravedigger-Web-Scraper
Python program that extracts all names and birthdays from the Eugene Pioneer Cemetery into an Excel sheet.

I scraped FindAGrave.com, which had a database of all 4,000+ graves in the cemetery I was looking at. The names were pretty straightforward, but the dates were in different formats, so you'll see some code addressing that. 
The format of the website is 20 graves/page, with a total of 207 pages, so I looped through each page. It takes a while for the program to run, both by nature and because I built in a few seconds wait time between each page so I didn't overrun the website.
The goal of this code was to allow me to sort people by their birthday; I'm working on the sorting from within the excel sheet itself rather than this code. 

This is a first for me in a lot of things--webscraping generally, working with data structures, panda, etc. It's also my first real solo project! As such, you'll see a lot of similarities between my code and Angelica Dietzel's, in her walkthrough on medium.com (https://medium.com/better-programming/how-to-scrape-multiple-pages-of-a-website-using-a-python-web-scraper-4e2c641cff8). 

The last thing I'll address: why am I doing this project in the first place? I live in Eugene, and spend a lot of time in this cemetary, so I thought it'd be nice to pay my respects to people on their birthdays!
