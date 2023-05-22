#Definition of a ne function - specifying what the procedure is, what it does and how
# so that it can be used later (potentially multiple times)

#Parameter - data given/injected into the function
#Default parameters - assumed if nothing is provided as argument

#Return Values - data extracted from a function into the space where funciton was called

x=7
def t_area(base = 1, height = 2):
    area = height*base*0.5
    area += x
    return area


x = t_area()
y = t_area(10,7) # Call to the function with arguments
z = t_area(18)
a = t_area(height=8)
print("The total area of those triangles is {}".format(x+y+z+a))
print(t_area(10,10))