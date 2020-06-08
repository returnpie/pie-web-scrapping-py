import requests
from bs4 import BeautifulSoup

indeed_resul = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_resul.text, 'html.parser')

print(indeed_soup)