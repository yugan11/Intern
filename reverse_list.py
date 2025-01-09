def reverse_list(my_list, index):
    if index < 0 or index >= len(my_list):
        print("Invalid index!")
        return my_list
    my_list[index:] = my_list[index:][::-1]
    return my_list
my_list = [1, 2, 3, 4, 5, 6, 7]
index = 3
result = reverse_list(my_list, index)
print("List after reversing from index", index, ":", result)
