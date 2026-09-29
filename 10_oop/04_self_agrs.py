class Chaicup:
    size = 150 #ml

    def describe(self):
        print(f"Chaicup is {self.size} ml")


cup = Chaicup()
cup.describe()

Chaicup.describe(cup)

cup2 = Chaicup()
cup2.size = 100

Chaicup.describe(cup2)
 