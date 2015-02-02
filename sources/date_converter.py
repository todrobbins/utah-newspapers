import csv
import datetime

def convert_date(date):
    new_date = datetime.datetime.strptime(date, "%b %Y")
    return "{}-{:02}".format(new_date.year, new_date.month)

new_rows = []

with open('utah-newspapers.csv', 'rb') as f:
    reader = csv.reader(f)

    rownum = 0
    for row in reader:
        if rownum > 0:
            print row
            row[3] = convert_date(row[3])
            row[4] = convert_date(row[4])
            new_rows.append(row)

        rownum += 1

print new_rows