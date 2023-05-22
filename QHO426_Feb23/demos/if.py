temp = float(input("Enter your body temperature: "))

if temp > 38:
    print("You have a fever. Poor you!")
elif temp < 36:
    print("You have low temperature. Seek help.")
elif temp == 37:
    print("You have standard body temperature. Boring.")
else:
    print("You either typed in wrong value or you have no fever")
print("Your temperature is {}C".format(temp))
#Indentation specifies the code block - colection of related statements in Python
