import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/home/"

#Get the HTML
req = requests.get(url)
htmlContent = req.content
#parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

#Get the Title of the HTML page
title = soup.title

# Get all the paras from the page
paras = soup.find_all('p')

print(paras)