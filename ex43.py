from sys import exit
from random import randint


class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured.  Subclass it and implement enter()."
        exit(1)
    
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n-----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
    
class Death(Scene):
    
    quips = [
        "You died.  You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
class Finished(Scene):
    
    print "You fucking won!!  Congratulations!!"
    
class CentralCorridor(Scene):
    
    def enter(self):
        print """The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.  You are the last surviging member and your last mission is to get the neutron destruct bomb from the Weapons Armory, pit it in the bridge, and blow the sup up after getting into an escape pod."""
        print "\n"
        print " Gothon jumps out and is about to shoot you"
        
        action = raw_input(">> ")
        
        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Goton."
            print "it strengthens from your blast and defeats you."
            return 'death'
        
        elif action == "dodge":
            print "You survive for a minute but hit a wall and are eaten."
            return 'death'
            
        elif action == "tell a joke":
            print "you live."
            return 'laser_weapon_armory'
            
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
            
            
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print" here we go, pick a random number.  Odds of guessing this right are 1 in 999.  Good fucking luck!"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypak]>> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "Bzzzzed! Should have been %r" % code
            guesses += 1
            guess = raw_input("[keypad]>> ")
            
        if guess == code:
            print "fuck yeah!  That's the amount of luck for the year you get.  You've just used it all up on this sucka!"
            return 'the_bridge'
        else:
            print "The lock stays closed.  You're fucked."
            return 'death'
        
class TheBridge(Scene):
    
    def enter(self):
        print "you get to the bridge and you get attacked.  Do something!"
        action = raw_input(">> ")
        
        if action == "throw the bomb":
            print "your balls fell off"
            return 'death'
        elif action == "slowly place the bomb":
            print "You're still fucked.  your balls fell off again but you survived & got out."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
        
    
class EscapePod(Scene):
    
    def enter(self):
        print "you get to the pod and have to fucking pick a random number again to continue"
        good_pod = randint(1,5)
        print good_pod
        guess = raw_input("[pod #]>> ")
        
        
        if int(guess) != good_pod:
            print "You get into pod #%s" % guess
            print "You're fucked"
            return 'death'
        else:
            print "You get into pod#%s" % guess
            print "Hurray, you won!"
            
            return 'finished'
    

class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()