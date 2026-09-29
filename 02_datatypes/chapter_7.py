# Tuples
# These are immutable

masala_special = ("cardamom", "cinnamon", "cloves", "nutmeg")
(cardamom, cinnamon, cloves, nutmeg) = masala_special

print(cardamom)
print(cinnamon)
print(cloves)
print(nutmeg)


# Behind the scenes, is the reason for the below
ginger_ratio, cardamom_ratio = 2, 1

print(f"Ratio of G: {ginger_ratio} and C: {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"Ratio of G: {ginger_ratio} and C: {cardamom_ratio}")

# Membership
print(f"Is ginger in the masala special? {'ginger' in masala_special}")