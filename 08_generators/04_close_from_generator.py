def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

# menu = full_menu()
# print(next(menu))
# print(next(menu))
# print(next(menu))
# print(next(menu))

# print(menu)

# for chai in menu:
#     print(chai)
#     next(menu)

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("No more chai")

stall = chai_stall()
print(next(stall))
stall.close()
