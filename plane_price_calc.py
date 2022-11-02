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
        return True


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
        print (f"user price of first class: {self.first_price}")
        print (f"user price of standard class: {self.standard_price}")
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
        return True
## enter flight details + stuff in class
    def plane_input (self):
        print("-------------------------")
        while True:
            type_input = str(input(f"What type is your plane({planes[0][0]},{planes[1][0]},{planes[2][0]}): "))
            type_input = type_input.upper()
            valid = self.set_type(type_input)
            if valid == True:
                return True
            else: 
                return False
            
    def seat_calc (self):
        inps = get_input(1,"how many first-class seats are on the aircraft?: ")
        if inps == None:
            print ("not a valid input")
            return False
        if inps != 0:
            if inps > planes[self.type_pos][5]:
                print (f"more than the allowed {planes[self.type_pos][5]} first-class seats ")
                main_menu() 
                return False
        else:
            if planes[self.type_pos][5] > planes[self.type_pos][4]/2:
                print(f"more than half the capacity of the {planes[self.type_pos][4]} standard-class seats")
                main_menu() 
                return False
        self.first_amount = inps
        self.standard_amount = (planes[self.type_pos][4] - (inps*2))
        main_menu()
        return True


## airport details 
    def dep_location (self):
        location = input("please input your departing airport (LPl, BOH)")
        location = location.upper()
        if location == "LPL":
            print ("Liverpool John Lennon")
            self.home = location
            return True
        if location == "BOH":
            self.home = location
            return True
        else: 
            print ("not a valid input")
            main_menu()
            return False
    def arive_location(self):
        location = input(f"please input your targeted airport ({airports[0][0]},{airports[1][0]},{airports[2][0]},{airports[3][0]},{airports[4][0]})")
        location = location.upper()
        loop = 0
        for i in airports:
            if location == airports[loop][0]:
                self.destination = airports[loop][0]
                self.destination_pos = loop
                print(airports[self.destination_pos][1])
                return True
            loop += 1
            if loop == len(airports):
                print ("Invalid airport")
                main_menu()
                return False

##price plan
    def check_airports(self):
        if self.home == None or self.destination == None:
            print("you need to add your airports")
            main_menu()
            return False
        return True
    def check_planes(self):
        if self.type == None or self.destination == None:
            print("you need to add your plane type")
            main_menu()
            return False
        return True
    def check_seats (self):
        if self.first_amount == None or self.standard_amount == None:
            print("you need to add the amount of first class seats on the aircraft")
            main_menu()
            return False
        return True 
    def check_flight_range (self):
        if self.home == "LPL":
            if airports[self.destination_pos][2] > planes[self.type_pos][3]:
                print("airport too far away, pick an aircraft with a longer range")
                print(f"your plane has a range of {planes[self.type_pos][3]} and the distance to the airport is {airports[self.destination_pos][3]}")
                main_menu()
                return False 
            return True
        elif self.home == "BOH":
            if airports[self.destination_pos][3] > planes[self.type_pos][3]:
                print("airport too far away, pick an aircraft with a longer range")
                print(f"your plane has a range of{planes[self.type_pos][3]} and the distance to the airport is {airports[self.destination_pos][3]}")
                main_menu()
                return False  
            return True 
    def price_options(self):
        self.standard_price = get_input(1,"enter the price of the standard class seats: ")
        self.first_price = get_input(1,"enter the price of the first class seats: ")
        return False

## handle exeptions with int inputs :D 
def get_input (type, message):
    if type == 1: 
        try:
            inp = int(input(message))
            return inp
        except:
            return None
    return None

## the main menu with the options
def main_menu ():
    print("-------------------------")
    for i in inputs:
        print (i)
    print("-------------------------")
    choice = get_input(1,"please enter the number before your choice: ")
    if choice == 1:
        if not plane.dep_location():
            return
        if not plane.arive_location():
            return
    elif choice == 2: 
        if not plane.plane_input():
            return
        if not plane.get_data():
            return     
        if not plane.seat_calc():
            return
    elif choice == 3:
        if not plane.check_airports():
            return
        if not plane.check_planes():
            return
        if not plane.check_seats():
            return 
        if not plane.check_flight_range ():
            return
        if not plane.price_options():
            return
    elif choice == 4:
        if not plane.reset_data():
            return
        print("data cleared")
    elif choice == 5:
        print("exiting program")
        return True
    elif choice == 6:
        print("giving all secret data")
        plane.get_data_more()
    else:
        print ("invalid input")
    


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
