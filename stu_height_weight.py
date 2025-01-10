students = {
    "YUGAN": {"height": 160, "weight": 55},
    "MARSH": {"height": 175, "weight": 70},
    "AKASH": {"height": 155, "weight": 45},
    "VICKY": {"height": 180, "weight": 85},
}
min_height = 160
min_weight = 50
filtered_students = {name: data for name, data in students.items() 
                     if data["height"] >= min_height and data["weight"] >= min_weight}
print(filtered_students)
