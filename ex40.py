# OOP basic principles

# Klasa jako "minimoduł"...


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between."

    def apple(self):
        print("I'm an apple with a class!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    

dont_look_back_in_anger = Song([
    "Slip inside the eye of your mind",
    "Don't you know you might find",
    "A better place to play",
    "You said that you'd never been",
    "But all the things that you've seen",
    "Slowly fade away",
    "So I start a revolution from my bed",
    "'Cause you said the brains I had went to my head",
    "Step outside, summertime's in bloom",
    "Stand up beside the fireplace",
    "Take that look from off your face",
    "You ain't ever gonna burn my heart out",
    "And so Sally can wait",
    "She knows it's too late",
    "As we're walking on by",
    "Her soul slides away",
    "But don't look back in anger",
    "I heard you say"])

wonderwall = Song([
    "Today is gonna be the day",
    "That they're gonna throw it back to you",
    "By now you should've somehow",
    "Realized what you gotta do",
    "I don't believe that anybody",
    "Feels the way I do about you now",
    "Backbeat, the word is on the street",
    "That the fire in your heart is out",
    "I'm sure you've heard it all before",
    "But you never really had a doubt",
    "I don't believe that anybody",
    "Feels the way I do about you now",
    "And all the roads we have to walk are winding",
    "And all the lights that lead us there are blinding",
    "There are many things that I",
    "Would like to say to you but I don't know how",
    "Because maybe",
    "You're gonna be the one that saves me",
    "And after all",
    "You're my wonderwall"])

dont_look_back_in_anger.sing_me_a_song()
print('-' * 25)
wonderwall.sing_me_a_song()
