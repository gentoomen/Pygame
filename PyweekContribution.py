
import pygame
from pygame.locals import * # only needed for the 'QUIT' constant
from stuff import *

class PyweekContribution:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([400, 300])
        pygame.display.set_caption("pyweek contribution")
        self.running = True
        self.fps = 60
        self.clock = pygame.time.Clock()
    def cls(self):
    	self.screen.fill((255,255,255))
    def update_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
    def update_draw(self):
        # self.cls() # cls
        # self.screen.blit(derp, (x, y))
        pygame.display.flip() # draw stuff
    def update_clock(self):
        self.clock.tick(self.fps)

if __name__ == '__main__':
    game = PyweekContribution()
    fpscounter = FPSCounter.FPSCounter(game)
    
    game.cls()
    
    while game.running:
        fpscounter.update_draw(50, 50)
        game.update_draw()
        game.update_clock()
        game.update_input()
        fpscounter.update_fps_count()
