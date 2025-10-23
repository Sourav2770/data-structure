list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

length = len(list1)
list2 = []


for i in range(0, length):
    if list1[i] % 2 != 0:
        list2.append(list1[i])

print(list2)
