from src import Scraper, Parser

def test_parse_default():
    scraper = Scraper()
    parser = Parser()

    page = scraper.get_page('https://geohints.com/Poles')

    items = parser.parse_default(page=page)

    assert items

def test_parse_domains():
    scraper = Scraper()
    parser = Parser()

    page = scraper.get_page('https://geohints.com/Domains')

    items = parser.parse_domains(page=page)

    assert items