from bs4 import BeautifulSoup # Module to sort through the html
import lxml # Module to parse through the html for BeautifulSoup
import urllib2 # Gets html
import webbrowser # This module can control the browser

# url = "https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com"
url = "https://princeton.service-now.com/kb_view.do?sysparm_article=KB0010348"
try: # Make sure link exists
    urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print(e.code) # Return any errors
except urllib2.URLError, e:
    print(e.args)

response = urllib2.urlopen(url) #Get markdown

html = response.read() #Markdown

soup = BeautifulSoup(html, "lxml") # Using lxml parser
print(soup.title)
print(soup.body)
