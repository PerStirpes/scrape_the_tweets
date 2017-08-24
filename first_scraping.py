import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.washingtonpost.com/graphics/politics/100-days-of-trump-tweets/?utm_term=.ea2e3db87ee2'
data = requests.get(url).text
soup = bs4.BeautifulSoup(data, "html.parser")
links = soup.select("data.data-date")
letters = soup.find_all("li", class_="visible")


with open("tweets_2.html", "r+") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))