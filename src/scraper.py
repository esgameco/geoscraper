import httpx

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self) -> None:
        pass

    def get_page(self, url: str) -> BeautifulSoup:
        '''Returns a BeautifulSoup object given a URL'''
        res = httpx.get(url=url)

        return BeautifulSoup(res.text, features='html.parser')
