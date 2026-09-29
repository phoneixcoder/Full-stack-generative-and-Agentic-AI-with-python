# file = open("order.txt", "w")
# try:
#     file.write("Masala Chai with 100 ml")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("Ginger Tea with 100 ml")