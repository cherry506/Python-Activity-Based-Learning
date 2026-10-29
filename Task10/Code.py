
courses = [
    ("Python", "09:00", "10:00", "R1"),
    ("Java", "09:30", "10:30", "R2"),
    ("Maths", "10:00", "11:00", "R1")
]

for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        a, b = courses[i], courses[j]
        if a[1] < b[2] and b[1] < a[2]:
            print(a[0], "and", b[0], "conflict")

