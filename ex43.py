# A game called "Gothans from Percal 25"

# Game could be improved by adding a choices in a tuple ((1, <do_something>),
#                                                        (2, <do_something_else))
from sys import exit
from random import randint
# This is a cool (new to me) thing, allows to print text without non-printable signs.
from textwrap import dedent


# Yeah, I know it pains to see this object, but "Explicit is better than Implicit".
class Scene(object):

    def enter(self):
        print("This scene is not configured yet!")
        print("Create a subclass and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # last scene    
        current_scene.enter()
    

class Death(Scene):

    quips = [
        "Oh no, you're dead.",
        "Whoops. You died. Sorry!",
        "Well, gotta say - you're bad at this game. Better luck next time!",
        "Nope. Dead again.",
        "Argh. You dead!",
        "Not again... >_< Dead as a corpse.",
        "Sorry bruh, you died. On a positive note - you won't get Alzheimer!"
    ]

    def enter(self):
        # print a random quip from the list
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
    

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              Gothans from Percal 25 got on your ship and murdered your crew.
              You are the sole survivor, your last mission is to obtain neutron bomb from
              laser weapon armory, place it on the bridge and blow it off once you've launched
              yourself to space in an escape pod.

              You enter the Central Corridor towards Laser Weapon Armory, but suddenly a Gothan
              with red skin and black thangs, dressed in an evil space clown suit, pops up blocking
              the way to the Armory. He is about to reach for his gun and pop you. What you gonna do?
              """))
        

        action = input('> ')

        if action == 'shoot':
            print(dedent("""
                  You reach quickly for your gun and shoot the Gothan. The clown suit waves and wraps around
                  his body and you can't aim properly. Laser beam hits his suit, but it is reflected! The new and shiny suit
                  (bought by his mum) is now stained and the Gothan is mad. He shoots your head multiple times,
                  and your corpse drops on the floor.
                  """))
            return 'death'

        elif action == 'dodge':
            print(dedent("""
                  Like a world class boxer, you dodge, move and pivot as the Gothan's laser beam cuts the air where just a second ago
                  was your head. You accidentally trip, fall on the floor and hit your head, losing consciousness as a result.
                  You then wake up just to witness happy Gothan trottling over your body, then eating your brains. Ouch.
                  """))
            return 'death'
        
        elif action == 'tell a joke':
            print(dedent("""
                  Thank God they taught you some badass jokes back in the academy, even in foreign languages!
                  You tell a joke:
                  'Przychodzi pisior do sąsiada i mówi:

                    Czy mogę panu nasrać na wycieraczkę?
                    Spadaj pajacu.
                    Na następny dzień na wycieraczce jest gówno. Gość biegnie do pisiora i mówi:
                    Osrałeś mi gnoju wycieraczkę.
                    A pisior na to:
                    Konsultacje były? Były.'

                  Gothan freezes, tries to resist, but eventually bursts with laughter.
                  You take the chance, kill him and head to the Laser Weapon Armory.
                  """))
            return 'laser_weapon_armory'

        else:
            print("NO CAN DO.")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              You jump to Laser Weapon Armory, kneel and scan the room, in search of Gothans. 
              It's awfully quiet... You get up, run towards the far end of the room, where you find
              the neuron bomb inside a locker. To take it, you will have to open the lock.
              You have 10 attempts. 
              If you fail, the lock will shut the locker forever.
              Code has 3 digits.
              """))
    
        # Standard guessing game, could be improved by adding 'too small' or 'too high'
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad] > ")
        guesses = 1

        while guess != code and guesses < 10:
            print("BZZZZZD!!!")
            guesses += 1
            guess = input("[keypad] > ")

        if guess == code:
            print(dedent("""
                  The locker opens up with a loud screeching sound.
                  You grab the neuron bomb and run as fast as you can towards the bridge,
                  where you'll have to place it in the right spot.
                  """))

            return 'the_bridge'
        
        else:
            print(dedent("""
                  You hear the buzzer again, but this time for the last time.
                  You can see characteristic blue light in the slit of the locker,
                  and realize the safety switch welded it forever. You can't do anything.
                  Gothans destroy your ship with you on board. You're dead.
                  """))

            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              You get to the bridge with neuron bomb under your armpit
              and spot 5 Gothans, trying to take control over the ship.
              All of them are wearing ugly evil clown suits.
              They see you, but are afraid to shoot because of the bomb you are holding.
              What will you do?
              """))

        action = input('> ')

        if action == 'drop the bomb':
            print(dedent("""
                         You panic and drop the bomb, diving for the door.
                         Gothans shoot you in the back, killing you.
                         In agony, you spot that one of the Gothans is trying to
                         disarm the bomb, yet has no idea what he's doing.
                         You die knowing they will most likely pay for it.
                         Rest in peace soldier."""))
            return 'dead'

        elif action == 'slowly set the bomb':
            print(dedent("""
                         You slowly walk forward, holding a gun to the bomb. Gothans are sweating.
                         They know that if they shoot, you will detonate the bomb, and you all die.
                         You place the bomb on the ground, still aiming at it with your gun.
                         As you exit the bridge, you shoot the control panel and lock the door.
                         You then immediately head to the nearest escape pod as the bomb is about to blow.
                         """))
            
            return 'escape_pod'
        
        else:
            print("CANNOT COMPUTE!")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              You run through the corridors, desperately trying to reach the pod before the ship explodes.
              It would seem there are no Gothans around, so you have a clear path.
              You reach the room. There are 5 pods, but some of them may have been damaged
              and there is no time to check.
              Which pod will you choose?
              """))

        good_pod = randint(1, 5)
        guess = input('[pod #] > ')

        if int(guess) != good_pod:
            print(dedent(f"""
                  You jump into pod# {guess} and launch. Capsule launches to space
                  and implodes. Shell breaks and fragments kill you, shattering you
                  into pieces.
                  """))

            return 'death'

        else:
            print(dedent(f"""
                  You jump into pod# {guess} and launch. Capsule launches to space
                  heading towards the nearest planet. During the flight you glance
                  behind and observe as your ship implodes and then explodes,
                  bright as a star, destroying also Gothans ship. Congratulations,
                  you won!
                  """))

        return 'finished'



class Finished(Scene):

    def enter(self):
        print("You won! Good Job!")
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
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
