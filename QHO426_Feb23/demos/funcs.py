def triangle(a,h):
    return a+h

def lap(x):
    print(f"This is not {x-5}")
    return x**2

def map(x):
    print(x+2)

def main():
    g = 8
    map(lap(triangle(g,-2)))

main()