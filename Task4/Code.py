
n = int(input("Number of passengers: "))
total = 0

for i in range(n):
    age = int(input("Age: "))
    d = float(input("Distance (km): "))
    cls = input("Class (Sleeper/AC): ").lower()
    cancel = input("Cancel? (yes/no): ").lower()

    fare = (d * 1.5 if d <= 100 else
            150 + (d - 100) * 1.2 if d <= 500 else
            630 + (d - 500))

    if cls == "ac":
        fare *= 2
    if age >= 60:
        fare *= 0.5

    fare += 40

    if cancel == "yes":
        penalty = (fare - 40) * 0.25
        print("Penalty:", round(penalty, 2),
              "Refund:", round(fare - penalty, 2))
    else:
        print("Ticket fare:", round(fare, 2))
        total += fare

print("Total active fare:", round(total, 2))

