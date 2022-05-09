# make the imports you need here
from re import T
from data_handling import table_print

class Animal:
    #Animals admitted to the shelter
    __adopted_list = []
    __all_animals_list = []

    @staticmethod
    def tracking():
        print("Total animals to be adopted: " + str(len(Animal.__all_animals_list) - len(Animal.__adopted_list)) + "\n")

    @staticmethod
    def get_all_animals():
        return Animal.__all_animals_list

    @staticmethod
    def get_adopted_animals():
        return Animal.__adopted_list

    @staticmethod
    def get_available_animals():
        available_list = []
        for animal in Animal.__all_animals_list:
            if not animal.__adopted:
                available_list.append(animal)              
                
        return available_list

    # Which animal kind is the most popular (i.e. gets adopted the most)?
    # Loop through all adoptions, adding animal kinds to a single master list
    # Initialize variables to hold the most popular animal and the number of times it appears
      
    @staticmethod
    def report_most_popular():
        #Put the kinds of animals in a list
        kind_list = []
        for animal in Animal.get_adopted_animals():
            kind_list.append(animal.get_kind())
        return max(kind_list, key = kind_list.count)
        
    # Give a report of all of the animals of a given kind and lower than a certain age at the shelter that have not been adopted yet. 
    @staticmethod
    def report_not_adopted(kind, age):
        report = []
        #Find the animals that are not adopted
        for animal in Animal.get_available_animals():
            if(animal.get_kind() == kind) and animal.get_age()<=age:
                temp = [animal.get_name(), animal.get_age()]
                report.append(temp)

        #Print report into a table
        table_print(["Animal", "Age"], report, [10,10]) 
    
    def __init__(self, name, age, kind, color, vaccinated = False):
        self.__name = name
        self.__age = age
        self.__kind = kind
        self.__color = color
        self.__vaccinated = vaccinated
        self.__adopted = False      
        Animal.__all_animals_list.append(self)

    def __str__(self):
        if not self.__adopted:
            reply = "A "
            reply += self.__color + " "
            reply += self.__kind + " named "
            reply += self.__name + ", who is "
            reply += str(self.__age) + " years old "
            reply += "is up for adoption.\n"
            reply += self.__name + " is "
            if not self.__vaccinated:
                reply += "not "
            reply += "vaccinated.\n"
        else:
            reply = self.__name + " has already been adopted.\n"
        return reply

    # compare two animal objects based on name, kind, age, and color
    def __eq__(self, other):
        if self.__name != other.__name:
            return False
        elif self.__age != other.__age:
            return False
        elif self.__kind != other.__kind:
            return False
        elif self.__color != other.__color:
            return False
        else:
            return True

    #getters and setters
    
    def adopt(self):
        Animal.__adopted_list.append(self)
        self.__adopted = True

    def is_adopted(self):
        return self.__adopted

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_age(self):
        return self.__age
    
    def get_kind(self):
        return self.__kind
    
    def vaccinate(self):
        self.__vaccinated = True

    def is_vaccinated(self):
        return self.__vaccinated

    

if __name__ == "__main__":
    #create a test code here
    animal1 = Animal('Harry', 10, 'dog', 'black')
    animal2 = Animal('Edward', 3, 'cat', 'orange')
    animal3 = Animal('Bob', 2, 'bunny', 'white')
    animal4 = Animal('Hank', 4, 'dog', 'purple')
    animal5 = Animal('Tom', 7, 'panda', 'blue')
    animal6 = Animal('Tom', 7, 'dog', 'blue')
    animal1.adopt()
    animal2.adopt()
    animal3.adopt()
    animal4.adopt()
    animal5.adopt()
    animal6.adopt()
    #print("The most popular animal kind is: "+ Animal.report_most_popular())

    animal1 = Animal('Percy', 10, 'koala', 'black')
    animal2 = Animal('Joe', 3, 'monkey', 'orange')
    animal3 = Animal('Sadie', 2, 'bunny', 'white')
    animal4 = Animal('Jayda', 4, 'dog', 'purple')
    animal5 = Animal('Kathleen', 7, 'dog', 'blue')
    Animal.report_not_adopted('dog', 11)









   