
import blocks
import pygame
import os

class MapCell(  ):
    def __init__( self, value ):
        #print(value)
        blockdata = blocks.blocks[value]
        self.solid = blockdata["solid"]
        self.transparent = blockdata["transparent"]
        self.material = blockdata["material"]
        self.image = pygame.image.load(os.path.abspath(os.path.join("resources", "images", self.material)))
        self.damage = blockdata["damage"]
        self.health = blockdata["health"]
def LoadMapFromFile( file ):
    file = os.path.abspath(os.path.join("resources", "maps", file))
    raw = open( file ).read()
    raw = raw.split("\n") # rows - y
    data = []
    for y in range( 0, len(raw) ):
        line = []
        for x in range( 0, len(raw[y]) ):
            line.append( MapCell(raw[y][x]) )
        data.append( line )
    return Map(data)
class Map(  ):
    def __init__( self, data_array ):
        self.data = data_array
    def height( self ):
        return len(self.data)
    def width( self ):
        return len(self.data[0])
    def at( self, x, y ):
        if x < 0 or y < 0 or x > self.width or y > self.height:
            return MapCell("1")
        return self.data[y][x]