from bs4 import BeautifulSoup
from scraper import simple_get
raw_html = simple_get('https://www.modernfarmequipment.com/inventory/v1/Current/New-Holland/');
html = BeautifulSoup(raw_html,"html.parser")
for make in html.select(".makes"):
	for a in html.select(".make"):
		if a in html.select(".make a"):
			print('in')