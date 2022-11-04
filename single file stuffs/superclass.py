# animal superclass

class Animal(object):
        
    def setWeight(self, w):
        self.w=w

    def setLength(self, l):
        self.l=l
    
    def setSpecies(self, sp):
        self.sp = sp
    
    def getLength(self):
        return (self.l)

    def getWeight(self):
        return (self.w)

    def getSpecies(self):
        return (self.sp)



# subclass Bird inherits Animal class
class Bird(Animal):
     
    def setWingSpan(self, ws):
        self.ws=ws
       
    def setAltitude(self, a):
        self.a=a
             
    def getWingSpan(self):
        return(self.ws)
       
    def getAltitude(self):
        return(self.a)
    

# subclass Fish inherits Animal class
class Fish(Animal):

    def setNumberOfFins(self, fins):
        self.fins=fins
        
    def setDepth(self, depth):
        self.depth=depth
        
    def getNumberOfFins(self):
        return(self.fins)
        
    def getDepth(self):
        return(self.depth)

		
#create the objects
eagle=Bird()
blackbird=Bird()
sparrow=Bird()

trout=Fish()

# set attributes
trout.setWeight(2)
trout.setDepth(10)
trout.setLength(0.50)


eagle.setWeight(10)
eagle.setWingSpan(2)
eagle.setLength(0.50)
sparrow.setWeight(0.5)
sparrow.setLength(0.10)

#retrive attributes
print(eagle.getWeight())
print(eagle.getLength())
print(sparrow.getWeight())
print(sparrow.getLength())

 