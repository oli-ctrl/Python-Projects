class Plane ():
    def __init__(self):
        self.type = None
        self.type_pos = None
        self.home = None
        self.destination = None
        self.first_amount = None
        self.standard_amount = None


    def set_type (self, inp):
        loop = 0
        for i in planes:
            if inp == planes[loop][0]:
               self.type = planes[loop][0]
               self.type_pos = loop
               return True
            loop += 1
            if loop == len(planes):
                print ("Invalid input")
                return False
    def get_data (self):
        loop = 0
        print("-------------------------")
        print (f"plane type Shortened: {planes[self.type_pos][0]}")
        print (f"plane type: {planes[self.type_pos][1]}")
        print (f"running cost per seet per 100 km: £{planes[self.type_pos][2]}")
        print (f"Maximum flight range: {planes[self.type_pos][3]}")
        print (f"Capacity if all seats are standard-class: {planes[self.type_pos][4]}")
        print (f"Capacity if all seats are first-class: {planes[self.type_pos][5]}")
    def reset_data (self):
        self.type = None
        self.type_pos = None
        self.home = None
        self.destination = None

def plane_input ():
    while True:
        type_input = str(input(f"What type is your plane({planes[0][0]},{planes[1][0]},{planes[2][0]}): "))
        type_input = type_input.upper()
        valid = plane.set_type(type_input)
        if valid == True:
            break
def seat_calc (inps):
    if inps != 0:
        if inps > planes[plane.type_pos][5]:
            print (f"more than the allowed {planes[plane.type_pos][5]} first-class seats ")
            main_menu() 
        else:
            if planes[plane.type_pos][5] > planes[plane.type_pos][4]/2:
                print(f"more than half the capacity of the {planes[plane.type_pos][4]} standard-class seats")
                main_menu() 
        plane.first_amount = inps
        plane.standard_amount = (planes[plane.type_pos][4] - (inps*2))
        main_menu()

def main_menu ():
    print("-------------------------")
    for i in inputs:
        print (i)
    print("-------------------------")
    choice = int(input("please enter the number before your choice: "))
    if choice == 1:
        print("airport stuff soon")
    elif choice == 2: 
        plane_input()
        plane.get_data()
        seat_calc(int(input("how many first-class seats are on the aircraft?: ")))
    elif choice == 3:
        print("enter price plan and calculate proffit")
    elif choice == 4:
        plane.reset_data()
        print("data cleared")
    elif choice == 5:
        print("exiting program")
        return True
    


## airport code, airport name, distence from liverpool, distance from bournemouth
airports = [["JFK", "John F Kennedy International", 5326, 5486], ["ORY", "Paris-Orly", 629, 379], ["MAD", "Adolfo Suarez Madrid-Barajas", 1428,1151], ["AMS", "Amsterdam Schiphol",526,489], ["CAI", "Cairo International",3779 ,3584 ]]
## plane code, plane name, price, maximum flight range, capacity standard class, capacity first class
planes = [["MNB", "Medium narrow body", 8, 2650, 180, 8],["LNB", "Large Narrow Body", 8, 5600, 220, 10],["MWB", "Medium Wide Body", 5, 4050, 406, 14]]

inputs = ["1. enter airport details", "2. Enter flight details","3. enter price plan", "4. Clear data", "5. Quit"]

## define plane 
plane = Plane()
## main loop

while True:
    end = main_menu()
    if end == True:
        break
