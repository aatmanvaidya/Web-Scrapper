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
print(anchors)