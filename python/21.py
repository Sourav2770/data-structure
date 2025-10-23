str1 = input("Enter a string: ")

str2 = "ing"
str3 = "ly"

if str2 in str1:
    new_str = str1[:-3]
    resultString = new_str + "ly"
else:
    new_str = str1[:-1]
    resultString = str1[:-1] + str2



print(resultString)        
