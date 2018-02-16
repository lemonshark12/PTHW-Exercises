def zorking(balls, bills):
    print "this is zorking"
    return balls + bills

def zirking(balls, bills):
    print "this is zirking"
    return balls - bills

def zurking(balls, bills):
    print "this is zurking"
    return balls * bills

def zuurking(balls, bills):
    print "this is zuurking"
    return balls / bills

balls = int(raw_input("Give me the number of your balls\n>>"))
bills = int(raw_input("Give me the number of your bills\n>>"))

zork = zorking(balls, bills)
zirk = zirking(balls, bills)
zurk = zurking(balls, bills)
zuurk = zuurking(balls, bills)

choice = raw_input("What would you like to do with your balls and bills?\n>>")
if choice == "zork":
    print "if you zork-it, it's:\n %d" % zork
else:
    print "fuck off"