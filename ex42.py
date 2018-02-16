## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    print "This is an animal..."

## class dog is-a animal
class Dog(Animal):
    
    print "...specifically a dog."
    def __init__(self, name):
       ## class dog has an __init__ that takes self and name parameters
        self.name = name
        
## class cat is-a animal
class Cat(Animal):
    print "...or a cat."
    def __init__(self, name):
        ## class cat has-a function __init__ that takes self and name as parameters
        self.name = name
        
## class person is-a object
class Person(object):
    
    print "People also exist, we call them \'Person\' "
    def __init__(self, name):
        ## class person has a __init__ that takes self and name as parameters
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None
        
## class employee is-a person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## class employee has an __init__ that takes self, name, and salary parameters
        ##hmm what is this strange magic?
        super(Employee, self) .__init__(name)
        ## class employee has-a salary attribute
        self.salary = salary
        
## make class fish that is-a object
class Fish(object):
    pass

## make class salmon that is-a fish
class Salmon(Fish):
    pass

## make class halibut that is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## set satan as an instance of class cat 
satan = Cat("Satan")

## set mary as an istance of class person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan
mary.pet = satan

## set frank as an instance of class employee with parameters self="Frank" and salary=120000 
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover
print "Frank has a dog named Rover"

#frank.pet = satan
print "Frank has a cat named Satan"

frank.pet = "mary"

print "Frank has a dog named Rover"


test_bullshit = raw_input(">> ")

def give_frank_a_cat():
    
    frank.pet = test_bullshit
    print frank.pet
    frank.pet = "satan"
    print frank.pet
    frank.pet = "balls"
    print frank.pet

give_frank_a_cat()

## make flipper an instance of class fish
flipper = Fish()

## make course an instance of class salmon
crouse = Salmon()

## make harry an instance of class halibut
harry = Halibut()