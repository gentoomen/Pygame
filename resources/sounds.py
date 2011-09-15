
import pygame.mixer
import os

pygame.mixer.init()

def loadsound(path):
    path += ".ogg"
    path = os.path.join("sounds", path)
    path = os.path.abspath(path)
    return pygame.mixer.Sound(path)

sounds = {}

# now we can do:
# 
# import random
# random.choice(sounds["boom"]).play()
# NOTE: maybe automate this process
sounds["boom"] = []
sounds["boom"].append(loadsound("boom1"))
sounds["boom"].append(loadsound("boom2"))
sounds["boom"].append(loadsound("boom3"))
sounds["boom"].append(loadsound("boom4"))

sounds["coin"] = []
sounds["coin"].append(loadsound("coin1"))
sounds["coin"].append(loadsound("coin2"))
sounds["coin"].append(loadsound("coin2"))

sounds["hit"] = []
sounds["hit"].append(loadsound("hit1"))
sounds["hit"].append(loadsound("hit2"))

sounds["jump"] = []
sounds["jump"].append(loadsound("jump1"))
sounds["jump"].append(loadsound("jump2"))

sounds["pew"] = []
sounds["pew"].append(loadsound("pew1"))
sounds["pew"].append(loadsound("pew2"))
sounds["pew"].append(loadsound("pew3"))

sounds["select"] = []
sounds["select"].append(loadsound("select1"))
sounds["select"].append(loadsound("select2"))
