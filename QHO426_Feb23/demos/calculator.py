print("Provide 2 numbers: ")
n1 = float(input())
n2 = float(input())
print(f"{n1:.7f} + {n2:.0f} = {n1+n2}") #f-string approach
print("{} - {} = {}".format(n1,n2, n1-n2)) #format method
print(str(n1) + " x " + str(n2) + " = " + str(n1*n2)) #String concatenation (combine)
print(str(n1), "/", str(n2), "=", str(n1/n2) ) #Comma separated
print(f"{n1}^{n2} = {n1**n2}")
print(f"{n1} % {n2} = {n1%n2}") # Modulo operator -> calculating remainder of division