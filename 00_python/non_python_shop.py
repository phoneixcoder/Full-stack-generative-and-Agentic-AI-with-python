class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        return print("Sipping a chai with sweetness level {self.sweetness} and milk level {self.milk_level}.")