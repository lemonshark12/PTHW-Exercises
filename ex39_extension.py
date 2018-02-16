robot_parts = {
    'sensors': 'digital',
    'pressure based': 'pneumatic',
    'electrical': 'power distribution'
}

robot_functionalities = {
    'digital': 'read HIGH or LOW',
    'analog': 'read any value',
    'preumatic': 'actuators based on air',
    'power distribution': 'vary voltage & current to suit task'
}

print '-' *10
print "The parts of robots are: %s" % robot_parts

print "These parts can accomplish several tasks.  The %s can for instance %s, and the %s can %s" % (robot_parts['electrical'], robot_functionalities['power distribution'], robot_parts['sensors'], robot_functionalities['digital'])