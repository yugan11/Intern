words = ["Python", "Perm", "Java", "C++", "PHP", "Ruby", "Pineapple"]
words_starting_with_p = list(filter(lambda x: x[0].upper() == 'P', words))
if len(words_starting_with_p) >= 2:
    
    print("Yes, there are at least two words that start with 'P'.")
    
else:
    
    print("No, there are less than two words that start with 'P'.")
print("Words starting with 'P':", words_starting_with_p)
