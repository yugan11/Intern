tuple_of_tuples = (("Red", "White", "Blue"), ("Green", "Pink", "Purple"), ("Orange", "Yellow", "Lime"))
is_white_present = any("White" in tup for tup in tuple_of_tuples)
is_olive_present = any("Olive" in tup for tup in tuple_of_tuples)
print("Check if White present in said tuple of tuples!", is_white_present)
print("Check if Olive present in said tuple of tuples!", is_olive_present)