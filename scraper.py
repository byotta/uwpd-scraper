"""
Scrapes UWPD recent crime log webpage and sends an email when it updates
"""
import requests
import time
from bs4 import BeautifulSoup

url = "http://police.uw.edu/crimedata/60daylog/"

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.find("iframe", {"class": "uw-pdf-view"})
    firstPDF = element["src"]

    time.sleep(300)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.find("iframe", {"class": "uw-pdf-view"})
    secondPDF = element["src"]
    if firstPDF != secondPDF:
        # alert with email
        print("new crime")
