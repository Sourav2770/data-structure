import csv

with open("sample4.csv", "r", newline="") as f1:
    reader = csv.reader(f1)
        

    col_index = 1   
    
    for row in reader:
        print(row[col_index])
