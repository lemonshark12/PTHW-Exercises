from sys import exit
import random

gender_list = ['boy', 'girl']
ethnicity_list = ['white', 'black', 'asian', 'hispanic']
adopted_list = ['adopted', 'not adopted']
years = 8

gender = random.choice(gender_list)
ethnicity = random.choice(ethnicity_list)
adopted_actual =random.choice(adopted_list)

def birth(ethnicity):
    print "Welcome to life!  You are a(n) %s %s." % (ethnicity, gender)
    if gender == gender_list[1] and ethnicity == ethnicity_list[1]:
        print "Damn, nigga, you're shit outta luck this time!"
    print "Now let\'s see where you're living..."
    adopted_guess = raw_input("...but first, do you think you were adopted?\nPick either 'adopted' or 'not adopted'\n>> ")
    if adopted_guess == adopted_actual and adopted_actual == adopted_list[0]:
        print "\nYou're right, you were loved and not adopted."
        print "Since you got this one right, you have a special opporunity..."
        god_mode()
    elif adopted_guess == adopted_actual and adopted_actual != adopted_list[0]:
        print """\nYou're right, you were not loved and were left on the curb by the dumpster.  It's a miracle that you survived this long."""
        education(years)
    elif adopted_guess != adopted_actual and adopted_actual == adopted_list[0]:
        print "\nYou're a dumbass.  You were loved and not adopted you unappreciateive little shit."
        education(years)
    else:
        print "\nFuck this, let's move on from this topic."
        education(years)

def education(years):
    education_choice = raw_input("\nYou got older. Do you want to go to college?\n>> ")
    if education_choice == "yes":
        print "Since you are a %s %s, it will take you %d years to finish college" % (ethnicity, gender, years)
    
def god_mode():
    god_choice = raw_input("would you like to change your  ethnicity?\n>> ")
    if god_choice == "ethnicity":
        print "Your choices are:"
        print ethnicity_list
        ethnicity_change = raw_input("pick one\n>> ")
        ethnicity = ethnicity_change
        birth(ethnicity)

birth(ethnicity)