class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path 🚲")


vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()
