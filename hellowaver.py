from dataclasses import dataclass


class HelloWaver:
    """Class that waves only once"""

    _n_wavers: int = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.has_waved = True
        self.n_wavers += 1

    @property
    def n_wavers(self):
        return type(self)._n_wavers

    @n_wavers.setter
    def n_wavers(self, val):
        type(self)._n_wavers = val

    def ask_to_wave(self) -> bool:
        """Main function of the program"""
        if not self.has_waved:
            print(f"{self.name} waves at you.")
            self.has_waved = True
            return True
        else:
            print(f"{self.name} just stares at you..")
            return False

    @classmethod
    def how_many_wavers(cls):
        print(f"There are currently {cls._n_wavers} wavers in existence.")
