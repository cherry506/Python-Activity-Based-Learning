
n = int(input("Number of students: "))
eligible = []
ineligible = []

for _ in range(n):
    name = input("Name: ")
    marks = float(input("Aggregate marks: "))
    subjects = list(map(float, input("Subject marks: ").split()))
    attendance = float(input("Attendance (%): "))
    income = float(input("Family income: "))

    if marks >= 75 and min(subjects) >= 60 and attendance >= 75 and income <= 250000:
        eligible.append((name, marks, attendance, income))
    else:
        ineligible.append(name)

eligible.sort(key=lambda s: (-s[1], -s[2], s[3], s[0].lower()))

print("\nScholarship Rank List:")
for rank, s in enumerate(eligible, 1):
    print(rank, s[0], "Marks:", s[1], "Attendance:", s[2])

print("\nIneligible Students:", ineligible)



