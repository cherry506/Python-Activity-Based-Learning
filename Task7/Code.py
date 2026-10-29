
import math

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost: "))
transport = float(input("Transport cost: "))
certificates = float(input("Certificate cost: "))
sponsor = float(input("Sponsorship amount: "))
participants = int(input("Expected participants: "))
contribution = float(input("Contribution per participant: "))

cost = venue + equipment + catering + transport + certificates
collected = participants * contribution
shortfall = max(0, cost - sponsor - collected)

if contribution > 0:
    breakeven = math.ceil(max(0, cost - sponsor) / contribution)
else:
    breakeven = 0 if sponsor >= cost else "Not possible"

print("\nTotal Event Cost:", cost)
print("Participant Contributions:", collected)
print("Sponsorship Shortfall:", shortfall)
print("Break-even Registrations:", breakeven)

