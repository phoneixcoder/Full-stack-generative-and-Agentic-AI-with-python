class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return(f"Order of {self.type} Chai with size {self.size}")

order = ChaiOrder("milk", 100)
print(order.summary())

order2 = ChaiOrder("milk", 200)
print(order2.summary())
