#
# When initializing a camera you need 3 data containers, one for the players
# x, y coordinates, one for the map width and height and one for the screen aka
# window width and height. E.g. classes like these:
#
#    class ScreenData(  ):
#        def __init__( self, w, h ):
#            self.width, self.height = w, h
#    class PlayerData(  ):
#        def __init__( self, x, y ):
#            self.x, self.y = x, y
#    class MapData(  ):
#        def __init__( self, w, h ):
#            self.width, self.height = w, h
#
class Camera(  ):
    def __init__( self, player, map, screen ):
        self.player = player
        self.map = map
        self.screen = screen
        self.x, self.y = self.player.x, self.player.y
    def calculate_position( self ):
    	if ( self.map.width <= self.screen.width and self.map.height <= self.screen.height ):
    	    return (0, 0)
        if (
             ( self.player.x - ( self.screen.width / 2 ) > 0 ) and
            ( self.player.x + ( self.screen.width / 2 ) < self.map.width) ):
            self.x = self.player.x - ( self.screen.width / 2 )
        elif (
            ( self.player.y - ( self.screen.height / 2 ) > 0 ) and
            ( self.player.y + ( self.screen.height / 2 ) < self.map.height ) ):
            self.y = self.player.y - ( self.screen.height / 2 )
        return (self.x, self.y)
    def view( self ):
        self.x, self.y = self.calculate_position(  )
if ( __name__ == '__main__' ):
    # Load dependencies
    import pygame
    pygame.init()    
    # Define data containers
    class ScreenData(  ):
        def __init__( self, w, h ):
            self.width, self.height = w, h
    class PlayerData(  ):
        def __init__( self, x, y ):
            self.x, self.y = x, y
    class MapData(  ):
        def __init__( self, w, h ):
            self.width, self.height = w, h
    # Set up everything
    Screen  = ScreenData( 300, 300 )
    Player  = PlayerData( 50, 50 )
    MapInfo = MapData( 150, 150 )
    Viewer  = Camera( Player, MapInfo, Screen )
    pygame.display.set_mode(( Screen.width, Screen.height ))
    surface = pygame.display.get_surface()
    clock   = pygame.time.Clock()
    # Run game loop
    while True:
        # Input & Move
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[ pygame.K_LEFT ]:
            if Player.x - 1 >= 0:
                Player.x -= 1
        if key[ pygame.K_RIGHT ]:
            if ( Player.x + 1 <= MapInfo.width ):
                Player.x += 1
        if key[ pygame.K_UP ]:
            if Player.y - 1 >= 0:
                Player.y -= 1
        if key[ pygame.K_DOWN ]:
            if ( Player.y + 1 <= MapInfo.height ):
                Player.y += 1
        # Draw
        surface.fill((0,0,0)) # cls
        # TODO draw white background for map-only-parts
        for x in range(-1,2):
            for y in range(-1,2):
                surface.set_at( ( Player.x - Viewer.x + x, Player.y - Viewer.y + y ), ( 255, 0, 0 ) )
        print ( Player.x - Viewer.x + x, Player.y - Viewer.y + y )
        pygame.display.flip()
        # Relocate camera
        Viewer.view()
        # Time
        clock.tick(60)