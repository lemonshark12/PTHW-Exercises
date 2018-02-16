var = True & True
print "T, %r" % var
var = False & True
print "F, %r" % var
var = 1 == 1 or 2 !=1
print "T, %r" % var
var = True and 1 == 1
print "T, %r" % var
var = False & 0 !=0
print "F, %r" % var
var = True or 1 == 1
print "T, %r" % var
var = "test" == "testing"
print "F, %r" % var
var = 1 != 0 and 2 == 1
print "F, %r" % var
var = "test" != "testing"
print "T, %r" % var
var = "test" == 1
print "F, %r" % var
var = not (True and False)
print "T, %r" % var
var = not (1 == 1 or 1000 == 1000)
print "F, %r" % var
var = not (10 == 1 or 1000 == 1000)
print "F, %r" % var
var = not (1 != 10 or 3 == 4)
print "F, %r" % var
var = not ("testing" == "testing" and "Zed" == "Cool Guy")
print "T, %r" % var
var = 1 == 1 and not ("testing" == 1 or 1 == 0)
print "T, %r" % var
var = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print "F, %r" % var
var = 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print "F, %r" % var