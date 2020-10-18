"""
Module: Snake
Title: snake1.py

Authors:
Thomas Padova - tpadova@sandiego.edu
Quinn Bigane - qbigane@sandiego.edu

Date:
5/8/2020

Iteration 7: Fill in the event handlers. See Iteration 
6 of the life program for examples of this. The handlers 
will be in the Snake class - that is, the controller. As 
in the game of life, these handlers will talk to both the 
model and the view.

This is the final version of the program. You can validate 
it by playing the game and interacting with it in various ways.
"""
import random
import tkinter as tk
from tkinter.font import Font
from enum import Enum
import time

class Snake:
    """ This is the controller """
    def __init__(self):
        """ Initializes the snake game """
        # Define parameters
        #define architecture parameters
        self.NUM_ROWS = 30
        self.NUM_COLS = 30
        #define gamestate variables
        self.game_state = GameState
        self.game_state.STARTUP
        
        #define time related parameters
        self.time1 = 0.000
        self.time2 = 0.000
        self.DEFAULT_TIME_STEP = 1000
        self.step_time = self.DEFAULT_TIME_STEP
        
        # Create Snake view
        self.view = SnakeView(self.NUM_ROWS, self.NUM_COLS)
        #Create Snake model
        self.model = SnakeModel(self.NUM_ROWS, self.NUM_COLS)

        # Set up the control panel buttons (bind buttons to handlers)
        # Start
        self.view.set_start_handler(self.start_handler)
        # Pause
        self.view.set_pause_handler(self.pause_handler)
        #Step Speed
        self.view.set_step_slider_handler(self.step_speed_handler)
        # Reset 
        self.view.set_reset_handler(self.reset_handler)
        # Quit
        self.view.set_quit_handler(self.quit_handler)
        # Wraparound
        self.view.set_wraparound_handler(self.wraparound_handler)
        

        #set up arrows (bind arrow key presses to appropriate handlers)
        #set the left click
        def left_handler(event):
            """connect left arrow key to left arrow key handler"""
            self.left_click_handler()
        self.view.set_left_click_handler(left_handler)
        #Set the right click
        def right_handler(event):
            """connect right arrow key to right arrow key handler"""
            self.right_click_handler()
        self.view.set_right_click_handler(right_handler)
        #Set the up click
        def up_handler(event):
            """connect up arrow key to up arrow key handler"""
            self.up_click_handler()
        self.view.set_up_click_handler(up_handler)
        #Set the down click
        def down_handler(event):
            """connect down arrow key to down arrow key handler"""
            self.down_click_handler()
        self.view.set_down_click_handler(down_handler)
        
        
        # Start the simulation
        self.view.window.mainloop()


    def left_click_handler(self):
        """ if left arrow press occurs change direction to west """
        self.model.direction = Direction.WEST
    def right_click_handler(self):
        """ if right arrow press occurs change direction to east """
        self.model.direction = Direction.EAST
    def up_click_handler(self):
        """ if up arrow press occurs change direction to north """
        self.model.direction = Direction.NORTH
    def down_click_handler(self):
        """ if down arrow press occurs change direction to south """
        self.model.direction = Direction.SOUTH
    def start_handler(self):
        """ Start simulation  """
        # if self.game_state == GameState.STARTUP:
        self.view.one_step(self.step_time, self.continue_sim)
        self.time1 = time.time()
    def pause_handler(self):
        """ Pause simulation """
        if self.game_state == GameState.RUNNING or GameState.RUNNINGWRAP:
            self.view.stop_next_step()
            self.game_state.PAUSED
        

    def reset_handler(self):
        """ Reset simulation """
        self.step_time = self.DEFAULT_TIME_STEP // self.view.step_speed_slider.get()
        self.view.reset()
        self.model.__init__(self.NUM_ROWS,self.NUM_COLS)


    def quit_handler(self):
        """ Quit life program """
        self.view.window.destroy()

    def step_speed_handler(self, value):
        """ Adjust simulation speed"""
        self.step_time = (self.DEFAULT_TIME_STEP // int(value))
    def wraparound_handler(self):
        """Turn on and off wraparound"""
        pass

    def continue_sim(self):
        """ Keep the simulation running """
        self.one_step()
        self.view.one_step(self.step_time, self.continue_sim)
    
    def one_step(self):
        """ Advance the simulation by one timestep """
        #update the model
        (snake,food, game_over, points) = self.model.one_step(self.view.wraparound.get())
        #get current time
        now = time.time()
        #calculate elapsed time
        elapsed = round((now - self.time1), 2)
        self.time1 = now
        #update the view
        self.view.update_scoreboard(points, game_over, elapsed)
        #if the game has not ended
        if not game_over:
            #for every cell
            for r in range(self.NUM_ROWS):
                for c in range(self.NUM_COLS):
                    cell = (r,c)
                    #if that cell is a snake, make black
                    if snake[0] == cell:
                        self.view.make_black(cell[0],cell[1])
                    #if that cell is the head of the snake, make blue
                    elif cell in snake[1:]:
                        self.view.make_blue(cell[0],cell[1])
                    #if that cell is the food, make red
                    elif cell == food:
                        self.view.make_red(cell[0],cell[1])
                    #otherwise, make the cell white
                    else: 
                        self.view.make_white(cell[0],cell[1])
class SnakeView:
    def __init__(self, num_rows, num_cols):
        """ Initialize view of the game """
        # Constants
        self.game_over_label = None
        self.CELL_SIZE = 20
        self.CONTROL_FRAME_HEIGHT = 100
        self.SCORE_FRAME_WIDTH = 200
        # Size of grid
        self.num_rows = num_rows
        self.num_cols = num_cols

        # Create window
        self.window = tk.Tk()
        self.window.title("Game of Life")

        # Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(self.window, height = num_rows * self.CELL_SIZE,
                                width = num_cols * self.CELL_SIZE)
        self.grid_frame.grid(row = 1, column = 1)
        self.cells = self.add_cells()

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = (self.num_cols * self.CELL_SIZE) + self.SCORE_FRAME_WIDTH, 
                                height = self.CONTROL_FRAME_HEIGHT, borderwidth = 1, relief = 'solid')
        self.control_frame.grid(row = 2, column = 1, columnspan = 2)
        self.control_frame.grid_propagate(False)
        (self.start_button, self.pause_button, self.step_speed_slider, 
         self.reset_button, self.quit_button, self.wraparound_button) = self.add_control()

        # Create frame for score
        self.score_frame = tk.Frame(self.window, width = self.SCORE_FRAME_WIDTH, height = self.num_rows * self.CELL_SIZE, borderwidth = 1, relief = 'solid')
        self.score_frame.grid(row = 1, column = 2) # use grid layout manager 
        self.score_frame.grid_propagate(False)
        (self.score_label, self.points_frame, self.points_label, self.time_frame, self.time_label, self.pointspersec_frame, self.pointspersec_label) = self.add_scoreboard()
    def set_left_click_handler(self, handler):
        """ set handler for pressing left arrow to the function handler """
        self.window.bind('<Left>', handler)

    def set_right_click_handler(self, handler):
        """ set handler for pressing right arrow to the function handler """
        self.window.bind('<Right>', handler)

    def set_up_click_handler(self, handler):
        """ set handler for pressing up arrow to the function handler """
        self.window.bind('<Up>', handler)


    def set_down_click_handler(self, handler):
        """ set handler for pressing down arrow to the function handler """
        self.window.bind('<Down>', handler)
        
    def set_start_handler(self, handler):
        """ set handler for clicking on start button to the function handler """
        self.start_button.configure(command = handler)

    def set_pause_handler(self, handler):
        """ set handler for clicking on pause button to the function handler """
        self.pause_button.configure(command = handler)

    def set_reset_handler(self, handler):
        """ set handler for clicking on reset button to the function handler """
        self.reset_button.configure(command = handler)

    def set_quit_handler(self, handler):
        """ set handler for clicking on quit button to the function handler """
        self.quit_button.configure(command = handler)

    def set_step_slider_handler(self, handler):
        """ set handler for dragging the step speed slider to the function handler """
        self.step_speed_slider.configure(command = handler)

    def set_wraparound_handler(self,handler):
        """ set handler for checking the wraparound box"""
        self.wraparound_button.configure(command = handler)

    def add_cells(self):
        """ Add cells to the view """
        cells = []
        #for every row
        for r in range(self.num_rows):
            row = []
            #for every column
            for c in range(self.num_cols):
                #create a frame to represent every cell
                frame = tk.Frame(self.grid_frame, width = self.CELL_SIZE, 
                         height = self.CELL_SIZE, borderwidth = 1, 
                         relief = "solid")
                #grid that frame to its respective row and coloumn
                frame.grid(row = r, column = c)
                row.append(frame)
            cells.append(row)
        return cells

    def add_control(self):
        """ 
        Create control buttons and slider, and add them to the control frame 
        """
        control_panel_padx = ((self.num_cols * self.CELL_SIZE) + self.SCORE_FRAME_WIDTH)/27 #20 --> 27
        #create and grid the start button
        start_button = tk.Button(self.control_frame, text="Start")
        start_button.grid(row=1, column=1, padx=control_panel_padx)
        #create and grid the pause button
        pause_button = tk.Button(self.control_frame, text="Pause")
        pause_button.grid(row=1, column=2, padx=control_panel_padx)
        #create and grid the step speed slider
        step_speed_slider = tk.Scale(self.control_frame, from_=1, to=10, 
                    label="Step Speed", showvalue=0, orient=tk.HORIZONTAL)
        step_speed_slider.grid(row=1, column=3, padx=control_panel_padx)
        #create and grid the reset button
        reset_button = tk.Button(self.control_frame, text="Reset")
        reset_button.grid(row=1, column=4, padx=control_panel_padx)
        #create and grid the quit button
        quit_button = tk.Button(self.control_frame, text="Quit")
        quit_button.grid(row=1, column=5, padx=control_panel_padx)

        # use a tk.BooleanVar to keep track of whether or not the game is in wraparound mode
        self.wraparound = tk.BooleanVar()
        self.wraparound.set(False)
        wraparound_button = tk.Checkbutton(self.control_frame,text="Wraparound", var=self.wraparound) 
        wraparound_button.grid(row =1, column=6, padx=control_panel_padx)
        # Vertically center the controls in the control frame
        self.control_frame.grid_rowconfigure(1, weight = 1) 

        # Horizontally center the controls in the control frame
        self.control_frame.grid_columnconfigure(0, weight = 1)
        self.control_frame.grid_columnconfigure(7, weight = 1)                                                    
        return (start_button, pause_button, step_speed_slider, 
                reset_button, quit_button, wraparound_button)
    
    def init_scoreboard_vars(self):
        """Create all variables for the scoreboard"""
        #points variables
        self.points = tk.StringVar()
        self.points.set("Points: 0")
        #time variables
        self.total_time = 0
        self.time = tk.StringVar()
        self.time.set("Time: 0.00")
        #points per second variables
        self.pps = tk.StringVar()
        self.pps.set("Points per sec: 0.00")
        #game over variables
        self.game_over = tk.StringVar()
        self.game_over.set("")
        
    def add_scoreboard(self):
        """ 
        Create control buttons and slider, and add them to the control frame 
        """
        self.init_scoreboard_vars()
        # create score title
        score_label = tk.Label(self.score_frame, text="Score")
        score_label.grid(row=1, column=1,pady=15)
        # create points frame / label - initialize points to display as 0
        points_frame = tk.Frame(self.score_frame, borderwidth = 1, width = 20, height = 20, relief = "solid")
        points_frame.grid(row=2, column=1,pady=15)
        points_label = tk.Label(points_frame, text = "Points: ", textvariable = str(self.points))
        points_label.grid(row = 1, column = 1)
        # create time frame / label - initialize time to 0.00
        time_frame = tk.Frame(self.score_frame, borderwidth = 1, width = 20, height = 20, relief = "solid")
        time_frame.grid(row=3, column=1,pady=15)
        time_label = tk.Label(time_frame, textvariable = self.time)
        time_label.grid(row = 1, column = 1)
        # create points per second frame / label - initialize points per second to 0.00
        pointspersec_frame = tk.Frame(self.score_frame, borderwidth = 1, width = 20, height = 20, relief = "solid")
        pointspersec_frame.grid(row=4, column=1,pady=15)
        pointspersec_label = tk.Label(pointspersec_frame, textvariable = self.pps)
        pointspersec_label.grid(row = 1, column = 1)
        # create game_over label - initialize to the empty string
        game_over_label = tk.Label(self.score_frame, textvariable= self.game_over)
        game_over_label.grid(row=5, column=1,pady=15)
        # Vertically center the controls in the control frame
        self.score_frame.grid_rowconfigure(0, weight = 0) 
        self.score_frame.grid_rowconfigure(6, weight = 1)
        # Horizontally center the controls in the control frame
        self.score_frame.grid_columnconfigure(0, weight = 1)
        self.score_frame.grid_columnconfigure(7, weight = 1)
        return (score_label, points_frame, points_label, time_frame, time_label, pointspersec_frame, pointspersec_label)

    def update_scoreboard(self, points, game_over, elapsed):
        """ Update the scoreboard with the correct points, game over label, time, points, and points per second """
        self.points.set("Points: " + str(points))
        if game_over: # if the game has ended
            self.game_over.set("Game Over")
        else: # game is still running
            self.game_over.set("")
            self.total_time += elapsed
            self.total_time = round(self.total_time, 2)
            self.time.set("Time: " + str(self.total_time))
        if self.total_time == 0: # the game just started
            self.pps.set("Points per sec: 0.00")
        else: # the game has been going for a while
            pts_str = self.points.get()
            pts = pts_str.strip("Points: ")
            pps = round((int(pts) / self.total_time), 2)
            self.pps.set("Points per sec: " + str(pps))

    def stop_next_step(self):
        """when called, ends the next time step"""
        self.window.after_cancel(self.time_object)

    def one_step(self, step_time, step_handler):
        """call the next time step with the handler passed"""
        self.time_object = self.window.after(step_time, step_handler)
    def make_black(self,r,c):
        """make the given cell black based on row and column fed"""
        self.cells[r][c]['bg'] = 'black'
    def make_white(self,r,c):
        """make the given cell white based on row and column fed"""
        self.cells[r][c]['bg'] = 'white'
    def make_blue(self,r,c):
        """make the given cell blue based on row and column fed"""
        self.cells[r][c]['bg'] = 'blue'
    def make_red(self,r,c):
        """make the given cell red based on row and column fed"""
        self.cells[r][c]['bg'] = 'red'

    def reset(self):
        """reset the view"""
        #remove game over label
        self.game_over.set("")
        #reset the points label
        self.points.set("Points: 0")
        #change all cells to white
        for r in range(self.num_rows):
                for c in range(self.num_cols):
                    self.make_white(r,c)
        #reset the time counter
        self.total_time = 0
        #reset the time label
        self.time.set("Time: 0.00")
        #do not call the next time step
        self.stop_next_step()
        #reset the points per second label
        self.pps.set("Points per sec: 0.00")

