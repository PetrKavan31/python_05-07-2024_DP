import pickle
import json


class Airplane:
    def __init__(self, passengers, weight):
        self.passengers = passengers
        self.weight = weight

    def __str__(self):
        return f"{self.passengers}, {self.weight}"

    # Pickle packing
    def pack_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def unpack_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)

    def to_dict(self):
        return {
            "passengers": self.passengers,
            "weight": self.weight,
        }


airplane1 = Airplane(150, 1500)


def main():
    # pickle file
    pickle_data = airplane1.pack_pickle()
    print(f"Saved data to pickle file: \n {pickle_data}")
    from_pickle_airplane = Airplane.unpack_pickle(pickle_data)
    print(f"Loaded data from pickle file: \n {from_pickle_airplane.__dict__}\n")

    # json file
    serialized = json.dumps(airplane1.to_dict())
    print(f"JSON Serialized object:\n\n{serialized}\n\n")

    deserialized = json.loads(serialized)
    print(f"JSON Deserialized object:\n\n{deserialized}")


if __name__ == "__main__":
    main()
