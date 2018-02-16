#import os
import random


word_bank = open("word_bank.txt", mode = "r")
to_print = word_bank.readlines()
j = random.randint(0,len(to_print)-1)
solution = to_print[j]
spliced_solution =[]
guesses = []
progress = []
status = 0 #not-won-yet (1=won)

def keep_track():
    for i in solution:
        spliced_solution.append(i)
    spliced_solution.pop()
  #  print spliced_solution[:-1:]
    print spliced_solution

def setup():
    print 'keeping track'
    keep_track()
    progress.append(len(spliced_solution)*"__ ")
    print progress[0]
    play()
    
def play():
    while status != 1:
        guess = raw_input("?")
        if guess == "quit":
            break
        elif guess == "check":
            print spliced_solution
            continue
        elif guess in spliced_solution:
            print "fuck yeah!"
            continue
        print "playing"
        #play()
    else:
        print "you won!"
        win()

def win():
    pass

setup()