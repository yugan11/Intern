def remove_ith_character(input_string, i):
    if i < 0 or i >= len(input_string):
        return "Index is out of range."    
    new_string = input_string[:i] + input_string[i+1:]
    return new_string
input_string = "Hello, world!"
i = 7  
result = remove_ith_character(input_string, i)
print("Original String:", input_string)
print("Modified String:", result)
