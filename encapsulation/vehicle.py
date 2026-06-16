class Vehicle:
    def __init__(self,type):
        self.type = type
    def start_engine(self):
        return f"The {self.type}'s engine has started."

    def stop_engine(self):
        return f"The {self.type}'s engine has stopped."

    def honk(self):
        return "Beep beep!"