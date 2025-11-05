import csv

with open("sample4.csv", "r", newline="") as f1:
    read = csv.reader(f1)
    count = 0

    for row in read:
        print(row)
        count += 1
