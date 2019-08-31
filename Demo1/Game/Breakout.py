import Ball, Highscore, Level, Pad
from Level import *
from Highscore import *
from Pad import *
from Ball import *
from Shared import GameConstants
from Scenes import *

import pygame

class Breakout:
    def __init__(self):
        self.__lives = 5
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((0,0),0)
        self.__balls = [
            Ball((0,0), 0, self)
        ]
        pygame.init()
        # pygame.mixer.init()
        pygame.display.set_caption("Game programming with Python & Pygame")
        self.__clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE
                                                , pygame.DOUBLEBUF
                                                , 32)
        pygame.mouse.set_visible(False)

        self.__scenes = (
            PlayingGameScene(self),
            MenuScene(self),
            GameOverScene(self),
            HighscoreScene(self)
        )

        self.__currentScene = 0
        self.__sounds = ()

    def start(self):
        while True:
            self.__clock.tick(100)
            self.screen.fill((0,0,0))
            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()
    
    def changeScene(self, scene):
        pass
    
    def getLevel(self):
        pass
    
    def getScore(self):
        pass
    
    def increaseScore(self, score):
        pass
    
    def getLives(self):
        pass
    
    def getBalls(self):
        pass
    
    def getPad(self):
        pass
    
    def playSound(self, soundClip):
        pass
    
    def reduceLives(self):
        pass
    
    def increaseLives(self):
        pass
    
    def reset(self):
        pass

game = Breakout()

game.start()