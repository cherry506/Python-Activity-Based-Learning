
n = int(input("Enter number of months: "))
bills = []

for i in range(n):
    units = float(input(f"Units for month {i+1}: "))

    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 200 + (units - 100) * 3
    else:
        energy = 500 + (units - 200) * 5

    surcharge = energy * 0.05
    rebate = energy * 0.10 if units <= 100 else 0
    bill = energy + 50 + surcharge - rebate
    bills.append(bill)

    print(f"Month {i+1} Bill: Rs.{bill:.2f}")

print("\nBill Comparison:")
for i in range(1, n):
    increase = (bills[i] - bills[i-1]) / bills[i-1] * 100

    if increase > 20:
        print(f"Month {i+1}: Unusual increase ({increase:.2f}%)")
    else:
        print(f"Month {i+1}: Normal change ({increase:.2f}%)")

