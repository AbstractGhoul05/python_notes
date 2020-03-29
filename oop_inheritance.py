class Animal:
     
    def __init__(self):
        print("ANIMAL CREATED")

    def eat(self):
        '''
            This is a function for the animal to eat
        '''
        print("I am eating")

    def who_am_i(self):
        print("I am an animal")

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        '''
            This is a function for telling what the object is
        '''
        print("I am a dog")

    def bark(self, number):
        '''
            This is a function for barking n times
        '''
        for i in range(number):
            print("WOOF!")

    def eat(self):
        print("I am a dog and I'm eating")

my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()