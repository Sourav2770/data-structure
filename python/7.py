n = int(input("Enter the  number to find factorial : "))

fact = 1
for i in range (1,n+1):
    fact=fact*i

print(f"factorial of the entered number is {fact}")