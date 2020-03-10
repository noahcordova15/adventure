#from orphan import orphan

def intro():
    global name
    name = input("Who is this child? (Input name) ")

def claim():
    global name
    print("Welcome to the family, " + name + " Skywalker.")

def start():
    global ptype
    global name
    print(name+", you have been adopted by an interesting family. You will require a certain set of skills; you will use these skills to complete tasks that build towards an inherently good or evil goal.")
    choice = input("Now, choose, would you like to be good or evil? (type G or E)")
    if(choice in ['G', 'g']):
          ptype = 1
          print("Congratulations, you are good")
    elif(choice in ['E', 'e']):
          ptype = 2
          print("Congratulations, you are evil")
    else:
          print("Invalid input. Please try again.")
    

#driver
intro()
claim()
start()
