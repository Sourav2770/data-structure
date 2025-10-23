year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("entered date is leap year")
    else:
        print("entered date is not leap year")

else:
    if year % 4 == 0:
        print("entered date is leap year")
    else:
        print("entered date is not leap year")
