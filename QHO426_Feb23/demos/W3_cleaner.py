def dimensions():
    w = float(input("Enter width of the room: "))
    l = float(input("Enter length of the room: "))
    return l*w

def r_name():
    return input("Enter room name: ")

def price(name, area):
    if name.lower() == "bathroom":
        return area * 20
    elif name.lower() == "bedroom":
        return area * 10
    elif name.lower() == "living room":
        return area * 12
    else:
        return area * 30

def run():
    t_price = 0
    num = int(input("How many rooms to clean? "))
    for i in range(num):
        room = r_name()
        area = dimensions()
        p = price(room, area)
        t_price += p
    print(f"The total price is £{t_price:.2f}")

run()