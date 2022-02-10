import csv

with open('data2.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)
