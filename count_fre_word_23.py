def count_word_frequency(filename):
    with open(filename, 'r') as file:
        content = file.read()
        content = content.lower()
        words = content.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count
