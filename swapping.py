a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
print("Before swapping the value a is {} and b is {}".format(a,b))
temp = a
a = b
b = temp
print(f"After swapping the value a is {a} and b is {b}")