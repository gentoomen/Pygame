
import pygame.mixer
import os

pygame.mixer.init()

def loadsound(path):
    path += ".ogg"
    path = os.path.join("sounds", path)
    path = os.path.abspath(path)
    return pygame.mixer.Sound(path)

print (loadsound("boom1"))