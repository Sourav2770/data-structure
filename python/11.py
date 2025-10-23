string = input("enter a string :")
arr = list(string)

length = len(arr)


for i in range(0, length-1):
    first = arr[0]
    last = arr[length-1]


arr[0] = last
arr[length-1] = first


str=''.join(arr)

print(str)

    