
import blocks
import pygame

class MapCell(  ):
    def __init__( self, value ):
        blockdata = blocks.blocks[value]
        self.solid = blockdata["solid"]
        self.transparent = blockdata["transparent"]
        self.material = blockdata["material"]
        self.image = pygame.image.load(os.path.join("images", self.material))
        self.damage = blockdata["damage"]
        self.health = blockdata["health"]
def LoadMapFromFile( file ):
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
    def height():
        return len(self.data)
    def width():
        return len(self.data.first)