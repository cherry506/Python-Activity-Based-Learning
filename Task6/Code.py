
n = int(input("Number of subjects: "))
marks = list(map(int, input("Enter marks: ").split()))

if len(marks) != n or any(m < 0 or m > 100 for m in marks):
    print("Invalid marks")
else:
    marks = [min(100, m + (35-m if 0 < 35-m <= 5 else 0))
             for m in marks]
    p = sum(marks) / n

    if min(marks) < 35:
        result = "Fail"
    elif p >= 75:
        result = "Distinction"
    elif p >= 60:
        result = "First Class"
    elif p >= 50:
        result = "Second Class"
    else:
        result = "Pass"

    print("Final Marks:", marks)
    print("Percentage:", round(p, 2), "%")
    print("Result:", result)

