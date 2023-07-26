from src import *

if __name__ == '__main__':
    scraper = Scraper()
    parser = Parser()
    csv = CSV()
    anki = Anki()

    BASE_URL = 'https://geohints.com/'

    use_pages = ['Poles', 'Bollards', 'Flags', 'Trees', 'PostBoxes', 'Rifts', 'Scenery', 'Sidewalks', 'Stop', 'Street', 'Yield', 'Posts', 'Chevrons', 'Direction', 'Pedestrian', 'RoadNumbering', 'TrafficLights']

    # for p in use_pages:
    #     page = scraper.get_page(f'{BASE_URL}{p}')
    #     items = parser.parse_default(page=page)
    #     # outp = csv.write_csv(items, outfile=f'./output/{p}.csv')
    #     outp = anki.create_deck(items, outfile=f'./output/{p}.apkg', outname=p)
    
    # Domains
    page = scraper.get_page(f'{BASE_URL}Domains')
    items = parser.parse_domains(page=page)
    outp = anki.create_deck(items, outfile=f'./output/Domains.apkg', outname='Domains')