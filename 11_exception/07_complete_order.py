class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 30, "ginger": 20}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Cups must be an integer")
        total = menu[flavor] * cups
        print(f"Billing for {flavor} Chai with {cups} cups is Rs. {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for your order")

bill("ginger", 2)
bill("masala", "10")
bill("elaichi", 10)