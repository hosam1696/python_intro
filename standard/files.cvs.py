# dealing with comma separated values (CSV)
import csv
csv_file = open('one.csv', 'r')
c1 = csv.reader(csv_file)

print(csv_file.readlines(), list(c1))

for line in list(c1):
    for col in line:
        print(col.ljust(12))

# write a csv file

csv.writer(csv_file)