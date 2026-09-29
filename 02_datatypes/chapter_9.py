essential_spices = {"ginger", "cardamom", "cinnamon"}
optional_spices = {"cloves", "nutmeg", "allspice", "cinnamon"}

#  | is the union operator
all_spices = essential_spices | optional_spices
print(f"All spices are: {all_spices}")

# & is the intersection operator
common_spices = essential_spices & optional_spices
print(f"Common spices are: {common_spices}")

# Only in essential spices
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices are: {only_in_essential}")