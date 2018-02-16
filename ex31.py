print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese care.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear%2 != TypeError:
            print "this was an integer"
    
    elif bear%2 == TypeError:
            print "this was not an integer"
    
    
    if bear in range(0,99) and bear != 2:
        print "The bear eats your face off.  Good job!"
    elif bear == 2:
        print "The bear eats your legs off Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear
    
    
elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1.  Blueberries."
    print "2.  Yellow jacket clothepins."
    print "3.  Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
        
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"
        
else:
    print "You stumble around and fall on a kinfe and die  Good job!"