list_0 = [(2, 5),(1, 2),(4, 4),(2, 3),(2, 1)] 
def last_num(num):
    return num[1]
sorted_list=sorted(list_0, key=last_num)
print(f"the sorted list is {sorted_list}")