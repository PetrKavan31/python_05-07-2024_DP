class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = "Data of the Singleton instance"

    def get_data(self):
        return self.data


# Testování Singleton vzoru
singleton1 = Singleton()
singleton2 = Singleton()

print("Is singleton1 the same instance as singleton2?", singleton1 is singleton2)  # Výstup: True

print("Data of singleton1:", singleton1.get_data())  # Výstup: Data of the Singleton instance
print("Data of singleton2:", singleton2.get_data())  # Výstup: Data of the Singleton instance

# Modifikace dat na jedné instanci
singleton1.data = "Modified data"

print("Data of singleton1:", singleton1.get_data())  # Výstup: Modified data
print("Data of singleton2:", singleton2.get_data())  # Výstup: Modified data
