import sys, pygame, random, time

pygame.init()

BOARD_SIZE = WIDTH, HEIGHT = 640, 480
CELL_SIZE = 10
# RGB color code value for black to represnt dead cells.
DEAD_COLOR = 0, 0, 0
# RGB color code value for magenta represnt live cells.
ALIVE_COLR = 255,0,255

class LifeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.clear_screen()
        pygame.display.flip()

        self.init_grids()

    def init_grids(self):
        1:26:42
            self.num_cols = int(WIDTH / CELL_SIZE)
            self.num_rows = int(HEIGHT / CELL_SIZE)
            print('Columns: %d\nRows %d' % (self.num_cols, self.num_rows))
            self.grids = [[[0] * self.num_rows] * self.num_cols,
                          [[0] * self.num_rows] * self.num_cols]

            self.active_grid = 0
            self.set_grid()

            print(self.grids[0])
            
    #def zero_grid(self):

    def set_grid(self, value=None):
        """
        set_grid(0) # all dead
        set_grid(1) # all alive
        set_grid() # random
        set_grid(None) # random
        """
        for c in range (self.num_cols):
            for r in range(self.num_rows):
                if value is None:
                    cell_value = random.choice([0, 1])
                else:
                    cell_value = value
                self.grids[self.active_grid][c][r] = random.randint(0,1)

    def draw_grid(self):
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        for c in range (self.num_cols):
            for r in range(self.num_rows):
                if self.grids[self.active_grid][c][r] == 1:
                    color = ALIVE_COLR
                else: 
                    color = DEAD_COLOR
                pygame.draw.circle(self.screen, 
                color, 
                (int(c * CELL_SIZE + (CELL_SIZE/2)) ,                                                         
                int(r * CELL_SIZE + (CELL_SIZE/2 ))), 
                int(CELL_SIZE/2), 0)
        pygame.display.flip()

            
            

    def clear_screen(self):
        self.screen.fill(DEAD_COLOR)

    def update_generation(self):
        #Inspect the current active generation
        # update the inactive grid to store next generation
        # swap out the active grid
        self.set_grid(None)
        pass

    


    def handle_events(self):
        for event in pygame.event.get():
            # if event is the keypress of "s" toggle the game pause.
            # if event is the keypress of "r" randomize the game pause.
            # if event is the keypress of "q" quit the game pause.

            if event.type == pygame.QUIT: sys.exit()


    def run(self):
        while True:
            self.handle_events()
            self.update_generation()
            self.draw_grid()
            time.sleep(1)

          

if __name__ == '__main__':
    game = LifeGame()
    game.run()