#Declare a tuple
x = ("Piotr", 68, True)
y = tuple(["Garry", 32, False])
#Print tuples
print(x)
print(y)
print(x[1])
#Cannot change individual items
#x[1] = 69

#Concatenate Tuples
z = x + y
print(z)
print(y)
print(x)
#Using min and max functions
h = (74, 68, 45, 35, 15, 1, 82)
print(max(h))

lista = list(h)
temp = lista[0]
lista[0] = lista[1]
lista[1] = temp
h1 = tuple(lista)
print(h1)
del h1