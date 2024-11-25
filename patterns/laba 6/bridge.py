class Appliance:
    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

class WashingMachine(Appliance):
    def start(self):
        print("Washing machine started.")

    def stop(self):
        print("Washing machine stopped.")

class Refrigerator(Appliance):
    def start(self):
        print("Refrigerator cooling started.")

    def stop(self):
        print("Refrigerator stopped cooling.")

class Switch:
    def __init__(self, appliance):
        self.appliance = appliance

    def turn_on(self):
        self.appliance.start()

    def turn_off(self):
        self.appliance.stop()