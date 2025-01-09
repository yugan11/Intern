def myfun(a, b):
    for i in a:
        for j in b:
            if i == j:
                #print(f"The Value {i} and {j} are equal")
                return True
               
            
    return False

list_1 = [2,3,4,5,6]
list_2 = [7,8,9,7,-1]
result = myfun(list_1, list_2)
print(result)
