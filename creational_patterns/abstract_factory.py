from abc import ABC, abstractmethod


# Abstract Factory for doors and their fittings
class AbstractDoorFactory(ABC):
    @abstractmethod
    def create_door(self):
        pass

    @abstractmethod
    def create_door_frame(self):
        pass

    @abstractmethod
    def get_fitting_experts(self):
        pass


# Concrete Factory for Wooden Doors
class WoodenDoorFactory(AbstractDoorFactory):
    def create_door(self):
        return WoodenDoor()

    def create_door_frame(self):
        return WoodenDoorFrame()

    def get_fitting_experts(self):
        return Carpenter()


# Concrete Factory for Steel Doors
class SteelDoorFactory(AbstractDoorFactory):
    def create_door(self):
        return SteelDoor()

    def create_door_frame(self):
        return SteelDoorFrame()

    def get_fitting_experts(self):
        return Welder()


# Abstract Product for doors
class Door(ABC):
    @abstractmethod
    def fit_door(self):
        pass


# Concrete Product - Wooden Door
class WoodenDoor(Door):
    def fit_door(self):
        print("Carpenter is needed to fit a Wooden Door")


# Concrete Product - Steel Door
class SteelDoor(Door):
    def fit_door(self):
        print("Welder is needed to fit a Steel Door")


# Abstract Product for door frames
class DoorFrame(ABC):
    @abstractmethod
    def get_frame(self):
        pass


# Concrete Product - Wooden Door Frame
class WoodenDoorFrame(DoorFrame):
    def get_frame(self):
        print("We have the frame for Wooden Door")


# Concrete Product - Steel Door Frame
class SteelDoorFrame(DoorFrame):
    def get_frame(self):
        print("We have the frame for Steel Door")


# Abstract Product for fitting experts
class FittingExpert(ABC):
    @abstractmethod
    def describe(self):
        pass


# Concrete Product - Carpenter (Fits Wooden Doors)
class Carpenter(FittingExpert):
    def describe(self):
        print("I'm a carpenter! I fit wooden doors")


# Concrete Product - Welder (Fits Steel Doors)
class Welder(FittingExpert):
    def describe(self):
        print("I'm a welder! I fit steel doors")


# Client code to use the factories
def client_code(factory: AbstractDoorFactory):
    door = factory.create_door()
    door_frame = factory.create_door_frame()
    expert = factory.get_fitting_experts()

    door.fit_door()
    door_frame.get_frame()
    expert.describe()


if __name__ == "__main__":
    print("Lets try with wooden factory")
    client_code(WoodenDoorFactory())
    print("Lets try with steel factory")
    client_code(SteelDoorFactory())



