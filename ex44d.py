## makes class Parent that is-a object
class Parent(object):
## makes function override that takes self as parameter
    def override(self):
        print "PARENT override()"
## makes function implicit that takes self as parameter   
    def implicit(self):
        print "PARENT implicit()"
## makes function altered that takes self as parameter   
    def altered(self):
        print "PARENT altered()"
## make class child that is-a Parent       
class Child(Parent):
## make function override for child that is unique to metaclass Parent    
    def override(self):
        print "CHILD override()"
## make function altered that is initially unique to class child but then runs Parent.altered and then continues with its own child code afterwards       
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
        
dad = Parent()
son = Child ()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()