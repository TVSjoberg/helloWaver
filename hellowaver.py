from dataclasses import dataclass

@dataclass
class HelloWaver:
    """" Class that waves only once """"

    name: str
    has_waved: bool = False

    def ask_to_wave(self):
        if not has_waved:
            print(f"{name} waves at you.")
            has_waved = True
        else:
            print(f"{name} just stares at you..")
