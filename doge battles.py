from gc import freeze
from operator import truediv
from random import randint


class Doge():
    def __init__(self, name, energy ,health, is_alive: bool):
        self.name = name
        self.energy = 100
        self.health = 100
        self.is_alive = True


    def attack(self):
        returned_damage = (self.energy//10) * randint(1,3)
        self.energy -= randint(15,30)
        if self.energy < 1:
            self.energy = 1
        return returned_damage
    
    def regenerate(self):
        if self.health < 100:
            self.health += self.energy//10 * randint(5,10)
            self.energy -= randint(10,40)
            if self.health > 100:
                self.health = 100
            if self.energy < 1:
                self.energy = 1
        else:
            self.health = 100

    def eat(self):
        self.energy += randint (30,70)
        if self.energy > 100:
            self.energy = 100

    def attacked(self,received_damage):
        self.health -= received_damage
    
    def check_alive(self):
        if self.health < 1:
            self.is_alive = False
            return False

    def bark(self):
        print(self.name,("barked"))

    def freeze(self):
        if randint(1,2) == 1:
            self.health += randint (5,10)
        else:
            self.energy += randint (1,4)

def player_turn():
    player_action = input("what do you want your doge to do (`attack`, `regenerate`,`eat`): ")
    if player_action == "attack":
        returned_damage = player_doge.attack()
        print("your doge inflicted {} damage to its opponent!!!".format(returned_damage))
        opponent_doge.attacked(returned_damage)
        print("the enemy doge is on {} health".format(opponent_doge.health))
        return True
    elif player_action == "regenerate":
        player_doge.regenerate()
        return True
    elif player_action == "eat":
        player_doge.eat()
        return True
    else: 
        print("invalid input")
        return False




def enemy_turn():
    attack_weight = 3
    regenerate_weight = opponent_doge.health/10
    eat_weight = opponent_doge.energy/10
    if attack_weight < regenerate_weight and attack_weight < eat_weight:
        returned_damage = opponent_doge.attack()
        print("the enemy doge inflicted {} damage to you!!!".format(returned_damage))
        player_doge.attacked(returned_damage)
        return True
    elif eat_weight < regenerate_weight and eat_weight < attack_weight: 
        print("the opponent doge ate")
        opponent_doge.eat()
        return
    elif regenerate_weight< eat_weight and regenerate_weight < attack_weight:
        print("the opponent doge regenerated")
        opponent_doge.regenerate()
        return
    

    print(attack_weight,regenerate_weight,eat_weight)
    print("The enemy doge froze and regained his breath gaining some energy and health")
    player_doge.freeze()






## the dogs name inputs
name1 = input("please name your doge: ")
name2 = input("please name the opponent doge: ")

## create doges 
player_doge= Doge(name1,0,0,True)
opponent_doge= Doge(name2,0,0,True)




## game loop, breaks when one of the dogs dies
while True:

    ## checks if the dogs are alive
    if player_doge.check_alive() == False:
        print("your doge is ded")
        break
    elif opponent_doge.check_alive() == False:
        print("the enemy doge is ded")
        break

    ## player actions and player dog stats 
    print("your doge stats: Health: {} energy: {}".format(player_doge.health, player_doge.energy))
    while True:
        valid = player_turn()
        if valid == True:
            break
    enemy_turn()
input("press enter key to close")