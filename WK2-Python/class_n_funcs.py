from typing import List


class Profile:
    def __init__(self,
                 name: str,
                 age: int,
                 nicknames: List[str],
                 phone: str,
                 address: str):
        self.name = name
        self.age = age
        self.nicknames = nicknames
        self.phone = phone
        self.address = address

    def get_name(self):
        return self.name


def my_profile(name: str, age: int, nicknames: List[str]):
    print(f"My name is {name} and my age is {age}")
    print(f"I have many nicknames. e.g. {nicknames}")


if __name__ == '__main__':
    my_nicknames = ["goggle", "winston"]
    my_profile(name="Yu",
               age=18,
               nicknames=my_nicknames)

    # Let us write a Car class in a different file and associate Profile with the Car class; 1 person many cars

    # Let us write a Engine class in a different file and associate Car with the Engine class; 1 car 1 engine

    # Now, let us instantiate some examples. Me -> Car -> Engine


