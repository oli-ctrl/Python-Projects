


class Plane ():
    def __init__(self):
        self.type = None
        self.type_pos = None
        self.home = None
        self.destination = None
        self.destination_pos = None
        self.first_amount = None
        self.standard_amount = None
        self.first_price = None
        self.standard_price = None


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
        print("-------------------------")
        print (f"plane type Shortened: {planes[self.type_pos][0]}")
        print (f"plane type: {planes[self.type_pos][1]}")
        print (f"running cost per seet per 100 km: £{planes[self.type_pos][2]}")
        print (f"Maximum flight range: {planes[self.type_pos][3]}")
        print (f"Capacity if all seats are standard-class: {planes[self.type_pos][4]}")
        print (f"Capacity if all seats are first-class: {planes[self.type_pos][5]}")


    def get_data_more (self):
        print("-------------------------")
        print (f"plane type Shortened: {planes[self.type_pos][0]}")
        print (f"plane type: {planes[self.type_pos][1]}")
        print (f"running cost per seet per 100 km: £{planes[self.type_pos][2]}")
        print (f"Maximum flight range: {planes[self.type_pos][3]}")
        print (f"Capacity if all seats are standard-class: {planes[self.type_pos][4]}")
        print (f"Capacity if all seats are first-class: {planes[self.type_pos][5]}")
        print (f"user amount of first class: {self.first_amount}")
        print (f"user amount of standard class: {self.standard_amount}")
        print (f"user chosen home {self.home}")
        print (f"user chosen destination {self.destination}")

    def reset_data (self):
        self.type = None
        self.type_pos = None
        self.home = None
        self.destination = None
        self.destination_pos = None
        self.first_amount = None
        self.standard_amount = None
        self.first_price = None
        self.standard_price = None

## enter flight details + stuff in class
def plane_input ():
    print("-------------------------")
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
        return


## airport details 
def dep_location ():
    location = input("please input your departing airport (JPl, BOH)")
    location = location.upper()
    if location == "JPL" or location == "BOH":
        plane.home = location
    else: 
        print ("not a valid input")
        main_menu()
        return
def arive_location():
    
    location = input(f"please input your targeted airport ({airports[0][0]},{airports[1][0]},{airports[2][0]},{airports[3][0]},{airports[4][0]},)")
    location = location.upper()
    loop = 0
    for i in airports:
        if location == airports[loop][0]:
            plane.destination = airports[loop][0]
            plane.destination_pos = loop
            print(airports[plane.destination_pos][1])
            return True
        loop += 1
        if loop == len(airports):
            print ("Invalid airport")
            main_menu()
            return

##price plan
def check_airports():
    if plane.home == None or plane.destination == None:
        print("you need to add your airports")
        main_menu()
        return
def check_planes():
    if plane.type == None or plane.destination == None:
        print("you need to add your plane type")
        main_menu()
        return
def check_seats ():
    if plane.first_amount == None or plane.standard_amount == None:
        print("you need to add the amount of first class seats on the aircraft")
        main_menu()
        return
def check_flight_range ():
    if plane.home == "JPL":
        if airports[plane.destination_pos][2] > planes[plane.type_pos][3]:
            print("airport too far away, pick an aircraft with a longer range")
            print(f"your plane has a range of{planes[plane.type_pos][3]} and the distance to the airport is {airports[plane.destination_pos][3]}")
    elif plane.home == "BOH":
        if airports[plane.destination_pos][3] > planes[plane.type_pos][3]:
            print("airport too far away, pick an aircraft with a longer range")
            print(f"your plane has a range of{planes[plane.type_pos][3]} and the distance to the airport is {airports[plane.destination_pos][3]}")
def price_options():
    plane.standard_price = int(input("enter the price of the standard class seats"))
    plane.first_price = int(input("enter the price of the first class seats"))
    

def main_menu ():
    print("-------------------------")
    for i in inputs:
        print (i)
    print("-------------------------")
    choice = int(input("please enter the number before your choice: "))
    if choice == 1:
        dep_location()
        arive_location()
    elif choice == 2: 
        plane_input()
        plane.get_data()
        seat_calc(int(input("how many first-class seats are on the aircraft?: ")))
    elif choice == 3:
        check_airports()
        check_planes()
        check_seats()
        check_flight_range ()
        price_options()
    elif choice == 4:
        plane.reset_data()
        print("data cleared")
    elif choice == 5:
        print("exiting program")
        return True
    elif choice == 6:
        print("giving all secret data")
        plane.get_data_more()
    


## airport code, airport name, distence from liverpool, distance from bournemouth
airports = [["JFK", "John F Kennedy International", 5326, 5486], ["ORY", "Paris-Orly", 629, 379], ["MAD", "Adolfo Suarez Madrid-Barajas", 1428,1151], ["AMS", "Amsterdam Schiphol",526,489], ["CAI", "Cairo International",3779 ,3584 ]]
## plane code, plane name, price, maximum flight range, capacity standard class, capacity first class
planes = [["MNB", "Medium narrow body", 8, 2650, 180, 8],["LNB", "Large Narrow Body", 8, 5600, 220, 10],["MWB", "Medium Wide Body", 5, 4050, 406, 14]]
## idk why i did it this way D:
inputs = ["1. enter airport details", "2. Enter flight details","3. enter price plan", "4. Clear data", "5. Quit"]

## define plane 
plane = Plane()
## main loop

while True:
    end = main_menu()
    if end == True:
        break
