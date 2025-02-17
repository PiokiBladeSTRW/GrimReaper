class soundManager:
    import os
    import pygame.mixer as mix
    import threading
    import json
    import random

    soundData_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)) , '../../assets/Values/sounds.json')
    
    with open(soundData_path, 'r') as SND:
        soundData = json.load(SND)
    
    prefix = os.path.join(os.path.dirname(os.path.abspath(__file__)) ,"../../assets/sounds/"  )
    suffix = ".ogg"  
    soundPath1 = soundPath2= None

    mix.init()

    sound1 = sound2 = mix.Sound(prefix+'wind'+suffix)    

    def __init__(self, currentLocation):
        self.cL = currentLocation
        self.amb = 0
        
        self.startTimer()
    
    def playSong(self, amb):
        if(not self.sound1.get_num_channels()):
            soundList = self.soundData[self.cL]["atm"]
            self.soundPath1 = self.prefix + soundList[self.random.randint(0, len(soundList)-1)] + self.suffix

            self.sound1 = self.mix.Sound(self.soundPath1)
            self.sound1.play(loops=3)

        if(not self.sound2.get_num_channels() and amb):
            soundList = self.soundData[self.cL]["amb"]
            self.soundPath2 = self.prefix + soundList[self.random.randint(0, len(soundList)-1)] + self.suffix

            self.sound2 = self.mix.Sound(self.soundPath2)
            self.sound2.play(loops=1)
        
        print("Hallo")

        self.startTimer()

    def fadeOutSong(self):
        if(self.sound1.get_num_channels()):
            soundList = self.soundData[self.cL]["atm"]
            soundName = self.soundPath1.split(self.prefix)[1][:-4]
            if(soundName not in soundList):
                self.sound1.fadeout(10000)
            
        if(self.sound2.get_num_channels()):
            soundList = self.soundData[self.cL]["amb"]
            soundName = self.soundPath2.split(self.prefix)[1][:-4]
            if(soundName not in soundList):
                self.sound2.fadeout(5000)           
        

    def startTimer(self):
        self.amb = self.amb ^ 1
        self.timer = self.threading.Timer(60, self.playSong, args=(self.amb,))
        self.timer.start()