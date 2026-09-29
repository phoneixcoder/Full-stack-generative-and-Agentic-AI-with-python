class ChaiOrder:
    def __init__(self, type_, sweetness, size):
        self.type = type_
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def summary(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def summaryString(cls, order_data):
        type, sweetness, size = order_data.split(",")
        return cls(type, sweetness, size)

class ChaiUtils:
    @staticmethod
    def isValidSize(size):
        return size.lower() in ["small", "medium", "large"]

order1 = ChaiOrder.summaryString("milk,mild,100")
order2 = ChaiOrder.summary({"tea_type": "milk", "sweetness": "mild", "size": 100})
order3 = ChaiOrder("milk", "mild", 100)

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)