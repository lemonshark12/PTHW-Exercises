i = int(raw_input("starting i \n>> "))
increment = int(raw_input("starting increment \n>>"))
balls = int(raw_input("How many balls do you want to have on the monkey max?\n>> "))

numbers = []

def monkey(i, balls):
    
    while i < balls:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

monkey(i, balls)

print "The numbers: "
    
for num in numbers:
        print num