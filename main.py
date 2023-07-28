from src import *

if __name__ == '__main__':
    scraper = Scraper()
    parser = Parser()
    csv = CSV()
    anki = Anki()

    BASE_URL = 'https://geohints.com/'

    use_pages = ['Poles', 'Bollards', 'Flags', 'Trees', 'PostBoxes', 'Rifts', 'Scenery', 'Sidewalks', 'Stop', 'Street', 'Yield', 'Posts', 'Chevrons', 'Direction', 'Pedestrian', 'RoadNumbering', 'TrafficLights']
    use_text = ['Domains', 'PhoneNumbers']

    # for p in use_pages:
    #     page = scraper.get_page(f'{BASE_URL}{p}')
    #     items = parser.parse_default(page=page)
    #     outp = anki.create_deck(items, outfile=f'./output/{p}.apkg', outname=p)
    # for p in use_text:
    #     page = scraper.get_page(f'{BASE_URL}{p}')
    #     items = parser.parse_text(page=page)
    #     outp = anki.create_deck(items, outfile=f'./output/{p}.apkg', outname=p)

    # countries = ['Columbia', 'Ecuador', 'Peru', 'Bolivia', 'Chile', 'Argentina', 'Uruguay', 'Brazil', 'Paraguay']
    # countries = ['Russia', 'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Poland', 'Ukraine', 'Romania', 'Netherlands', 'Belgium', 'Sweden', 'Czech Republic', 'Greece', 'Portugal', 'Hungary', 'Belarus', 'Austria', 'Switzerland', 'Serbia', 'Bulgaria', 'Denmark', 'Slovakia', 'Finland', 'Norway', 'Ireland', 'Croatia', 'Moldova', 'Bosnia and Herzegovina', 'Albania', 'Lithuania', 'Slovenia', 'North Macedonia', 'Latvia', 'Estonia', 'Luxembourg', 'Montenegro', 'Malta', 'Iceland', 'Andorra', 'Liechtenstein', 'Monaco', 'San Marino', 'Holy See']
    countries = ['India', 'China', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam', 'Iran', 'Turkey', 'Thailand', 'Myanmar', 'South Korea', 'Iraq', 'Afganistan', 'Saudi Arabia', 'Uzbekistan', 'Yemen', 'Malaysia', 'Nepal', 'North Korea', 'Syria', 'Sri Lanka', 'Kazakhstan', 'Cambodia', 'Jordan', 'Azerbaijan', 'Tajikistan', 'United Arab Emirates', 'Israel', 'Laos', 'Kyrgystan', 'Turkmenistan', 'Singapore', 'State of Palestine', 'Lebanon', 'Oman', 'Kuwait', 'Georgia', 'Mongolia', 'Armenia', 'Qatar', 'Bahrain', 'Timor-Leste', 'Cyprus', 'Bhutan', 'Maldives', 'Brunei', 'Taiwan']

    all_items = []

    for p in use_pages:
        page = scraper.get_page(f'{BASE_URL}{p}')
        all_items.extend(parser.parse_default(page=page))
    for p in use_text:
        page = scraper.get_page(f'{BASE_URL}{p}')
        all_items.extend(parser.parse_text(page=page))
    
    filtered_items = [x for x in all_items if x[1].split(' ')[0] in countries]
    
    outp = anki.create_deck(filtered_items, outfile=f'./output/Asia.apkg', outname='Asia')