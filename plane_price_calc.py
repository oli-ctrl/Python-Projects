class Plane ():
    def __init__(self):
        self.type = None
        self.type_pos = None
        self.max_distance = None
        self.home = None
        self.destination = None


    def set_type (self, inp):
        loop = 0
        for i in planes:
            if inp == planes[loop][0]:
               self.type = planes[loop][0]
               self.type_pos = loop
               return True
            elif loop > len(planes):
                print("cant find plane")
                return False
            loop += 1


    

## airport code, airport name, distence from liverpool, distance from bournemouth
airports = [["JFK", "John F Kennedy International", 5326, 5486], ["ORY", "Paris-Orly", 629, 379], ["MAD", "Adolfo Suarez Madrid-Barajas", 1428,1151], ["AMS", "Amsterdam Schiphol",526,489], ["CAI", "Cairo International",3779 ,3584 ]]
## plane code, plane name, maximum flight range, capacity standard class, capacity first class
planes = [["MNB", "Medium narrow body", 8, 2650, 180, 8],["LNB", "Large Narrow Body", 8, 5600, 220, 10],["MWB", "Medium Wide Body", 5, 4050, 406, 14]]

## define plane 
plane = Plane()
## main loop
while True:
    ## inputs for plane
    while True:
        type_input = str(input("What type is your plane: "))
        valid = plane.set_type(type_input)
        if valid == True:
            break
        
    print ("the plane type is",plane.type)
    print ("the plane pos is", planes[plane.type_pos])
    break