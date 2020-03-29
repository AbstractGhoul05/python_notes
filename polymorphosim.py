class Animal():
    def __init__ (self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this Abstract Method")

class Dog(Animal):

    def speak(self):
        print(f"{self.name} says 'WOOF!'")

class Cat(Animal):

    def speak(self):
        print(f"{self.name} says 'MEOW!'")

bruno = Dog('Bruno')
bruno.speak()
felix = Cat('Felix')
felix.speak()
# myanimal = Animal('Random')
# myanimal.speak()