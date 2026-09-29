def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Order of {item} Chai with quantity {quantity} is Rs. {cost}")
    except KeyError:
        print("Sorry that item is not available")
    except TypeError:
        print("Quantity must be an integer")


process_order("ginger", 2)
process_order("masala", "10")
