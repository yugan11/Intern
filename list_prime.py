list = [2,3,4,5,7]

for i in list:
    flag = False
    if i == 0 or i == 1:
        print("False")
        break
    
    elif i > 1:
        
        for j in range(2, i):
            if (i % j) == 0:
                # if factor is found, set flag to True
                flag = True
                
                # break out of loop
                break
        if flag:
            print("prime")
        else:
            print("not a prime")


