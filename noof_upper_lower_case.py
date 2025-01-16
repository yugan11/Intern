def letters(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
input_string = "Hello World!"
upper, lower = letters(input_string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
