from abc import abstractmethod
from Bike import Bike
from Car import Car


class Factory:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def getVehicle(name: str):

        if name == "bike":
            Bike().createVehicle("bike")
        elif name == "car":
            Car().createVehicle("car")
