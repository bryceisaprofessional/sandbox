# Short crawler to pull job postings from engineerjobs.com
# Features to generalize url might be added. For now, copy the URL with the location and post date
# and set the number of pages to return. 
# I plan to make this smarter

import urllib
import sys
from HTMLParser import HTMLParser

def extract_source(url):
	 source = urllib.urlopen(url)
	 return source.read().decode('utf-8').encode('ascii', 'ignore')

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.titleflag = 0
		self.locationflag = 0
		self.attrcount = 0
		self.titledata = []
		self.locationdata = []
		self.companydata = []
		self.datedata = []


	def handle_starttag(self, tag, attrs):
		self.titleflag -= 1
		for name, value in attrs:
			if value == 'jobtitle':
				self.titleflag = 4	#the next 3 tags will be loc, company, date of posting

	def handle_data(self, data):
		if self.titleflag == 4:
			self.titledata.append(data)
		if self.titleflag == 3:
			self.locationdata.append(data)
		if self.titleflag == 2:
			self.companydata.append(data)
		if self.titleflag == 1:
			self.datedata.append(data)

count = 0
# f = open("jobsfile.csv", 'r+')

for page in range (1, 2):
	source_list = extract_source \
	("http://www.engineerjobs.com/jobs/canada/british-columbia/vancouver.php?f=14&page=" + str(page))

	parser = MyHTMLParser()
	parser.feed(source_list)

	for i in range(0, len(parser.datedata)):
		count += 1
		print(parser.titledata[i] 	\
		+ " , " +   parser.locationdata[i]	\
		+ " , " +  parser.companydata[i]	\
		+ " , " +  parser.datedata[i] + "\n")


print count
# print parser.titledata
# print parser.locationdata
# print parser.companydata
# print parser.datedata
