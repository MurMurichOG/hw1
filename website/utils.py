import requests
from bs4 import BeautifulSoup
from website.models import ParsedData

def parse_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h2')
    contents = soup.find_all('p')

    for title, content in zip(titles, contents):
        ParsedData.objects.create(title=title.text, content=content.text)
