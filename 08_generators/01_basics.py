def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 2: Elaichi Chai"

stall = serve_chai();

for chai in stall:
    print(chai)

# Example 2
def cups():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

cup = cups()

print(next(cup))
print(next(cup))
print(next(cup))
print(next(cup)) #Error : StopIteration