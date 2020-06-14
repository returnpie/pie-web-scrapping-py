import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    resul = requests.get(URL)
    soup = BeautifulSoup(resul.text, 'html.parser')
    pagination = soup.find("div", { "class" : "pagination"})

    links = pagination.find_all('a')

    pages = []

    for page in links[:-1]:
        pages.append(int(page.string))

    max_page = pages[-1]

    return max_page

def extract_indeed_jobs(last_page):
    # for page in range(last_page):
    resul = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(resul.text, 'html.parser')
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

    for result in results:
        title = result.find("div", {"class": "title"})
        # print(title.find("a"))
        print(title)
    print(results)