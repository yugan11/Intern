string=input("Enter the string:")
dic = {}
for character in string:

    if character in dic:
        dic[character] += 1
    else:
        dic[character] = 1
print(dic)
