my_dict = {"a":7, "b": 2,"c": 9,"d": 1,"e": 4,"f": 8}

dict_items = list(my_dict.items())



for i in range(len(dict_items)):

    for j in range(0,len(dict_items) - i - 1):
        if dict_items[j][1] < dict_items[j+1][1]:
            temp = dict_items[j]
            dict_items[j] = dict_items[j+1]
            dict_items[j+1]=temp




sorted_dict = dict(dict_items)

print(sorted_dict)







        






