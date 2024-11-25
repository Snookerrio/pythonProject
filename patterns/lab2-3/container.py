from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self, container_id: int, weight: float) -> None:
        self.id = container_id
        self.weight = weight

    @abstractmethod
    def consumption(self) -> float:
        pass

class BasicContainer(Container):
    UNIT_CONSUMPTION = 2.5

    def consumption(self) -> float:
        return self.weight * BasicContainer.UNIT_CONSUMPTION

class HeavyContainer(Container):
    UNIT_CONSUMPTION = 3.0

    def consumption(self) -> float:
        return self.weight * HeavyContainer.UNIT_CONSUMPTION

class RefrigeratedContainer(HeavyContainer):
    UNIT_CONSUMPTION = 5.0

    def consumption(self) -> float:
        return self.weight * RefrigeratedContainer.UNIT_CONSUMPTION

class LiquidContainer(HeavyContainer):
    UNIT_CONSUMPTION = 4.0

    def consumption(self) -> float:
        return self.weight * LiquidContainer.UNIT_CONSUMPTION

