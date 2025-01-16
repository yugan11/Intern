numbers = [19, 26, 39, 52, 13, 15, 38, 91, 130, 182, 260, 75]

divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print("Numbers divisible by 19 or 13:", divisible_by_19_or_13)
