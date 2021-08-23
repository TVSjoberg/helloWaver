from dataclasses import dataclass

@dataclass
class HelloWaver:
    """Class that waves only once """

    name: str
    has_waved: bool = True

    _n_wavers: int = 0

    @property
    def n_wavers(self):
        return type(self)._n_wavers

    @n_wavers.setter
    def n_wavers(self, val):
        type(self)._n_wavers = val

    def __post_init__(self):
        self.n_wavers += 1

    def ask_to_wave(self):
        if not self.has_waved:
            print(f"{self.name} waves at you.")
            self.has_waved = True
        else:
            print(f"{self.name} just stares at you..")

    def how_many_wavers(self):
        print(f'There are currently {self.n_wavers} wavers in existance.')
