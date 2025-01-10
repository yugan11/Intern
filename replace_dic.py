letter_count = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
total_sum = sum(letter_count.values())

for key in letter_count:
    letter_count[key] = total_sum
print(letter_count)
