import requests
from bs4 import BeautifulSoup

indeed_resul = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_resul.text, 'html.parser')


pagination = indeed_soup.find("div", { "class" : "pagination"})

# print(pagination)

pages = pagination.find_all('a')

# print(pages)

spans = []

for page in pages[:-1]:
    spans.append(int(page.string))
    # print(page.find("span"))

print(spans)