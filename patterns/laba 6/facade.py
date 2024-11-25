from singleton import SettingsManager

class LightingSystem:
    def turnOnLights(self):
        print("Lights turned on.")

    def turnOffLights(self):
        print("Lights turned off.")

    def setBrightness(self, level):
        print(f"Brightness set to {level}.")

class SecuritySystem:
    def armSystem(self):
        print("Security system armed.")

    def disarmSystem(self):
        print("Security system disarmed.")

    def triggerAlarm(self):
        print("Alarm triggered!")

class ClimateControlSystem:
    def setTemperature(self, targetTemp):
        print(f"Temperature set to {targetTemp}°C.")

    def turnOnHeater(self):
        print("Heater turned on.")

    def turnOnAC(self):
        print("Air conditioning turned on.")

class SmartHomeFacade:
    """Фасад для управління системами розумного дому."""
    def __init__(self):
        self.lighting = LightingSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControlSystem()
        self.settings = SettingsManager()

    def controlLighting(self, on):
        if on:
            self.lighting.turnOnLights()
        else:
            self.lighting.turnOffLights()

    def activateSecuritySystem(self):
        self.security.armSystem()

    def setClimateControl(self, targetTemp):
        self.climate.setTemperature(targetTemp)
        self.settings.settings["preferred_temperature"] = targetTemp