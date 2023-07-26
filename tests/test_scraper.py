from src import Scraper

def test_get_page():
    scraper = Scraper()

    page = scraper.get_page('https://geohints.com/Poles')

    assert page.find('div')