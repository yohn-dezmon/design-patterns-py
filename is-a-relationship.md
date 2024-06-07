# "Is-a" relationship

- this indicates that one class is a specialized version of another class.
- when this happens, this is a good time to use inheritance 
- the subclass inherits methods and attributes from the superclass  
- specialization is when methods are overridden or new methods are added

- with interfaces, as opposed to superclasses, the methods are INTENDED to be overriden. 

# Polymorhpism 

- objects of the subclass can be treated as objects of the superclass (?)
- oh ok, like you could have an argument in a function that accepts the type of the superclass, and you can call it on any of the instantiations of the subclass (!)


```python 
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function that takes any animal and calls its speak method
def make_animal_speak(animal):
    print(animal.speak())
```
