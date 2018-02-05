import csv
from collections import Counter


with open('Speed Dating Data.csv', 'rU') as file:
    csvReader = csv.reader(file)
    header = csvReader.next()
    data = [row for row in csvReader]


for colnum, colname in enumerate(header):
    print colname
    print Counter([row[colnum] for row in data]).most_common(3)
    print ""
