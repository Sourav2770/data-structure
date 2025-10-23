str1 = input("Ënter string 1: ")
str2 = input("Enter string 2: ")

arr1 = list(str1)
arr2 = list(str2)

len1 = len(arr1)
len2 = len(arr2)



temp = arr1[0]
arr1[0] = arr2[0]
arr2[0] = temp


resString = ''.join(arr1) + " " + ''.join(arr2)

print(resString)

    



