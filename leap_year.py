year = int(input("Enter the Year You want to check :"))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("IT is leap year!")
        else:
            print("IT is not leap year!")
    else:
        print("IT is leap year!")
else:
    print("IT is not leap year!")