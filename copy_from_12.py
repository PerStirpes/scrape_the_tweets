import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

file = urlopen("file:///Users/booboo/Rithm/scrape_the_tweets/tweets.html").read()
# url = 'file://Users/booboo/Rithm/scrape_the_tweets/tweets.html'
data = requests.get(url)
# data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")
links = soup.select("data.data-date")
letters = soup.find_all("li", class_="visible")

for li in soup.find_all('li'):
    print(li.text)
# from IPython import embed; embed()

# with open("tweets.html", "r") as f:
    
#     contents = f.read()

#     soup = BeautifulSoup(contents, 'lxml')

#     for tag in soup.find_all("li"):
#         print("{0}: {1}".format(tag.name, tag.text))
# /Users/booboo/web_scraping_intro/tweets.html
# file:///Users/booboo/Rithm/scrape_the_tweets/tweets.html


