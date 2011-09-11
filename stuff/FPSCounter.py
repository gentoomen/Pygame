
import pygame
import time

class FPSCounter:
    def __init__(self, game):
        self.current = 0
        self.game = game
        self.font_size = 25
        self.font = pygame.font.Font(None, self.font_size)
        self.last_time = time.time()
    def update_draw(self, x, y):
    	if not time.time() - self.last_time > 1:
        	return
        pygame.draw.rect(self.game.screen, (128, 128, 128), (x - 5, y - 5, ((len("FPS: " + str(self.current))) / 2 * self.font_size), self.font_size)) # not the best way to to this, I know...
        self.last_time = time.time()
        text = self.font.render('FPS: %d' % (self.current), True, (0, 0, 0))
        textrect = text.get_rect()
        textrect.x = x
        textrect.y = y
        self.game.screen.blit(text, textrect)
        self.current = 0
    def update_fps_count(self):
        self.current += 1
