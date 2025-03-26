# Class 1
class BMW():
    def Speed(self):
        print("A BMW Can Go 100 miles per hour")
    def Owner(self):
        print("BMW Is created by The Quandt family")
# Class 2
class Bugatti():
    def Speed(self):
        print("A Bugatti can go 260 miles per hour")
    def Owner(self):
        print("Bugatti is created by Rimac")
obj_BMW = BMW()
obj_Bugatti = Bugatti()

for Car in (obj_BMW,obj_Bugatti):
    Car.Speed()
    Car.Owner()  