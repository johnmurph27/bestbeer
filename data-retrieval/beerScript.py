import argparse
from bs4 import BeautifulSoup
import urllib2
import re
import sys

def url_to_beer_name(url):
	parsed_url= url.split('/')
	return parsed_url[-1].replace('-', ' ').title()

parser = argparse.ArgumentParser(description = "Process Search Term")
parser.add_argument('searchTerm')
args = parser.parse_args()
search = args.searchTerm
search = search.replace(' ', '+')
search = "http://beersmithrecipes.com/searchrecipe?uid=&term=" + search
html = urllib2.urlopen(search)
soup = BeautifulSoup(html.read())


links = []
for link in soup.find_all('a'):
	if "viewrecipe" in link.get('href'):
		links.append(link.get('href'))

if len(links)==0:
	print "No results,try again."
	sys.exit()

print 'Which beer recipe do you want to choose? Type in the appropriate number, from 1 to ' + str(len(links))
iterator=1
parser = []
for link in links:
	print str(iterator)+ ': ' + url_to_beer_name(link)	
	iterator+=1

while(True):
	response = input()
	if isinstance(response, int) and response>=1 and response<=len(links):
		search = links[response-1]
		break
	else:
		print "Invalid response, try again."

html = urllib2.urlopen(search)
soup = BeautifulSoup(html.read())

trs = soup.find_all('tr')
BittInd = 0;
ABVInd = 0;
for i in range(0,(len(trs)-1)):
	if 'Bitterness' in str(trs[i]):
		BittInd = i
	if 'ABV' in str(trs[i]):
		ABVInd = i;
out = str((trs[BittInd].find_all('td'))[0])+'\n' + str((trs[ABVInd].find_all('td'))[0])
regex = re.compile('<.{0,4}>')
print regex.sub('',out)

