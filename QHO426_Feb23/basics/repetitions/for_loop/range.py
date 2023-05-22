level = int(input("What level of brightness do you require?  "))
for i in range(2, level+1, 2):
    print("Beep's brightness level: ", "*" * i)
    print("Bop's brightness level: ", "*" * i)
    print()
print("Adjustment complete")