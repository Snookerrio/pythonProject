from abc import ABC, abstractmethod


class IPort(ABC):
    @abstractmethod
    def get_distance(self, other: 'IPort') -> float:
        pass

    @abstractmethod
    def incoming_ship(self, ship) -> None:
        pass

    @abstractmethod
    def outgoing_ship(self, ship) -> None:
        pass

    @abstractmethod
    def add_container(self, container) -> None:
        pass


class Port(IPort):
    def __init__(self, port_id: int, coordinates: tuple) -> None:
        self.id = port_id
        self.latitude, self.longitude = coordinates
        self.containers = []

    def get_distance(self, other: 'IPort') -> float:
        return ((self.latitude - other.latitude) ** 2 + (self.longitude - other.longitude) ** 2) ** 0.5

    def incoming_ship(self, ship) -> None:
        print(f"Корабель {ship.id} прибув до порту {self.id}.")

    def outgoing_ship(self, ship) -> None:
        print(f"Корабель {ship.id} покинув до порту {self.id}.")

    def add_container(self, container) -> None:
        self.containers.append(container)
        print(f"Container {container.id} added to port {self.id}.")
