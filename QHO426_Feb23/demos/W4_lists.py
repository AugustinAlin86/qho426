#Declare empty list
bleh = []
meh = list()
#Declare a non-empty list
yummy = ["Chicken", "Ice Cream", "Chocolate", "Chips"]
#Print entire list
print(yummy)
#Print a single item
print(yummy[-2])
#Print some items
print(yummy[1:3])
#Add elements to our list (expand it) - adding at the end of the list
print(bleh)
bleh.append("Marmite")
bleh.append("Anchioves")
bleh.append("Carrot")
bleh.append("Liver")
bleh.append("Tomato")
print(bleh)
yummy.append("Pierogi")
print(yummy)
#Add multiple items to a list
n = int(input("How many items to add: "))
for i in range(n):
    bleh.append(input("Enter horrible food: "))
print(bleh)
bleh.extend(["Horse Meat", "Pancakes"])
print(bleh)
#Insert items at specific positions on the list
bleh.insert(1, "Cabbage")
print(bleh)
bleh.insert(4, "Onions")
print(bleh)
#Remove item from the list
if "Carrot" in bleh:
    bleh.remove("Carrot")
if "Tato" in bleh:
    bleh.remove("Tato")
print(bleh)
#Remove items by index
x = bleh.pop(5) #Returns that value
print(x)
print(bleh)
#Alternative way of deleting by index
del bleh[7]
print(bleh)
#Check a list for particular data type/traverse the list
lista = ["Fred", 56, True, 99.4, "Potato", True, 82]
sum = 0
for item in lista:
    if isinstance(item, int):
        sum += item
print(sum)
print(type(item))