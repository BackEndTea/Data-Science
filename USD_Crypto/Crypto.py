import csv


class Currency:

    def __init__(self, fileName):
        with open(fileName, 'rb') as crypto:
            csv_reader = csv.reader(crypto)
            self.header = csv_reader.next()
            self.data = [row for row in csv_reader]

        pass