class SnakeModel:
    def __init__(self, num_rows, num_cols):
        """ initialize the model of the game """
        #create variables for number of rows and cols based on passed variables
        self.num_rows = num_rows
        self.num_cols = num_cols
        #set points to 0
        self.points = 0
        #set gameover status to false
        self.game_over = False
        #set wraparound status to false
        self.wraparound_state = False
        # initialize self.open_cells
        self.open_cells = []
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.open_cells.append((r,c))
        # create the snake and food and initialize the direction
        self.create_snake()
        self.food = (random.choice(self.open_cells))
        self.init_direction()

    def init_direction(self): 
        """ Initializes self.direction to the furthest direction """
        # find distances North, South, East, and West
        distN = self.snake[0][0] - 1
        distS = (self.num_cols) - self.snake[0][0]
        distE = (self.num_rows - 1) - self.snake[0][1]
        distW = self.snake[0][1]

        # find which direction is furthest
        distances = [distN, distS, distE, distW]
        greatest_dist = 0
        for d in distances:
            if d > greatest_dist:
                greatest_dist = d
        
        # initialize self.direction to furthest direction
        if greatest_dist == distN:
            self.direction = Direction.NORTH
        elif greatest_dist == distS:
            self.direction = Direction.SOUTH
        elif greatest_dist == distE:
            self.direction = Direction.EAST
        else:
            self.direction = Direction.WEST
    def create_snake(self):
        """ create the snake (head) in a random cell """
        self.snake = [random.choice(self.open_cells)]
        self.open_cells.remove(self.snake[0])

    def advance_snake(self):
        ''' Advances the head of the snake '''
        head = self.snake[0]
        head_r = head[0]
        head_c = head[1]
        # moves head in the appropriate direction, according to self.direction
        if self.direction == Direction.NORTH:
            new_r = head_r - 1
            self.snake.insert(0,(new_r, head_c))
        elif self.direction == Direction.SOUTH:
            new_r = head_r + 1
            self.snake.insert(0,(new_r, head_c))
        elif self.direction == Direction.EAST:
            new_c = head_c + 1
            self.snake.insert(0,(head_r, new_c))
        elif self.direction == Direction.WEST:
            new_c = head_c - 1
            self.snake.insert(0,(head_r, new_c))

        
    def not_wrap_one_step(self):
        """ Game is not in wraparound, so end game if snake tries to go outside of grid """
        if self.snake[0][0] > (self.num_rows - 1) or self.snake[0][0] < 0:
            self.game_over = True
        elif self.snake[0][1] > (self.num_cols - 1) or self.snake[0][1] < 0:
            self.game_over = True
    def wrap_one_step(self):
        """One step if the game is in wrap around mode, game will continue to opposite side if 
        runs into wall"""
        cur_tuple = (self.snake[0])
        self.snake.remove(self.snake[0])
        if cur_tuple[0] > (self.num_rows - 1):
            new_row = 0
            self.snake.insert(0, (new_row, cur_tuple[1]))
        elif cur_tuple[0] < 0:
            new_row = self.num_rows - 1
            self.snake.insert(0, (new_row, cur_tuple[1]))
        elif cur_tuple[1] > (self.num_cols - 1):
            new_col = 0
            self.snake.insert(0, (cur_tuple[0], new_col))
        elif cur_tuple[1] < 0:
            new_col = self.num_cols - 1
            self.snake.insert(0, (cur_tuple[0], new_col))
        else:
            self.snake.insert(0, cur_tuple)
        
    def one_step(self, wraparound):
        """pass the method whether or not in wraparound mode,
           compute the next step of the program with respect
           to the meathod and whether the program is running
           in wraparound mode or normally"""
        #move the snake one step in the direction it is facing
        self.advance_snake()
        # check is snake ran into itself, set game_over to True
        snake_head = self.snake[0]
        if snake_head in self.snake[1:]:
            self.game_over = True
        # if not in wraparound mode and if the snake is going to go off the grid, terminate the game
        if not wraparound: # how can we get chkValue into this 
            self.not_wrap_one_step()
        # if in wraparound mode and if the snake is going to go off the grid, wrap head around to other side of the grid on the same row /  column
        else: # in wraparound mode
            self.wrap_one_step()
        # Removes segment where tail was if the head did not run into food, if it ran into food, increase points by 1 
        if self.snake[0] == self.food:
            self.points += 1
            self.food = random.choice(self.open_cells)    
        else:
            self.snake.remove(self.snake[-1])
        return self.snake, self.food, self.game_over, self.points
     
class CellState(Enum):
    """state of a cell"""
    EMPTY = 0
    SNAKE = 1
    HEAD = 2
    FOOD = 3

class GameState(Enum):
    """State of the game"""
    STARTUP = 0
    RUNNING = 1
    PAUSED = 2
    GAMEOVER = 3
    RUNNINGWRAP = 4

class Wraparound(Enum):
    '''
    On or off
    '''
    ON = 1
    OFF = 2

class Direction(Enum):
    '''
    Directions
    '''
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

if __name__ == "__main__":
   snake_game = Snake()
