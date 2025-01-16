input_string = "This is an example string with some words of varying lengths"

words = input_string.split()

long_words = list(filter(lambda x: len(x) >= 4, words))

print("Words with at least 4 characters:", long_words)
