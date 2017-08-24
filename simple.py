from bs4 import BeautifulSoup
import csv
#Generate lists
# A=[]
# B=[]
# C=[]

with open("tweets_2.html", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    for tag in soup.find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))
        

