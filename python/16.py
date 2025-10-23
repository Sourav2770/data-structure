a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

def expression(x, y):
    while y != 0:
        x, y = y, x % y  
    return x  


if a > b:
    print(f"The GCD of {a} and {b} is {expression(a, b)}")
else:
    print(f"The GCD of {a} and {b} is {expression(b, a)}")
