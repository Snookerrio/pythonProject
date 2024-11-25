class SingletonMeta(type):
    """Метаклас для реалізації синглтону."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SettingsManager(metaclass=SingletonMeta):
    """Менеджер налаштувань розумного дому."""
    def __init__(self):
        self.settings = {
            "preferred_temperature": 22,
            "lighting_mode": "normal"
        }

class EnergyManager(metaclass=SingletonMeta):
    """Менеджер енергоспоживання."""
    def monitorUsage(self):
        print("Monitoring energy usage...")

    def optimizeEnergy(self):
        print("Optimizing energy usage...")