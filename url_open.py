import urllib

def extract_source(hyperlink):
	hyperlink_source = urllib.urlopen(hyperlink)
	html_source = hyperlink_source.read()
	return html_source

print extract_source("http://www.thisamericanlife.org")

