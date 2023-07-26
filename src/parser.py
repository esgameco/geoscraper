from bs4 import BeautifulSoup

class Parser:
    def __init__(self) -> None:
        self.base_url = 'https://geohints.com/'

    def parse_default(self, page: BeautifulSoup) -> any:
        """Parses BeautifulSoup object using Bollard class"""
        items = page.find_all(name='div', attrs={'class': 'bollard'})

        output = []
        for item in items:
            try:
                output.append([
                    f'<img src="{self.base_url + item.find("img").get("src")}">', 
                    f'{item.find("p").get_text().replace("🌍", "").strip()} <a href="{item.find("a").get("href")}">O</a>',
                ])
            except Exception:
                pass

        return output
    
    def parse_domains(self, page: BeautifulSoup) -> any:
        items = page.find('body').get_text().split('\n')[3:]
        items = [x for x in items if x]
        output = []
        for i in items:
            output.append(i.split(' - '))

        return output
