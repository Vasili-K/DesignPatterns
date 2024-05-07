from abc import ABC, abstractmethod


# Abstract Creator class
class DoorFactory(ABC):
    @abstractmethod
    def create_door(self):
        pass


# Specific door factories
class WoodenDoorFactory(DoorFactory):
    def create_door(self):
        return WoodenDoor()


class SteelDoorFactory(DoorFactory):
    def create_door(self):
        return SteelDoor()


# Product interface
class Door(ABC):
    @abstractmethod
    def open_door(self):
        pass


# Specific products
class WoodenDoor(Door):
    def open_door(self):
        print("The Wooden Door is open")


class SteelDoor(Door):
    def open_door(self):
        print("The Steel Door is open")


def client_code(door_factory: DoorFactory):
    # Creation of an object depends on the factory
    door = door_factory.create_door()
    door.open_door()


if __name__ == "__main__":
    wooden_door_factory = WoodenDoorFactory()
    client_code(wooden_door_factory)

    steel_door_factory = SteelDoorFactory()
    client_code(steel_door_factory)


