import string
def create_alphabet_file(file_name, letters_per_line):
    alphabet = string.ascii_lowercase
    with open(file_name, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            file.write(alphabet[i:i+letters_per_line] + '\n')
    print(f"File {file_name} created successfully with letters listed by {letters_per_line} letters per line.")
file_name = 'alphabet.txt'  
letters_per_line = 5  
create_alphabet_file(file_name, letters_per_line)
