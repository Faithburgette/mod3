'''
Faith Burgette 
SDEV 220
Vehicle Data
'''

#creating super class
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
    
    def describe(self):
        return f"Vehicle Type : {self.vehicleType}"

#creating car subclass
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('Car')
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def describe(self):
        return f"""        Vehicle Type : Car
        Year : {self.year}
        Make : {self.make}
        Model : {self.model}
        Number of Doors : {self.doors}
        Type of Roof : {self.roof}"""

#creating 2nd example class
class Boat(Vehicle):
    def __init__(self, boatType, sleepCount, boatName):
        super().__init__('Boat')
        self.boatType = boatType
        self.sleepCount = sleepCount
        self.boatName = boatName

    def describe(self):
        return f"""        Vehicle Type : Boat
        Type of Boat : {self.boatType}
        Sleep Count : {self.sleepCount}
        Boat Name : {self.boatName}"""

#executing program
try:
    userVehi = input("Enter the type of vehicle : ")
    
    #receive user input for car
    if userVehi.upper() == 'CAR':
        year = input("Enter the year of the car : ")
        make = input("Enter the make of the car : ")
        model = input("Enter the model of the car : ")
        doors = input("Enter whether the car has 2 or 4 doors : ")
        roof = input("Enter whether the car has a sun roof or not : ")

        car = Automobile(year, make, model, doors, roof)

        print(car.describe())
#recieve user input for boat 
    elif userVehi.upper() == 'BOAT':
        boatType = input('Enter the type of boat : ')
        sleepCount = input('How many people does the boat sleep : ')
        boatName = input("What is the boats name : ")

        boat = Boat(boatType, sleepCount, boatName)

        print(boat.describe())
#give an default statement 
    else:
        print('Not accesible at this time.')
        
except ValueError:
    print('An error has occured.')
