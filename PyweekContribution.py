
import pygame
from pygame.locals import * # only needed for the 'QUIT' constant
from resources import *

class PyweekContribution:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([400, 300])
        pygame.display.set_caption("pyweek contribution")
        self.running = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        # set up map here or wut
        self.current_map = maploading.LoadMapFromFile("test")
        self.camera = camera.Camera(self.current_map.width, self.current_map.height, 400, 300)
        # load player here... I guess...
        # self.player = 
    def cls(self):
        self.screen.fill((255,255,255))
    def update_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
    def update_draw(self):
        # self.cls() # cls
        # self.screen.blit(derp, (x, y)) # draw stuff
        
        # draw background of map
        
        # draw foreground of map (tiles)
        cam_x, cam_y = self.camera.calculate_position(50, 50) # set up player position here
        #print(cam_x, cam_y)
        for y in range(0, self.current_map.height()):
            for x in range(0, self.current_map.width()):
                #print((x * 32 - cam_x, y * 32 - cam_y))
                self.screen.blit(self.current_map.at(x, y).image, (x * 32 - cam_x, y * 32 - cam_y))
        # draw entities (items, enemies)
        
        # draw character
        
        
        pygame.display.flip()
    def update_clock(self):
        self.clock.tick(self.fps)

if __name__ == '__main__':
    game = PyweekContribution()
    
    game.cls()
    
    while game.running:
        game.update_draw()
        game.update_clock()
        game.update_input()
