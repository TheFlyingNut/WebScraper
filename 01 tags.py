import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

#print(soup.title.string, type(soup.title.string))
for link in soup.find_all("a"):
    print(link)