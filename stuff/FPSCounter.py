
import pygame
import time

class FPSCounter:
    def __init__(self, game):
        self.current = 0
        self.game = game
        self.font = pygame.font.Font(None, 25)
        self.last_time = time.time()
    def update_draw(self, x, y):
    	self.game.cls()
        self.last_time = time.time()
        text = self.font.render('FPS: %d' % (self.current), True, (0, 0, 0))
        textrect = text.get_rect()
        self.game.screen.blit(text, textrect)
        self.current = 0
    def update_fps_count(self):
        self.current += 1
