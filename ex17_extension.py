from sys import argv

script, old_file, copy_file, copy_file2 = argv

begin = open(copy_file, 'w')
begin.write(old_file)
begin2 = open(copy_file2, 'w')
begin2.write(old_file)
print "fuck yeah, it's done!"
begin.close()
begin2.close()