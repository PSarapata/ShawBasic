## Animal is an object
# Why is there an object in class definition? Because "Explicit is better than Implicit", as per Zen of Python.
class Animal(object):
    pass


## Dog is a class that inherits from Animal. An instance of Dog has a name
class Dog(Animal):

    def __init__(self, name):
        self.name = name


## Same as Dog
class Cat(Animal):

    def __init__(self, name):
        self.name = name


## Person is an object, it has a name and it CAN have a pet.
class Person(object):

    def __init__(self, name):
        self.name = name

        self.pet = None


## Employee is a class which inherits from Person. An instance of Employee has a name, salary, CAN have a pet.
class Employee(Person):
    
    def __init__(self, name, salary):
        ## SAME THING as super()__init__(name) <-- but "Explicit is better than Implicit"
        super(Employee, self).__init__(name)

        self.salary = salary


## Fish is an object.
class Fish(object):
    pass



## Salmon is a class that inherits from Fish.
class Salmon(Fish):
    pass



## Halibut is a class which inherits from Fish.
class Halibut(Fish):
    pass


## Rover is a Dog.
rover = Dog("Rover")

## Satan is a Cat.
satan = Cat("Satan")

## Mary is a Person.
mary = Person("Mary")

## Mary has a pet, a Cat named Satan.
mary.pet = satan

## Frank is an Employee, he has a salary of 120 000 ($)
frank = Employee("Frank", 120000)

## Frank has a pet, a Dog named Rover.
frank.pet = rover

## flipper is an instance of a Fish
flipper = Fish()

## crouse -||- of a Salmon.
crouse = Salmon()

## harry -||- of a Halibut.
harry = Halibut()
