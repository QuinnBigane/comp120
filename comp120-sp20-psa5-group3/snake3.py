"""
Module: Snake
Title: snake3.py

Authors:
Thomas Padova - tpadova@sandiego.edu
Quinn Bigane - qbigane@sandiego.edu

Date:
5/8/2020

Iteration 3: Put widgets in the control frame. 
These will be the start, pause, reset, and quit buttons;
the step speed slider, and the wraparound check button. 
This will be very similar to Iteration 3 of the game of 
life. You have not seen the Tkinter CheckButton widget.
YOu can read about it at any one of a number of websites.
Just google “Tkinter checkbutton”. One that I found is here.
(Checkbuttons are the widget of choice to provide for
turning on or off some feature.)
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

        # Start the simulation
        self.view.window.mainloop()
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
                                height = self.CONTROL_FRAME_HEIGHT)
        self.control_frame.grid(row = 2, column = 1, columnspan = 2)
        self.control_frame.grid_propagate(False)
        (self.start_button, self.pause_button, 
        self.step_speed_slider, self.reset_button,
        self.quit_button, self.wraparound_button) = self.add_control()
        # Create frame for score
        self.score_frame = tk.Frame(self.window, width = self.SCORE_FRAME_WIDTH, height = self.num_rows * self.CELL_SIZE, bg = 'green')
        self.score_frame.grid(row = 1, column = 2) # use grid layout manager 
    

    def add_cells(self):
        """ Add cells to the view """
        cells = []
        #for every cell
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                #create a frame for that cell
                frame = tk.Frame(self.grid_frame, width = self.CELL_SIZE, 
                         height = self.CELL_SIZE, borderwidth = 1, 
                         relief = "solid")
                #grid and store that cell with respect to its row and column
                frame.grid(row = r, column = c)
                row.append(frame)
            cells.append(row)
        return cells

    def add_control(self):
        """ 
        Create control buttons and slider, and add them to the control frame 
        """
        #calculate padx for control frame
        control_panel_padx = ((self.num_cols * self.CELL_SIZE) + self.SCORE_FRAME_WIDTH)/27 # 20 --> 27
        #create start button
        start_button = tk.Button(self.control_frame, text="Start")
        start_button.grid(row=1, column=1, padx=control_panel_padx)
       #create pause button
        pause_button = tk.Button(self.control_frame, text="Pause")
        pause_button.grid(row=1, column=2, padx=control_panel_padx)
       #create step slider 
        step_speed_slider = tk.Scale(self.control_frame, from_=1, to=10, 
                    label="Step Speed", showvalue=0, orient=tk.HORIZONTAL)
        step_speed_slider.grid(row=1, column=3, padx=control_panel_padx)
        #create reset butto 
        reset_button = tk.Button(self.control_frame, text="Reset")
        reset_button.grid(row=1, column=4, padx=control_panel_padx)
       #create quit button
        quit_button = tk.Button(self.control_frame, text="Quit")
        quit_button.grid(row=1, column=5, padx=control_panel_padx)
        #create wrap around checkbutton 
        wraparound_button = tk.Checkbutton(self.control_frame,text="Warparound")
        wraparound_button.grid(row =1, column=6, padx=control_panel_padx)
        # Vertically center the controls in the control frame
        self.control_frame.grid_rowconfigure(1, weight = 1) 

        # Horizontally center the controls in the control frame
        self.control_frame.grid_columnconfigure(0, weight = 1)
        self.control_frame.grid_columnconfigure(7, weight = 1)                                                    
        return (start_button, pause_button, step_speed_slider, 
                reset_button, quit_button, wraparound_button)
class SnakeModel:
    def __init__(self, num_rows, num_cols):
        """ initialize the model of the game """

if __name__ == "__main__":
   snake_game = Snake()
