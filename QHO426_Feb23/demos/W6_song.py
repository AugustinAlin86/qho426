#Open file for reading
f = open("song.txt")
#Print single line
# print(f.readline(), end="")
# print(f.readline(), end="")
# #Print full content of the file
# print(f.read())
#Grab content of txt file and savbe it as a list
lista = f.readlines()
print(lista)
print(lista[2])
f.close()
g = open("song.txt", "a")
g.write("\nAnd it's everlasting, infinite\n")
g.writelines(["It goes on and on, you can't measure it\n", "Can't quench your love\n"])
g.close()

