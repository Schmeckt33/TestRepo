import csv

data = open(sys.argv[1])

for row in csv.reader(data)
    print(row)
