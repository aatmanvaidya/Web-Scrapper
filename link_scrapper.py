import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/home/"

#Get the HTML
req = requests.get(url)
htmlContent = req.content
#print(htmlContent)

#parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

#Get the Title of the HTML page
title = soup.title

# Get all the anchor tags
anchors = soup.find_all('a')

#Get all the anchor tags from the page
anchors=soup.find_all('a')
all_links = set()

#Get all the links on the page
for link in anchors:
    if(link != 'a'):
        linkText = "https://www.geeksforgeeks.org/" + link.get('href')
        all_links.add(link)
        print(linkText)