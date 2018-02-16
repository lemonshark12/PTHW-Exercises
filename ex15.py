# initiates the argv module
from sys import argv
# sets the variables for argv, namely the name of the script to use as well as the variable called "filename"
script, filename = argv
# sets "txt" as a variable that performs the function of open() on the previously defined filename by the user in the initial commant line
txt = open(filename)
# gives user the sentence below, including the initially user-defined filename
print "Here's your file %r:" % filename
# gives user the contents of the file initially designated in the command line after opening it as defined by the function that the "txt" variable is set to perform
print txt.read()

## readline(number of characters to read goes in here)
## readlines()  --> this gives the whole file without formatting, just with \n for signaling new lines.  All as one long string as output though


# gives the user the prompt below, then requests user to input answer
print "Tyep the filename again:"
# sets "file_again" as a variable defined by the user through keyboard input
file_again = raw_input("> ")
# sets "txt_again" as a variable that performs the open() function on the the previously user inputted content from line directly above
txt_again = open(file_again)
# gives user the contents of the "txt_again" variable, which is a file that is opened by the function defined by the "txt_again" variable and is user inputted above
print txt_again.read()
txt.close()
txt_again.close()