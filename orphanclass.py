import random

class orphan(object):
    #["black", "hispanic", "white", "asian", "indian"]
    #["black", "light black", "brown", "light brown", "tan white", "white white"]
    #["big", "average", "micro"]
    #["genius", "smart", "average", "dumb", "mentally handicapped"]

    def __init__(self,name,race,skinc,size,ilevel):
        self.name = name
        self.race = race
        self.skinc = skinc
        self.size = size
        self.intel = intel

    def chooseRace(self):
        self.race = input("What race is your character? Choose a number."
              "Black: 1"
              "Hispanic: 2"
              "White: 3"
              "Asian: 4"
              "Indian: 5"
              "Your race number: ")
            
    def __str__(self):
        if(race == 1):#black
            skchoice = random.randint(1,2)
            if(skchoice == 1):
                self.skinc = "black"
            if(skchoice == 2):
                self.skinc = "light black"
            self.size = "big"
            ilchoice = random.randint(1,3)
            if(ilchoice == 1):
                self.intel = "smart"
            if(ilchoice == 2):
                self.intel = "average"
            if(ilchoice == 3):
                self.intel = "dumb"
        if(race == 2):#hispanic
            skchoice2 = random.randint(1,2)
            if(skchoice2 == 1):
                self.skinc = "brown"
            if(skchoice2 == 2):
                self.skinc = "light brown"
            self.size = "above average"
            ilchoice = random.randint(1,3)
            if(ilchoice2 == 1):
                self.intel = "smart"
            if(ilchoice2 == 2):
                self.intel = "average"
            if(ilchoice2 == 3):
                self.intel = "dumb"
        if(race == 4):#asian
            self.skinc = "light brown"
            self.size = "micro"
            ilchoice4 = random.randint(1,2)
            if(ilchoice4 == 1):
                self.intel = "genius"
            if(ilchoice4 == 2):
                self.intel = "smart"
        if(race == 5):#indian
            skchoice4 = random.randint(1,2)
            if(skchoice4 == 1):
                self.skinc = "brown"
            if(skchoice4 == 2):
                self.skinc = "light brown"
            self.size = "micro"
            ilchoice5 = random.randint(1,2)
            if(ilchoice5 == 1):
                self.intel = "genius"
            if(ilchoice5 == 2):
                self.intel = "smart"
        if(race == 3):#white
            skchoice3 = random.randint(1,2)
            if(skchoice3 == 1):
                self.skinc = "tan white"
            if(skchoice3 == 2):
                self.skinc = "white white"
            self.size = "average"
            ilchoice3 = random.randint(1,3)
            if(ilchoice3 == 1):
                self.intel = "smart"
            if(ilchoice3 == 2):
                self.intel = "average"
            if(ilchoice3 == 3):
                self.intel = "dumb"

    
