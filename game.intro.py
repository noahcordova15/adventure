name = 'unknown'

def intro():
    name = input("Who is this child? ")
    claim(name)

def claim(name):
    print("Welcome to the family, " + name + " Skywalker.")

intro()
