# -- coding: utf-8 --
my_name = 'Polgár Dávid'
age = 30 # not a lie
my_height = 12 * 6 + 1 # inches
weight = 200 #lbs
eyes = 'Green'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %r." % my_name
print "He's %r inches tall." % my_height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "It I add %s, %s, and %s I get %s." % (
    age, my_height, weight, age + my_height + weight)