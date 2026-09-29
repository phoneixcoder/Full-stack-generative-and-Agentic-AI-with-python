ingredients = ["water", "milk", "black", "tea"]
print(f"Ingredients are: {ingredients}")

ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

ingredients.insert(2, "sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove("sugar")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]

ingredients.extend(spice_options) # append list at the end
print(f"Ingredients are: {ingredients}")

# Operator Overloading
print(f"Ingredients are: {ingredients + spice_options}")
print(f"Ingredients are: {ingredients * 2}")

# Bytearray

raw_spice_data = bytearray(b"CARDAMOM")
raw_spice_data = raw_spice_data.replace(b"CARDA", b"CINNA")
print(f"Raw spice data: {raw_spice_data}")
