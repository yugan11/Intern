numbers = {
    'a':12,
    'b':15,
    'c':22,
    'd':7,
    'e':30
}
even_num = {key:values for key, values in numbers.items() if values % 2 == 0}
print(even_num)
