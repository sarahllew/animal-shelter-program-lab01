# Animal.py class

# contains the definition of what an Animal is -- 
# define attributes:
'''
    * species - str: represents species of the animal -- ensure upper case
    * weight - float -- represents weight in lbs of animal
    * age - int -- represents age in years of animal
    * name - str -- represents name of animal -- ensure upper case

- need the constructor, attributes as None by default
- support 'setter' methods
- each Animal object should call toString --> returns a str with all attributes
'''

class Animal:
    ''' Animal class type that contains animal attributes '''
    def __init__(self, species = None, weight = None, age = None, name = None):
        if species != None:
            species = species.upper()
        if name != None:
            name = name.upper()
        self.species = species
        self.weight = weight
        self.age = age
        self.name = name

    def setSpecies(self, species):
        if species != None:
            species = species.upper()
            self.species = species
        
    def setWeight(self, weight):
        self.weight = weight
        
    def setAge(self, age):
        self.age = age
        
    def setName(self, name):
        if name != None:
            name = name.upper()
            self.name = name 

    def toString(self):
        ''' returns a str with all the animal attributes '''
        return ("Species: {}, Name: {}, Age: {}, Weight: {}"\
              .format(self.species, self.name, self.age, self.weight))



        
