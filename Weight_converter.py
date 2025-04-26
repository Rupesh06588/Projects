weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "K":
    print(f"You are {weight/0.45} pounds")
else:
    print(f"You are {weight*0.45} kilograms")
