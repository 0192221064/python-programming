n=int(input("enter n "))
total_denomination=0
for i in range(1, n+1):
    denomination = int(input(f"Enter the {i} Denomination: "))
    notes = int(input(f"Enter the number of {i} denomination notes: "))
    total_denomination+=denomination*notes
print(total_denomination)
