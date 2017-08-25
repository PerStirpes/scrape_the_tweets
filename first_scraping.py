# import bs4 as bs
# import requests, urllib.request, csv
# from urllib.request import urlopen
# # sauce = urllib.request.urlopen('https://www.washingtonpost.com/graphics/politics/100-days-of-trump-tweets/?utm_term=.0c2052f6d858').read()
# sauce = urlopen("file:///Users/booboo/Rithm/scrape_the_tweets/index_tweets.html").read()
# soup = bs.BeautifulSoup(sauce, 'html.parser')

# lists = soup.find_all('li', class_='visible')
# dates = soup.find_all("li", attrs={"data-date": True})

# tweet_data = ['date, time, tweets']

# for li in	dates[1:]:
# 	date = li['data-date']
# 	tweet_data.append([date])

# for list in lists[1:]:
# 	time = list.find_all('span', {"class": "gray"})[0].text
# 	tweets = list.text
# 	tweet_data.append([time, tweets])

# with open('tweets_attempt_8.csv', 'w') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerows(tweet_data) 

# # # # prints all text 
# # for list in soup.find_all('li'):
# # 	print(list.text)
# ###########

import csv; 
import requests; 
from bs4 import BeautifulSoup

with open('tweets_results.csv', 'w', newline='', encoding='utf8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['date','time','tweets'])

    sauce = requests.get('https://www.washingtonpost.com/graphics/politics/100-days-of-trump-tweets/?utm_term=.0c2052f6d858',headers={"User-Agent":"Existed"}).text
    soup = BeautifulSoup(sauce,"html.parser")

    for item in soup.select("li.pg-excerpt.visible"):
        date = item.get('data-date')
        time = item.select("span.gray")[0].text
        title = item.text.strip()
        print(date, time, title[10:])
        writer.writerow([date, time, title[10:]])