class Dog:

    family = 'Canidae'

    def __init__(self, breed, name, has_spots):
        self.breed = breed
        self.name = name
        self.has_spots = has_spots

    def bark(self, number_of_times):
        '''
            This function makes a dog bark number_of_times times
        '''
        for i in range(number_of_times):
            print(f"WOOF! My name is {self.name}, my breed is {self.breed}")
        
class Circle:

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(f"The area of this circle is {Circle.pi * (self.radius ** 2)}")

    def get_perimeter(self):
        print(f"The perimeter of this circle is {2 * Circle.pi * self.radius}")

my_dog = Dog('Huskie', 'Bruno', True)
print(my_dog.breed)
print(my_dog.family)
hi = "Hello"
my_dog.bark(2)

my_circle = Circle(42)
my_circle.get_area()
my_circle.get_perimeter()