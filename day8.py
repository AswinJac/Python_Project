def greet(a, b):
    print(f"Hello {a}")
    print(f"You are at {b}")


name = input("Enter name")
loc = input("Enter location cordinates")
greet(b=loc, a=name)
