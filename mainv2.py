import lxml, urllib.request
from bs4 import BeautifulSoup as bs
from textblob import TextBlob
from PageScraper import *
from main import *
from NewsSentimentAnalysis import *




if __name__=='__main__':
	lists=[]
	print("\n HELLO!!! What do you wanna do know? : \n 1. See National News \n 2. See Sentiment Value for National News \n 3. See overall Sentiment for now. \n")

	check = input("Enter the number: ")

	pageUrls=['https://www.thehindu.com/news/national/?page=', 'https://www.thehindu.com/news/international/?page=', 'https://www.thehindu.com/sci-tech/science/?page=']

	if chk =='1':
		mainUrl = pageUrls[0]
	elif chk == '2':
		mainUrl = pageUrls[1]
	else:
		mainUrl = pageUrls[2]


	for x in range(1,3):
		newsPaper={}
		url = urlMaker(mainUrl, x)
		soup = soupee(url)
		titles, links = parser(soup)

		if check=='1':
			seeNews(titles,links)
		elif check=='2':
			sentimentAnalysis(newsPaper, titles, lists)
		else:
			avgSentiment(titles,stories)