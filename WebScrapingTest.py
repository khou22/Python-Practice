from bs4 import BeautifulSoup
import lxml
import urllib2

response = urllib2.urlopen("https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com") #Get markdown

html = response.read() #Markdown

soup = BeautifulSoup(html, "lxml") # Using lxml parser
print(soup.title)
print(soup.body)
