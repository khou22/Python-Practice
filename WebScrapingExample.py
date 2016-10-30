# Creates list of all airports in the United States

from bs4 import BeautifulSoup # Module to sort through the html
import lxml # Module to parse through the html for BeautifulSoup
import urllib2 # Gets html
import webbrowser # This module can control the browser

# Use wikipedia list of all airports in the united states
url = "https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States"

try: # Make sure link exists
    urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print(e.code) # Return any errors
except urllib2.URLError, e:
    print(e.args)

response = urllib2.urlopen(url) # Get markdown
html = response.read() # Markdown
soup = BeautifulSoup(html, "lxml") # Using lxml parser

table = soup.findAll("table", { "class" : "wikitable" }) # Get table of airport names
airportRows = table[0].findAll("tr", { "valign" : "top" }) # Get table row with airport names

# Variables to collect
airportCitys = []
airportNames = []
airportAbbrv = []

print len(airportRows)
for index in range(0, len(airportRows)):
    columns = airportRows[index].findAll("td")
    city = columns[0].a.text
    name = columns[4].findAll("a")[0].text
    abbrv = columns[1].text
    print("%s (%s) in %s" % (name, abbrv, city))
