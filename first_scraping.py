import csv; 
import requests; 
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('data/tweets.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['date','time','tweets'])

    sauce = requests.get('https://www.washingtonpost.com/graphics/politics/100-days-of-trump-tweets/?utm_term=.0c2052f6d858',headers={"User-Agent":"Existed"}).text
    # sauce = urlopen("file:///Users/booboo/Rithm/scrape_the_tweets/data/index_tweets_wapo.html").read()
    soup = BeautifulSoup(sauce,"html.parser")

    for item in soup.select("li.visible"):
        date = item.get('data-date')
        time = item.select("span.gray")[0].text
        title = item.text.strip()
        print(date, time, title)
        writer.writerow([date, time, title])
