import pygame
import game
import frogger

TITLE = "Frogger"
CELL_SIZE = 50
ROWS = 11
COLUMNS = 19
WINDOW_WIDTH  = COLUMNS*CELL_SIZE
WINDOW_HEIGHT = ROWS*CELL_SIZE
DESIRED_RATE  = 30

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):
        super().__init__( title, width, height, frame_rate )
        self.game = frogger.Frogger( width, height, CELL_SIZE, ROWS, COLUMNS )
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        if pygame.K_UP in newkeys:
            self.game.up()
        if pygame.K_DOWN in newkeys:
            self.game.down()
        if pygame.K_LEFT in newkeys:
            self.game.left()
        if pygame.K_RIGHT in newkeys:
            self.game.right()
        self.game.evolve( dt )
    

    def paint( self, surface ):
        self.game.draw( surface )

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
