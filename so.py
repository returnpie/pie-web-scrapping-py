import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find_all("a", {"class": "s-pagination--item"})
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(page)


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
