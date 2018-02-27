#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, time, pyperclip

def getLink(search, num):
	session = requests.Session()
	session.trust_env = False
	if num == 0:
		res = session.get('https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + search + '&rh=i%3Aaps%2Ck%3A' + search)
	elif num > 10:
		webbrowser.open('https://www.amazon.com/s/field-keywords=' + search)
		sys.exit()
	else:
		res = session.get('https://www.amazon.com/s/ref=nb_sb_noss_' + str(num) + '?url=search-alias%3Daps&field-keywords=' + search + '&rh=i%3Aaps%2Ck%3A' + search)

	# Retrieve top search result links.
	soup = bs4.BeautifulSoup(res.text, "lxml")

	# Open a browser tab for each result.
	# link = soup.select('a')
	# print(link)
	link = soup.select('.s-access-detail-page')
	# print(link)

	if not link:
		getLink(search = search, num = num + 1)
	else:
		webbrowser.open(link[0].get('href'))

s = ""
if(len(sys.argv) > 1):
	s = '%20'.join(sys.argv[1:])
else:
    s = pyperclip.paste()
    keywords = s.split(" ")
    s = '%20'.join(keywords)

getLink(search = s, num = 0)