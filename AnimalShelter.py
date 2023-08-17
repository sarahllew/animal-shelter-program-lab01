# AnimalShelter.py

# contains the definition of what a single AnimalShelter object is
# object obtains a dictionary structure where the keys of the dictionary will
# be a str type representing the spwcies(uppercase) 
# dictionary value: list of Animal objects that AnimalShelter contains
'''
check if the species is none before doing upper() for all:
'''

from Animal import Animal
class AnimalShelter:
    ''' class that contains the definition of what a single AnimalShelter object
        obtains dictionary where keys are str representing species
        values are list of Animal objects that Animal shelter contains '''
    def __init__(self):
        self.animalshelter = {}

    def addAnimal(self, animal):
        ''' method that adds an Animal object (animal) to AnimalShelter
            added to the end of the list of existing animals of same species'''
        if animal.species != None:
            animal.species = animal.species.upper()
            if self.animalshelter.get(animal.species) == None:
                self.animalshelter[animal.species] = [animal]
            elif not animal in self.animalshelter.get(animal.species):
                self.animalshelter[animal.species].append(animal)
        else:
            if self.animalshelter.get(animal.species) == None:
                self.animalshelter[animal.species] = [animal]
            elif not animal in self.animalshelter.get(animal.species):
                self.animalshelter[animal.species].append(animal)
            
    def removeAnimal(self, animal):
        ''' removes an Animal object (animal) from the AnimalShelter if it exists.
            checks and sees if the parameter animal object has the same
            species, name, age, and weight as an existing animal '''
        if self.animalshelter.get(animal.species) != None: 
            for a in self.animalshelter.get(animal.species):
                if animal.name == a.name:
                    if animal.age == a.age:
                        if animal.species == a.species:
                            if animal.weight == a.weight:
                                self.animalshelter.get(animal.species).remove(a)

    def removeSpecies(self, species):
        ''' removes all animals of a certain species if it exists
            needs to remove the species entry from the AnimalShelter's dictionary'''
        if species != None:
            species = species.upper()
            if species in self.animalshelter.keys():
                del self.animalshelter[species]

    def getAnimalsBySpecies(self,species):
        '''returns a str of all animals of certain species. -- one line for each animal
            order should be dictacted by the order of the Animals in the AnimalShelter's list
            toString() method should be used
            if no animals of the species exist, returns an empty string'''
        if species != None:
            species = species.upper()
            if self.animalshelter.get(species) == None:
                return ""
            else:
                x = ""
                for animal in self.animalshelter[species]:
                   x += ((animal.toString())) + "\n"
                return x[:-1]
        else:
            if self.animalshelter.get(species) == None:
                return ""
            else:
                x = ""
                for animal in self.animalshelter[species]:
                    x += ((animal.toString())) + "\n"
                return x[:-1]
                    
    def doesAnimalExist(self, animal):
        ''' returns true if the parameter animal (with matching species, name, age, weight)
            exists in the AnimalShelter. returns false otherwise '''
        if self.animalshelter.get(animal.species) != None and animal in self.animalshelter.get(animal.species):
            for a in self.animalshelter.get(animal.species):
                if animal.name == a.name and animal.age == a.age and animal.weight == a.weight:
                    return True
                else:
                    return False
        else:
            return False
            
# removeAnimal method fails 
# doesAnimalExist returns false if there are 2 of the same species
##
##a1 = Animal("dog", 22.2, 3, "Bo")
##a2 = Animal("cat", 22.3, 4, "Bow")
##a3 = Animal("rat", 55.2, 2, "Boz")
##a4 = Animal("dragon", 300, 45, "Red")
##a5 = Animal("bunny")
##a6 = Animal("dog", 55.2, 2, "Boz")
##
##
##Pets = AnimalShelter()
##Pets.addAnimal(a1)
##Pets.addAnimal(a2)
##Pets.addAnimal(a3)
##Pets.addAnimal(a4)
##Pets.addAnimal(a5)
##Pets.addAnimal(a6)
##Pets.removeAnimal(a2)
##
##print(Pets.doesAnimalExist(a1))
##print(Pets.doesAnimalExist(a2))
##print(Pets.doesAnimalExist(a3))
##print(Pets.doesAnimalExist(a4))
##print(Pets.doesAnimalExist(a5))
##print(Pets.doesAnimalExist(a6))





