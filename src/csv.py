import csv

class CSV:
    def __init__(self) -> None:
        pass

    def write_csv(self, parsed: list, outfile: str) -> any:
        with open(outfile, mode='w', newline='', encoding='utf-8') as ofile:
            writer = csv.writer(ofile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerows(parsed)

            return outfile