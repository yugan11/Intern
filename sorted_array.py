def sorted_array(value1, value2):
    values = [value1, value2]    
    unique_values = set(values)
    sorted_unique_values = sorted(list(unique_values))
    return sorted_unique_values
value1 = 3
value2 = 1
result = sorted_array(value1, value2)
print("Sorted unique array:", result)
