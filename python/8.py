num = int(input("Enter the number: "))

r = 0
count = 0

if num ==0:
    count = 1
else:
    while num > 0:
        r = num % 10
        count+=1
        num = num//10
        if r == 0:
            break




print(f"Number of digits of the given number is {count}")

