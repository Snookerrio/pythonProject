from abc import ABC, abstractmethod
from port import IPort

# Базовий клас Ship
class Ship(ABC):
    def __init__(self, ship_id: int, port: IPort, max_weight: int, max_containers: int, fuel_consumption: float, fuel_limit: float) -> None:
        self.id = ship_id
        self.port = port
        self.max_weight = max_weight
        self.max_containers = max_containers
        self.fuel_consumption = fuel_consumption
        self.fuel_limit = fuel_limit
        self.fuel = 0
        self.containers = []

    def sail_to(self, destination: IPort) -> bool:
        distance = self.port.get_distance(destination)
        required_fuel = distance * self.fuel_consumption

        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            self.port.outgoing_ship(self)
            destination.incoming_ship(self)
            self.port = destination
            return True
        return False

    def refuel(self, fuel: float) -> None:
        if self.fuel + fuel <= self.fuel_limit:
            self.fuel += fuel
        else:
            print("Cannot refuel beyond fuel limit.")

    def load(self, container) -> bool:
        if len(self.containers) < self.max_containers and container.weight <= self.max_weight:
            self.containers.append(container)
            return True
        return False

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            self.port.add_container(container)
            return True
        return False

    def __repr__(self):
        return f"Ship(ID: {self.id}, Port: {self.port.id}, Fuel: {self.fuel}/{self.fuel_limit}, Containers: {len(self.containers)})"

class LightWeightShip(Ship):
    def __init__(self, ship_id: int, port: IPort) -> None:
        super().__init__(ship_id, port, 10000, 20, 1.0, 500.0)

class MediumShip(Ship):
    def __init__(self, ship_id: int, port: IPort) -> None:
        super().__init__(ship_id, port, 20000, 40, 1.5, 1000.0)

class HeavyShip(Ship):
    def __init__(self, ship_id: int, port: IPort) -> None:
        super().__init__(ship_id, port, 50000, 100, 2.5, 2000.0)

                                          #фабрика
class ShipFactory(ABC):
    @abstractmethod
    def create_ship(self, ship_id: int, port: IPort) -> Ship:
        pass

class LightWeightShipFactory(ShipFactory):
    def create_ship(self, ship_id: int, port: IPort) -> LightWeightShip:
        return LightWeightShip(ship_id, port)

class MediumShipFactory(ShipFactory):
    def create_ship(self, ship_id: int, port: IPort) -> MediumShip:
        return MediumShip(ship_id, port)

class HeavyShipFactory(ShipFactory):
    def create_ship(self, ship_id: int, port: IPort) -> HeavyShip:
        return HeavyShip(ship_id, port)


