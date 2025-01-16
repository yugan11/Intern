words = ["apple", "banana", "cherry", "orange", "kiwi", "grape", "melon", "mango"]
length_six_words = list(filter(lambda x: len(x) == 6, words))

print("Words with length 6:", length_six_words)
