from operator import truediv
from random import randint


class Doge():
    def __init__(self, name, energy ,health, is_alive: bool):
        self.name = name
        self.energy = 20
        self.health = 80
        self.is_alive = True


    def attack(self):
        returned_damage = (self.energy//10) * randint(10,20)
        self.energy -= randint(1,4)
        
        return returned_damage
    
    def regenerate(self):
        if self.health < 100:
            self.health += self.energy//100 * randint(5,10)
            self.energy -= randint(1,6)
            if self.health > 100:
                self.health = 100
        else:
            self.health = 100

    def eat(self):
        self.energy += randint (5,10)
        if self.energy > 20:
            self.energy = 20

    def attacked(self,received_damage):
        self.health -= received_damage
    
    def check_alive(self):
        if self.health < 1:
            self.is_alive = False
            return False
    def bark(self):
        print(self.name,("barked"))

def player_turn():
    player_action = input("what do you want your doge to do (`attack`, `regenerate`,`eat`): ")
    while True:
        if player_action == "attack":
            returned_damage = player_doge.attack()
            print("the dog inflicted {} damage to its opponent!!!".format(returned_damage))
            opponent_doge.attacked(returned_damage)
            print("the enemy doge is on {} health".format(opponent_doge.health))
            break
        elif player_action == "regenerate":
            player_doge.regenerate()
            break
        elif player_action == "eat":
            player_doge.eat()
            break

## the dogs name inputs
name1 = input("please name your doge: ")
name2 = input("please name the opponent doge: ")
## game loop, breaks when one of the dogs dies
player_doge= Doge(name1,0,0,True)
opponent_doge= Doge(name2,0,0,True)
while True:
    ## gives the doge objects its name and health


    ## checks if the dogs are alive
    if player_doge.check_alive() == False:
        print("your doge is ded")
        break
    elif opponent_doge.check_alive() == False:
        print("the enemy doge is ded")
        break

    ## player actions and player dog stats 
    print("your doge stats: Health: {} energy: {}".format(player_doge.health, player_doge.energy))
    player_turn()
        


    
    




        
        
        