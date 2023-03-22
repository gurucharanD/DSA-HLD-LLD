from abc import abstractmethod


class Vehicle:
    def __init__(self) -> None:
        # self.name = name
        pass
    
    @abstractmethod
    def createVehicle(self):
        pass

    