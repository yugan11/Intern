import re

def case_insensitive_replace(original_string, old_substring, new_substring):
    # Use re.sub with flags=re.IGNORECASE to perform case-insensitive replacement
    result = re.sub(old_substring, new_substring, original_string, flags=re.IGNORECASE)
    return result
original_string = "Hello world, welcome to the World of Python!"
old_substring = "world"
new_substring = "universe"
result_string = case_insensitive_replace(original_string, old_substring, new_substring)
print("Original String:", original_string)
print("Modified String:", result_string)
