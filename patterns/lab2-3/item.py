from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, item_id: int, weight: float, count: int, container_id: int) -> None:
        self.id = item_id
        self.weight = weight
        self.count = count
        self.container_id = container_id

    @abstractmethod
    def get_total_weight(self) -> float:
        pass

class SmallItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count

class HeavyItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count

class RefrigeratedItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count

class LiquidItem(Item):
    def get_total_weight(self) -> float:
        return self.weight * self.count

class ItemFactory:
    @staticmethod
    def create_item(item_type: str, item_id: int, weight: float, count: int, container_id: int) -> Item:
        if item_type == "Small":
            return SmallItem(item_id, weight, count, container_id)
        elif item_type == "Heavy":
            return HeavyItem(item_id, weight, count, container_id)
        elif item_type == "Refrigerated":
            return RefrigeratedItem(item_id, weight, count, container_id)
        elif item_type == "Liquid":
            return LiquidItem(item_id, weight, count, container_id)
        else:
            raise ValueError("Unknown item type")