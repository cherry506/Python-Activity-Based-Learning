
b = float(input("Initial balance: "))
n = int(input("Number of transactions: "))
s = r = 0

for _ in range(n):
    t = input("Type (deposit/withdraw): ").lower()
    a = float(input("Amount: "))

    if a <= 0 or t not in ("deposit", "withdraw"):
        r += 1
    elif t == "deposit":
        b += a
        s += 1
    elif a <= b and a <= 10000:
        b -= a
        s += 1
    else:
        print("Rejected")
        r += 1

print("Balance:", b, "\nSuccessful:", s, "\nRejected:", r)

