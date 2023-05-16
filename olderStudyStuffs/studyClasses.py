"""Certainly, here are slightly simplified questions on the same topic:

1. Define a class `Dog` with an attribute `name`. Also, within this class, define a method `bark` that prints "Woof!"

2. Create an instance of the `Dog` class you just defined. The instance should represent a dog named Max. Use the `bark` method to make Max bark.

3. Add an `age` attribute to the `Dog` class. This attribute should be provided when a new dog is created. 

4. Modify the `Dog` class so that the `name` attribute is automatically set to 'Puppy' whenever a new dog is created without a name.

5. In the `Dog` class, add a method `birthday` that increases the `age` attribute by 1.

6. Add a `__str__` method to the `Dog` class. This method should return a string in the following format: `"[Name] is [age] year(s) old"`.

7. Create a subclass of `Dog` called `Retriever`. This subclass should have an additional method `fetch` that prints "Retriever is fetching!". Use this subclass to create an instance representing a retriever named Buddy who is 5 years old."""

#1
class Dog ():
    def __init__(self, name="Puppy", age = -1):
        self.name = name
        self.age = age
        
    def bark(self):
        print("woof")
        
    def birthday(self):
        self.age += 1
        
    def __str__(self):
        return (f"{self.name} is {self.age} years old")
    
class Retriever(Dog):
    def fetch(self):
        print ("Retriver is fetching")

        

if __name__ == "__main__":
    #2 
    max = Dog("Max", 10)

    max.bark()
    
    buddy = Retriever("Buddy", 5)
    
    buddy.fetch()
    
    