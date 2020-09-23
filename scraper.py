"""
Scrapes UWPD recent crime log webpage and sends an email when it updates
"""
import requests
from bs4 import BeautifulSoup

url = "http://police.uw.edu/crimedata/60daylog/"

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.find("iframe", {"class": "uw-pdf-view"})
    firstPDF = element["src"]
    print(firstPDF)
