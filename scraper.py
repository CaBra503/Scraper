#import libraries
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
from bs4 import BeautifulSoup
# Import for CSV Files
import csv
from datetime import datetime
# Inventory page url, stored into variable
showroom_page = 'https://www.modernfarmequipment.com/inventory/v1/current/new-holland/'

# Raw html format single page
raw_html = urlopen(showroom_page)

soup = BeautifulSoup(raw_html, 'html.parser')
makes = soup.find('ul', attrs={'class':'make'})
# first_result = makes[0]
print(makes)

# make_links = soup.select_all('.make > a')

# with open('index.csv', 'a') as csv_file:
	# writer = csv.writer(csv_file)
	# writer.writerow(makes)

#Append for printing out a CSV File of anchor tags.
