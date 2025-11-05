with open("input.txt", "r") as infile:
    lines = infile.readlines()

with open("output.txt", "w") as outfile:
    outfile.writelines(lines[::2])  
