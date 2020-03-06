import random

class orphan(object):
    race = ["black", "hispanic", "white", "asian", "indian"]
    skinc = ["black", "light black", "brown", "light brown", "tan white", "white white"]
    dsize = ["big", "average", "micro"]
    ilevel = ["genius", "smart", "average", "dumb", "mentally handicapped"]

    def __init__(self, name, race):
        self.name = name
        self.race = race
            
    def __str__(self):
        if(race == "black"):
            choice = random.randint(1,2)
            if(choice == 1):
                skinc = "black"
            if(choice == 2):
                skinc = "light black"
        if(race == "hispanic"):
            choice2 = random.randint(1,2)
            if(choice2 == 1):
                skinc = "brown"
            if(choice2 == 2):
                skinc = "light brown"
        if(race == "asian"):
            skinc = "light brown"
        if(race == "indian"):
            choice4 = random.randint(1,2)
            if(choice4 == 1):
                skinc = "brown"
            if(choice4 == 2):
                skinc = "light brown"
        if(race == "white"):
            choice3 = random.randint(1,2)
            if(choice3 == 1):
                skinc = "tan white"
            if(choice3 == 2):
                skinc = "white white"

    
