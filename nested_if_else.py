height = int(input("Enter your height :"))
if height >= 3:
    print("Can ride!")
    age = int(input("What is your age:"))
    if age < 12:
        print("Please pay 150")
    elif age <=18:
        print("Please pay 250")
    else:
        print("Please pay 500")
else:
    print("Cannot ride!")
print("BYE")