# make the imports you need here
from animal import Animal
from people import Person
from data_handling import table_print

from unicodedata import numeric


class Visit:

    __TotalVisits=0

    # Creates a visitlist list object. 
    def __init__(self, person):
        self.__personVisiting=person
        self.__uniqueVisitNumber=Visit.__TotalVisits + 1
        self.__animalVisitList = []
        Visit.__TotalVisits+=1
        self.__adoptionCompleted=False

    
    def __str__(self):
        result="Visit List #"+str(self.__uniqueVisitNumber)+"\nVisited by "+self.__personVisiting.__str__()+"Adoption completed="+ str(self.__adoptionCompleted)
        result+="\nAnimals on the visit list: "
        for animal in self.__animalVisitList:
            result+=str(animal)
        return result

    # When a person wants to make a visit, call this method to
    # print all the animals in their visitlist, and also print the customer’s
    # name and the visitlist number.
    def print_visit_list(self):
        print_list = []
        for animal in self.get_animalVisitList():
            temp = [animal.get_name(), animal.get_kind(), animal.get_age(), animal.get_color(), animal.is_vaccinated()]
            print_list.append(temp)
        print("Customer's name:" + self.get_person().get_name() + ", unique visit number: " + str(self.get_uniqueVisitNumber()) + "\n")
        table_print(["Name", "Kind", "Age", "Color", "Vaccinated?"], print_list, [10,7,5,8,5])

    # Allows people to add new animal objects to their visitlist, as long as:
    #  - The object we’re trying to add really is a Animal
    #  - The exact same animal isn’t already in the list
    #  - The animals has not been adopted yet
    #  - The person has not adopted an animal yet
    
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            if animal not in self.__animalVisitList:
                if animal.is_adopted()==False:
                    self.__animalVisitList.append(animal)

    # a method that allows people to delete an existing animal object from the visitlist.
    #  - The animal must be in the list to be removed
    def remove_animal(self, animal):
        if animal in self.__animalVisitList:
            self.__animalVisitList.remove(animal)
    
    # a method to to allow a person to make an adoption of an animal object
    # (setting the animal as adopted, and setting the visitlist as completed
    # adoption), as long as:
    #  - The adoption has not been completed yet for that visitlist
    #  - The animal is in the visitlist
    #  - The animal has not been adopted yet

    def adopting(self, animal):
        if animal in self.__animalVisitList:
            if  self.__adoptionCompleted==False:
                if animal.is_adopted()==False:
                    animal.adopt()
                    self.__adoptionCompleted=True

    # define getters and setters as needed here
    def get_person (self):
        return self.__personVisiting

    def set_person(self,p):
        self.__personVisiting = p 
    
    def get_animalVisitList(self):
        return self.__animalVisitList
    
    def get_uniqueVisitNumber(self):
        return self.__uniqueVisitNumber

    

if __name__ == "__main__":
  
    person1 = Person("Taylor", "trolls@aol.com")
    person2 = Person("Ray", "bvree@yahoo.com")
    person3 = Person("Carmen", "carlow@live.com")
    person4 = Person("Lena", "lekali@gmail.com")
    
   
    visitlist1 = Visit(person1)
    visitlist2 = Visit(person2)
    visitlist3 = Visit(person3)
    visitlist4 = Visit(person4)
    visitlist5 = Visit(person2)

   
    animal1 = Animal('Harry', 10, 'dog', 'black')
    animal2 = Animal('Edward', 3, 'cat', 'orange')
    animal3 = Animal('Bob', 2, 'bunny', 'white')
    animal4 = Animal('Hank', 4, 'turtle', 'purple')
    animal5 = Animal('Tom', 7, 'panda', 'blue')

 
    visitlist1.add_animal(animal1)
    visitlist1.add_animal(animal2)
    visitlist1.add_animal(animal3)
    visitlist1.add_animal(animal4)
    visitlist1.add_animal(animal5)


    visitlist1.remove_animal(animal1)   
    visitlist1.remove_animal(animal3)
    

    visitlist1.print_visit_list()


    visitlist1.adopting(animal2)
    


    


