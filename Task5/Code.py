
material = float(input("Material cost: "))
labour = float(input("Labour cost: "))
machine = float(input("Machine cost: "))
waste = float(input("Wastage percentage: "))
qty = int(input("Quantity produced: "))
price = float(input("Selling price per unit: "))
target = float(input("Profit target: "))

wastage = material * waste / 100
cost = material + labour + machine + wastage
revenue = qty * price
profit = revenue - cost

print("Total Cost:", cost)
print("Revenue:", revenue)
print("Profit:", profit)
print("Status:", "Target Achieved" if profit >= target
      else "Target Not Achieved")

