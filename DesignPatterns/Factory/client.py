
from Factory import Factory
from Bike import Bike
from Car import Car

vehicle = input("enter vehicle type")
print("-->",vehicle)

# client code without factory
if vehicle == "bike":
    Bike().createVehicle("bike")
elif vehicle == "car":
    Car().createVehicle("car")

# client code with factory
Factory.getVehicle(vehicle)

# without a factory the client has to change his code
# or add new code when he has to create new objects
# and needs to recompile his code 
# with factory placed in between the client and the 
# parent and child classes the client has become less coupled
# with the classes and doesnt have to recompile his code
# even if the classes change

# in this case the client is just another file sitting beside your 
# parent and child classes. in realworld the client will be 
# some third party tool or person making use of your library
# if the client has to change his code everytime your code changes
# this will result in breaking changes to the system