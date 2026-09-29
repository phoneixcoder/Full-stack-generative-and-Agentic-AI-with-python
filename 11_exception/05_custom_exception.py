# def brew_chai(flavor):
#     if flavor not in ["ginger", "masala", "elaichi"]:
#         raise ValueError("Custom: Invalid flavor")
#     print(f"Preparing {flavor} chai")


# brew_chai("milk")
    

class OutOfIngredients(Exception):
    pass

def brew_chai(flavor):
    if flavor not in ["ginger", "masala", "elaichi"]:
        raise OutOfIngredients("Custom: Invalid flavor")
    print(f"Preparing {flavor} chai")

brew_chai("milk")
brew_chai("ginger")
