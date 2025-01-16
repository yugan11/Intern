def find_matches(input_string, string_list):
    matches = [s for s in string_list if input_string.lower() in s.lower()]
    return matches
string_list = ["apple", "banana", "cherry", "pineapple" , "Greenapple"]
input_string = "apple"  
matched_strings = find_matches(input_string, string_list)
print(f"Strings that match '{input_string}':", matched_strings)
    
