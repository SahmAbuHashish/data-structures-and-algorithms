from stack_and_queue.stack_and_queue import Queue

# #define a class called Cat 
# class Cat():
#   def __init__(self,name):
#     self.name = name
#     self.kind = "cat"


# #define a class called Dog 
# class Dog():
#   def __init__(self,name):
#     self.name = name
#     self.kind = "dog"   


# #  define a class AnimalShelter that save cats and dogs to find a  shelter for these animal. 
# class AnimalShelter():
#     def __init__(self):
#         self.cat = []
#         self.dog = []

#     #check if the animal is cat or dog then add it to the queue. 
#     def enqueue(self, animal):
        
#         if animal.kind == "cat":
#           self.cat.enqueue(animal.name)
#         elif animal.kind == "dog":
#           self.dog.enqueue(animal.name)


#     #check if the animal is cat or dog then delete the animal from queue 
#     def dequeue(self, pref):
#          if pref == "dog":
#             return self.dog.pop(0)[0]
#          elif pref == "cat":
#             return self.cat.pop(0)[0]
#          else:
#             return None

#-----------------------------------------------------------------------------------------

#define a class AnimalShelter that save cats and dogs to find a  shelter for these animal.      
class AnimalShelter():
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
    
    #returns a string representation of the class AnimalShelter
    def __str__(self):
        return f"AnimalShelter(dog={self.dog}, cat={self.cat})"
    
    #check if the animal is cat or dog then add it to the queue.
    def enqueue(self, animal):
        if animal["kind"] == "cat":
          self.cat.enqueue(animal)
        elif animal["kind"] == "dog":
          self.dog.enqueue(animal)

    #check if the animal is cat or dog then delete the animal from queue.
    def dequeue(self, pref):
          if pref != 'cat' and pref != 'dog':
            return None 
          if pref == 'cat' :
           return self.cat.dequeue()
          if pref == 'dog' :
           return self.dog.dequeue()


class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


# Create animal objects
dog1 = Animal("dog", "dog_1")
dog2 = Animal("dog", "dog_2")
cat1 = Animal("cat", "cat_1")
cat2 = Animal("cat", "cat_2")

# Create an instance of AnimalShelter
shelter = AnimalShelter()

# Enqueue animals
shelter.enqueue(dog1)
shelter.enqueue(cat1)
shelter.enqueue(dog2)
shelter.enqueue(cat2)

# Dequeue animals
dog = shelter.dequeue("dog")
print(f"{dog.name}")

cat = shelter.dequeue("cat")
print(f"{cat.name}")

#------------------------------------------------
class Animal:
    def __init__(self, species, name):
        """
        Initializes an empty Animal.
        """
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        """
        Initializes an empty AnimalShelter.
        """
        self.dog_queue = []
        self.cat_queue = []



    def enqueue(self, animal):
        """
        add animal value to the end of list.
        """
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        """
        Removes and returns the value of the front list.
        """
        if pref == "dog":
            if len(self.dog_queue) > 0:
                return self.dog_queue.pop(0)
        elif pref == "cat":
            if len(self.cat_queue) > 0:
                return self.cat_queue.pop(0)
        return None
