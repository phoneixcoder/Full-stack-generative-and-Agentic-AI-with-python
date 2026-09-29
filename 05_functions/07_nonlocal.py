def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Masala Chai"
    kitchen()
    print(f"Chai type is: {chai_type}") 

update_order()