from bs4 import BeautifulSoup
import lxml
import urllib2

response = urllib2.urlopen("https://en.wikipedia.org/wiki/Beautiful_Soup") #Get markdown

html = response.read() #Markdown

soup = BeautifulSoup(html, "lxml") # Using lxml parser
print(soup.title)
print(soup.body.findAll(text="Python"))