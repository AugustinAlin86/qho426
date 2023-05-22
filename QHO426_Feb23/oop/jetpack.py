from tech import Tech

class Jetpack(Tech):

    def __init__(self):
        pass

    def __str__(self):
        return "This is a JetPack, let's fly!"

    def __repr__(self):
        return "Jetpack()"

    def activate(self):
        print("Jetpack started")

    def deactivate(self):
        print("Jetpack is off (hopefully not mid-air)")

    def fly(self,speed):
        print(f"Jetpack flies at {speed}m/s")

if __name__ == "__main__":
    jetp = Jetpack()
    jetp.activate()
    jetp.fly(20)
    jetp.fly(41)
    jetp.deactivate()