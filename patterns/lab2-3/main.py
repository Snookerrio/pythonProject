import json
from port import Port
from ship import LightWeightShipFactory, MediumShipFactory, HeavyShipFactory
from container import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer


def load_data_from_json(file_path: str):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def main():
    # Завантаження даних з JSON
    data = load_data_from_json("input.json")

    # Створення портів
    ports = {}
    for port_data in data:
        if port_data["action"] == "create_port":
            port_id = port_data["id"]
            coordinates = (port_data["latitude"], port_data["longitude"])
            ports[port_id] = Port(port_id, coordinates)

    # Створення фабрик для кораблів
    lightweight_factory = LightWeightShipFactory()
    medium_factory = MediumShipFactory()
    heavy_factory = HeavyShipFactory()

    ships = {}
    for ship_data in data:
        if ship_data["action"] == "create_ship":
            ship_id = ship_data["id"]
            port_id = ship_data["port_id"]
            port = ports[port_id]
            max_weight = ship_data["max_weight"]
            max_containers = ship_data["max_containers"]
            fuel_consumption = ship_data["fuel_consumption"]

            if max_containers <= 20:
                ship = lightweight_factory.create_ship(ship_id, port)
            elif max_containers <= 40:
                ship = medium_factory.create_ship(ship_id, port)
            else:
                ship = heavy_factory.create_ship(ship_id, port)

            ships[ship_id] = ship

    # Створення контейнерів та додавання їх на кораблі
    for item_data in data:
        if item_data["action"] == "create_container":
            container_id = item_data["id"]
            weight = item_data["weight"]
            container_type = item_data["type"]

            if container_type == "B":
                container = BasicContainer(container_id, weight)
            elif container_type == "H":
                container = HeavyContainer(container_id, weight)
            elif container_type == "R":
                container = RefrigeratedContainer(container_id, weight)
            elif container_type == "L":
                container = LiquidContainer(container_id, weight)
            else:
                continue  # Ігнорувати невідомий тип контейнера

            # Завантажуємо контейнер у перший доступний корабель
            for ship in ships.values():
                if ship.load(container):
                    print(f"Контейнер {container_id} завантажено на корабель {ship.id}.")
                    break

    # Обробка дій
    for action_data in data:
        if action_data["action"] == "load_container":
            ship_id = action_data["ship_id"]
            container_id = action_data["container_id"]
            ship = ships[ship_id]
            container = next((c for c in ship.containers if c.id == container_id), None)
            if container:
                ship.load(container)

        elif action_data["action"] == "sail_to":
            ship_id = action_data["ship_id"]
            port_id = action_data["port_id"]
            ship = ships[ship_id]
            destination_port = ports[port_id]
            if ship.sail_to(destination_port):
                print(f"Корабель {ship_id} відплив до порту {port_id}.")
            else:
                print(f"Корабель {ship_id} не зміг відплисти до порту {port_id}.")

        elif action_data["action"] == "refuel":
            ship_id = action_data["ship_id"]
            fuel = action_data["fuel"]
            ship = ships[ship_id]
            ship.refuel(fuel)
            print(f"Корабель {ship_id} заправлений на {fuel} одиниць пального.")


if __name__ == "__main__":
    main()



