from modules import speed_limit
traffic_light='Green'
class Vehicle:
    def start_engine(self):
        message='Engine started'
        print(message)
class Car(Vehicle):
    def __init__(self,brand):
        self.brand=brand
        print("Car brand is :",self.brand)
    def start_engine(self):
        super().start_engine()
        message='Car engine started'
        print(message)
class Bike(Vehicle):
    def __init__(self,type):
        self.type=type
        print("Bike type is :",self.type)
    def start_engine(self):
        super().start_engine()
        message='Bike engine started'
        print(message)
print("-----------Car--------------")
c=Car("Honda")
c.start_engine()
print("Traffic light color is :",traffic_light)
print("Speed limit is:",speed_limit)
print("-----------Bike--------------")
b=Bike("Sports")
b.start_engine()
print("Traffic light color is :",traffic_light)
print("Speed limit is:",speed_limit)

