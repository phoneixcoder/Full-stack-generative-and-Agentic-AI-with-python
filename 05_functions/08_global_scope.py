chai_type = "Elaichi"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Masala Chai"
    kitchen()

front_desk()
print(f"Chai type is: {chai_type}")