chai_menu = {"masala": 30, "ginger": 100}

try:
    chai_menu["Pinku"]
except KeyError:
    print("Key not found")