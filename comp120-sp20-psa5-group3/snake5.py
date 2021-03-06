"""
Module: Snake
Title: snake5.py

Authors:
Thomas Padova - tpadova@sandiego.edu
Quinn Bigane - qbigane@sandiego.edu

Date:
5/8/2020

Iteration 5: Connect events in the SnakeView widgets to
stub event handler functions in the Snake class (that is,
the controller). Have the stub function print a short
message saying that they have been called. This will
be similar to Iteration 4 of the life program. There
will be events associated with each of the widgets in
the control frame.

Run the program and interact with all of the widgets 
(the buttons and the slider in the control frame, and
a sampling of the cells in the grid), making sure that
the corresponding stub functions are being called. 
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
        self.NUM_ROWS = 30
        self.NUM_COLS = 30

        # Create view
        self.view = SnakeView(self.NUM_ROWS, self.NUM_COLS)


        # Set up the control
        
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

        # Cell clicks.  (Note that a separate handler function is defined for 
        # each cell.)
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                def handler(event, row = r, column = c):
                    self.cell_click_handler(row, column)
                self.view.set_cell_click_handler(r, c, handler)

        # Start the simulation
        self.view.window.mainloop()



    def start_handler(self):
        """ Start simulation  """
        print("Start simulation")
        
    def pause_handler(self):
        """ Pause simulation """
        print("Pause simulation")
        

    def reset_handler(self):
        """ Reset simulation """
        print("Reset simulation")

    def quit_handler(self):
        """ Quit life program """
        print("Quit program")

    def step_speed_handler(self, value):
        """ Adjust simulation speed"""
        print("Step speed: Value = %s" % (value))
    
    def wraparound_handler(self):
        """Turn on and off wraparound"""
        print("Wraparound checked")

    def cell_click_handler(self, row, column):
        """ Cell click """
        print("Cell click: row = %d col = %d" % (row, column))
class SnakeView:
    def __init__(self, num_rows, num_cols):
        """ Initialize view of the game """
        # Constants
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
        (self.score_label, self.points_frame, self.points_label, self.time_frame, self.time_label, self.pointspersec_frame, self.pointspersec_label, self.game_over_label) = self.add_scoreboard()
    
    def set_cell_click_handler(self, row, column, handler):
        """ set handler for clicking on cell in row, column to the function handler """
        self.cells[row][column].bind('<Button-1>', handler)

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
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                frame = tk.Frame(self.grid_frame, width = self.CELL_SIZE, 
                         height = self.CELL_SIZE, borderwidth = 1, 
                         relief = "solid")
                frame.grid(row = r, column = c)
                row.append(frame)
            cells.append(row)
        return cells

    def add_control(self):
        """ 
        Create control buttons and slider, and add them to the control frame 
        """
        control_panel_padx = ((self.num_cols * self.CELL_SIZE) + self.SCORE_FRAME_WIDTH)/27 # 20 --> 27
        start_button = tk.Button(self.control_frame, text="Start")
        start_button.grid(row=1, column=1, padx=control_panel_padx)
        pause_button = tk.Button(self.control_frame, text="Pause")
        pause_button.grid(row=1, column=2, padx=control_panel_padx)
        step_speed_slider = tk.Scale(self.control_frame, from_=1, to=10, 
                    label="Step Speed", showvalue=0, orient=tk.HORIZONTAL)
        step_speed_slider.grid(row=1, column=3, padx=control_panel_padx)
        reset_button = tk.Button(self.control_frame, text="Reset")
        reset_button.grid(row=1, column=4, padx=control_panel_padx)
        quit_button = tk.Button(self.control_frame, text="Quit")
        quit_button.grid(row=1, column=5, padx=control_panel_padx)
        wraparound_button = tk.Checkbutton(self.control_frame,text="Warparound")
        wraparound_button.grid(row =1, column=6, padx=control_panel_padx)
        # Vertically center the controls in the control frame
        self.control_frame.grid_rowconfigure(1, weight = 1) 

        # Horizontally center the controls in the control frame
        self.control_frame.grid_columnconfigure(0, weight = 1)
        self.control_frame.grid_columnconfigure(7, weight = 1)                                                    
        return (start_button, pause_button, step_speed_slider, 
                reset_button, quit_button, wraparound_button)
    def add_scoreboard(self):
        """ 
        Create control buttons and slider, and add them to the control frame 
        """
        # create score title
        score_label = tk.Label(self.score_frame, text="Score")
        score_label.grid(row=1, column=1,pady=15)
        # create and initialize points frame 
        points_frame = tk.Frame(self.score_frame, borderwidth = 1, width = 20, height = 20, relief = "solid")
        points_frame.grid(row=2, column=1,pady=15)
        points_label = tk.Label(points_frame, text = "Points: 0 ")
        points_label.grid(row = 1, column = 1)
        # create and initialize time frame
        time_frame = tk.Frame(self.score_frame, borderwidth = 1, width = 20, height = 20, relief = "solid")
        time_frame.grid(row=3, column=1,pady=15)
        time_label = tk.Label(time_frame, text = "Time: 0.00 ")
        time_label.grid(row = 1, column = 1)
        # create and initialize the points per second frame
        pointspersec_frame = tk.Frame(self.score_frame, borderwidth = 1, width = 20, height = 20, relief = "solid")
        pointspersec_frame.grid(row=4, column=1,pady=15)
        pointspersec_label = tk.Label(pointspersec_frame, text = "Points per sec: 0.00 ")
        pointspersec_label.grid(row = 1, column = 1)
        # create the Game Over label
        game_over_label = tk.Label(self.score_frame, text="Game Over")
        game_over_label.grid(row=5, column=1,pady=15)

        # Vertically center the controls in the control frame
        self.score_frame.grid_rowconfigure(0, weight = 0) 
        self.score_frame.grid_rowconfigure(6, weight = 1)
        # Horizontally center the controls in the control frame
        self.score_frame.grid_columnconfigure(0, weight = 1)
        self.score_frame.grid_columnconfigure(7, weight = 1)

        return (score_label, points_frame, points_label, time_frame, time_label, pointspersec_frame, pointspersec_label, game_over_label)
class SnakeModel:
    def __init__(self, num_rows, num_cols):
        """ initialize the model of the game """

if __name__ == "__main__":
   snake_game = Snake()
