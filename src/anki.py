import genanki
import random

class Anki:
    def __init__(self) -> None:
        self.model = genanki.Model(
            random.randint(1, 100000000),
            'Card Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '<p>{{Question}}</p>',
                    'afmt': '{{FrontSide}}<hr id="answer"><p>{{Answer}}</p>',
                },
            ],
            css="""
                    .card {
                        font-family: arial;
                        font-size: 24px;
                        text-align: center;
                        color: black;
                        background-color: white;
                    }
                """
        )
        self.BASE_NAME = 'GeoHints '

    def gen_note(self, item: list) -> any:
        return genanki.Note(
            model=self.model,
            fields=item)

    def create_deck(self, parsed: list, outfile: str, outname: str) -> any:
        deck = genanki.Deck(
            random.randint(1, 100000000),
            f'{self.BASE_NAME}{outname}',
        )

        for i in parsed:
            deck.add_note(self.gen_note(i))

        genanki.Package(deck).write_to_file(outfile)

        return outfile