# -*- coding: utf-8 -*-

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                      "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])

boci_boci_tarka = Song(["Boci boci tarka",
                       "Se füle se farka",
                       "Oda megyünk lakni",
                       "Ahol tejet kapni!"])

balls = Song(["Balls balls bills bills bulls bulls bulls bowls"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

boci_boci_tarka.sing_me_a_song()

balls.sing_me_a_song()