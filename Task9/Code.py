
vehicle = input("Enter vehicle type (Car/Bike): ").lower()
hours = int(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid parking hours")
elif vehicle == "car":
    fee = hours * 30
    print("Parking Fee: ₹", fee)
elif vehicle == "bike":
    fee = hours * 15
    print("Parking Fee: ₹", fee)
else:
    print("Invalid vehicle type")

