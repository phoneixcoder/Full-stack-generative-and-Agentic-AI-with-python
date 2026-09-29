favorite_chais = [
    "Masala chai",
    "Green tea",
    "Masala chai",
    "Iced lemon tea",
    "Ginger chai",
    "Green tea",
    "Iced peach tea",
    "Elaichi tea",
]

unique = {my_chai for my_chai in favorite_chais}
print(unique)

recipe = {
    "Masala chai": ["ginger", "cardamom", "clove"],
    "Elaichi tea": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "clove", "black pepper"],
}

unique2 = {spice for masala in recipe.values() for spice in masala}

print(unique2)
