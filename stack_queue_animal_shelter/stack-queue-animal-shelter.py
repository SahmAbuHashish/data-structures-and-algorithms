from stack_and_queue.stack_and_queue import Queue

#define a class called Cat 
class Cat():
  def __init__(self,name):
    self.name = name
    self.kind = "cat"


#define a class called Dog 
class Dog():
  def __init__(self,name):
    self.name = name
    self.kind = "dog"   


#  define a class AnimalShelter that save cats and dogs to find a  shelter for these animal. 
class AnimalShelter():
    def __init__(self):
        self.cat = []
        self.dog = []

    #check if the animal is cat or dog then add it to the queue. 
    def enqueue(self, animal):
        
        if animal.kind == "cat":
          self.cat.enqueue(animal.name)
        elif animal.kind == "dog":
          self.dog.enqueue(animal.name)


    #check if the animal is cat or dog then delete the animal from queue 
    def dequeue(self, pref):
         if pref == "dog":
            return self.dog.pop(0)[0]
         elif pref == "cat":
            return self.cat.pop(0)[0]
         else:
            return None


     
