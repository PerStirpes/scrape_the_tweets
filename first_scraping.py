import bs4 as bs
import requests
import csv
from urllib.request import urlopen

sauce = urlopen("file:///Users/booboo/Rithm/scrape_the_tweets/tweets.html").read()
soup = bs.BeautifulSoup(sauce, 'html.parser')

lists = soup.find_all('li', class_='visible')
dates = soup.find_all("li", attrs={"data-date": True})

filename = "tweets.csv"
f = open(filename, "w")

headers = "date, time, tweet"

f.write(headers)

for list in lists:
    time = list.find_all('span', {"class": "gray"})[0].text
    for li in	dates:
    	date = li['data-date']
    tweets = list.text
    print("date: " + date)
    print("time: " + time)
    print("tweet: " + tweets)

    f.write(date + "," + time + "," + tweets + "\n")

f.close()


########### for d3 ##########



##########
# # # prints all text 
# for list in soup.find_all('li'):
# 	print(list.text)
###########


# soup = BeautifulSoup(file, 'html.parser')

# time = soup.find_all('span', {'class' : 'gray'})
# print(time)

# list = soup.find_all("li")
# print(list)



# from IPython import embed; embed()

# # with open('my_csv.csv', 'w') as csvfile:
# #     writer = csv.writer(csvfile)
# #     # write header rows: eg
# #     # writer.writerow( ('name, category') )
# #     # find thing to iterate over,
# #     # iterate over it and write rows
# #     # writer.writerow( data )
# #     for li in soup.find_all('li'):
# #         # grab name
# #         # grab category
# #         writer.writerow( (date, time, text) )

# # list = soup.select("li")
# # print(list)

# csv_data = [["date", "time", "tweet"]]

# # for row in list
#     # date = row.select('.date').text
# #     time = row.select('.gray').text
# #     tweet = row.select('span').text
# #     csv_data.append([date, time, tweet])




# # with open('tweets_csv.csv', 'w') as csvfile:
# #     writer = csv.writer(csvfile)
# #     writer.writerows(csv_data) 
# #     # write header rows: eg
# #     # writer.writerow( ('name, category') )
# #     # find thing to iterate over,
# #     # iterate over it and write rows
# #     # writer.writerow( data )
# #     for li in soup.find_all('li'):
# #         # grab name
# #         # grab category
# #         writer.writerow( (date, time, text) )

# In [11]: soup.find_all("li", attrs={"data-date": True})[0]
# Out[11]: <li class="pg-excerpt visible" data-date="Jan. 20"><span class="gray">7:31 a.m.</span> It all begins today! I will see you at 11:00 A.M. for the swearing-in. THE MOVEMENT CONTINUES - THE WORK BEGINS!</li>

# In [12]: soup.find_all("li", attrs={"data-date": True})[1]
# Out[12]: <li class="pg-excerpt visible" data-date="Jan. 20"><span class="gray">12:51 p.m.</span> Today we are not merely transferring power from one Administration to another, or from one party to another – but we are transferring…</li>

# In [13]: soup.find_all("li", attrs={"data-date": True})[2]
# Out[13]: <li class="pg-excerpt visible" data-date="Jan. 20"><span class="gray">12:51 p.m.</span> power from Washington, D.C. and giving it back to you, the American People. #InaugurationDay</li>

# In [14]: soup.find_all("li", attrs={"data-date": True})[3]
# Out[14]: <li class="pg-excerpt visible" data-date="Jan. 20"><span class="gray">12:52 p.m.</span> What truly matters is not which party controls our government, but whether our government is controlled by the people.</li>

# In [15]: soup.find_all("li", attrs={"data-date": True})[3]
# Out[15]: <li class="pg-excerpt visible" data-date="Jan. 20"><span class="gray">12:52 p.m.</span> What truly matters is not which party controls our government, but whether our government is controlled by the people.</li>

# In [16]: soup.find_all("li", attrs={"data-date": True})[0]['data-date']
# Out[16]: 'Jan. 20'

# In [17]: soup.find_all("li", attrs={"data-date": True})[0].text
# Out[17]: '7:31 a.m. It all begins today! I will see you at 11:00 A.M. for the swearing-in. THE MOVEMENT CONTINUES - THE WORK BEGINS!'

# In [18]: soup.find_all("li", attrs={"data-date": True})[0].contents
# Out[18]: 
# [<span class="gray">7:31 a.m.</span>,
#  ' It all begins today! I will see you at 11:00 A.M. for the swearing-in. THE MOVEMENT CONTINUES - THE WORK BEGINS!']

# list = soup.find_all("li")

# # headers = [header.text for header in list.find_all("li", attrs={"data-date": True})]
#  rows = []
#  for row in list.find_all("li", attrs={"data-date": True}):
#  	rows.append([val.text.encode('utf8') for val in row.find_all('li')])






