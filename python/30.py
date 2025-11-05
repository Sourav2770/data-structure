import csv

data = [
    {"Name": "Alice", "Age": 25, "Country": "USA"},
    {"Name": "Bob", "Age": 30, "Country": "Canada"},
    {"Name": "Charlie", "Age": 35, "Country": "UK"}
]

filename = "output.csv"

fieldnames = ["Name", "Age", "Country"]

with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()  
    writer.writerows(data)
print("Data written to", filename)



with open("output.csv", "r", newline="") as f1:
    read = csv.reader(f1)
    count = 0

    for row in read:
        print(row)
        count += 1

