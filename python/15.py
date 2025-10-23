dict1 = {"a" : 1, "b" : 2, "c" : 1}
dict2 = {"d" : 1, "e" : 2, "f" : 1}

merged = {}


for key in dict1:
    merged[key] = dict1[key]


for key in dict2:
    merged[key] = dict2[key]


print(merged)        
