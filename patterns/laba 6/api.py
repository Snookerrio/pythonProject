from fastapi import FastAPI
from facade import SmartHomeFacade
from singleton import SettingsManager, EnergyManager

app = FastAPI()

facade = SmartHomeFacade()
settings = SettingsManager()
energy_manager = EnergyManager()

@app.get("/")
def home():
    return {"message": "Welcome to Smart Home API"}

@app.post("/lighting/on")
def turn_on_lights():
    facade.controlLighting(on=True)
    return {"status": "Lights turned on"}

@app.post("/lighting/off")
def turn_off_lights():
    facade.controlLighting(on=False)
    return {"status": "Lights turned off"}

@app.post("/security/activate")
def activate_security():
    facade.activateSecuritySystem()
    return {"status": "Security system activated"}

@app.post("/climate/set-temperature")
def set_temperature(target: float):
    facade.setClimateControl(target)
    return {"status": f"Temperature set to {target}°C"}

@app.get("/settings")
def get_settings():
    return {"settings": settings.settings}

@app.post("/settings/update")
def update_settings(key: str, value: str):
    settings.settings[key] = value
    return {"status": "Settings updated", "settings": settings.settings}

@app.post("/energy/monitor")
def monitor_energy():
    energy_manager.monitorUsage()
    return {"status": "Energy usage monitored"}

@app.post("/energy/optimize")
def optimize_energy():
    energy_manager.optimizeEnergy()
    return {"status": "Energy usage optimized"}