from src import Scraper, Parser, CSV

def test_write_csv():
    scraper = Scraper()
    parser = Parser()
    csv = CSV()

    page = scraper.get_page('https://geohints.com/Poles')

    items = parser.parse_default(page=page)

    outp = csv.write_csv(items, outfile='./output/out.csv')

    assert outp