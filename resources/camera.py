#
# When creating a camera you need to specify the map's width and height and the
# screen's width and height.
#
# When you want to calculate the offset of everything call calculate_position()
# with the player/character's x and y coordinates and it returns the camera's
# coordinates. To use those the best idea (probably) is to subtract them from
# whatever coordinates you already have. Kinda like this:
#
# cam = Camera( map_width, map_height, screen_width, screen_height )
# camera_x, camera_y = cam.calculate_position( player_x, player_y )
# screen.blit( tile_x - camera_x, tile_y - camera_y )
#
# TODOs:
#
# - When the map is smaller than the screen, the map gets drawn on the
# top-left corner without any nice padding. I'm thinking of positioning the
# camera on the center of the map in this case.
#
class Camera(  ):
    def __init__( self, map_width, map_height, screen_width, screen_height, tile_size = 32 ):
    	self.mw, self.mh = map_width, map_height
        self.sw, self.sh = screen_width, screen_height
        self.ts = tile_size
    def calculate_position( self, player_x, player_y ):
    	# center camera on player
    	x, y = player_x - self.sw / 2, player_y - self.sh / 2
        if x < 0:
        	# lock left side
        	x = 0
        elif x > ( self.mw * self.ts ) - ( self.sw ):
        	# lock right side
        	x = ( self.mw * self.ts ) - ( self.sw )
        if y < 0:
        	# lock top
        	y = 0
        elif x > ( self.mh * self.ts ) - ( self.sh ):
        	# lock bottom
        	y = ( self.mh * self.ts ) - ( self.sh )
        return( x, y )