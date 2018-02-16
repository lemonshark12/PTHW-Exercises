from sys import argv

script, data_file = argv

data = open(data_file, 'r')
print data.read(5)


data = open(data_file, 'a+')

#go_to = (raw_input("X, Y, Z -coordinates\n>> "))

x_pos = int(raw_input("X-coordinate\n>> "))
y_pos = int(raw_input("Y-coordinate\n>> "))
z_pos = int(raw_input("Z-coordinate\n>> "))

go_to = "%r, %r, %r\n" % (x_pos, y_pos, z_pos)
data.write(go_to)