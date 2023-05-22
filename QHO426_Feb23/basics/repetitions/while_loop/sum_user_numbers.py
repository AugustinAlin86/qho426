n = int(input("How many numbers should I sum up?"))
i = 1
total = 0
while(i <= n):
    total += int(input(f"Enter number {i} of {n}\t"))
    i += 1
print(f"The total is {total}")