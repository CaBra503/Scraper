import requests
from bs4 import BeautifulSoup
import re
import csv
# Regex to grab specifics of url.
	# regEx = re.match('^?P<protocol>[\w]+)\:\/\/(?P<host>[\w\.\-]+)(\:(?P<port>\d+))?((?P<path>\/[^\?\#\n]*)(\?(?P<params>(?P<first_param>[^\#\?\&\=\n]+(=[^\#\?\&\=\n]*)*)(\&(?P<param_more>[^\#\?\&\=\n]+(=[^\#\?\&\=\n]*)*))*))?(\#(?P<tag>[^\#\?\n]+)?)?)?$')
request = requests.get('https://www.WebsiteWithSomeKindOfInventoryYouWantToParse.com/*')
soup = BeautifulSoup(request.text, 'html.parser');
makes = soup.find_all('li', attrs={'class': 'make'})
all_makes = []
for make in makes:
	title = str(make.find('h3'))
	url = str(make.find('a')['href'])
	all_makes.append((title, url))
print('Successfull Scrape of  site')
# Writes to csv
with open('Attatchments_600Tl.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(all_makes)