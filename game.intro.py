from orphan import orphan

def intro():
    global name
    name = input("Who is this child? ")

def claim():
    global name
    print("Welcome to the family, " + name + " Skywalker.")

#driver
intro()
claim()
