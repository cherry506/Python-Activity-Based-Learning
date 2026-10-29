
name = input("Patient name: ")
consult = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))

if min(consult, diagnostic, treatment) < 0:
    print("Invalid charges!")
else:
    total = consult + diagnostic + treatment
    concession = total * 0.10 if total >= 5000 else 0
    final_bill = total - concession

    if final_bill < 2000:
        category = "Low Bill"
    elif final_bill <= 10000:
        category = "Medium Bill"
    else:
        category = "High Bill"

    print("\n--- Hospital Bill ---")
    print("Patient:", name)
    print("Total Bill: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)
    print("Classification:", category)

