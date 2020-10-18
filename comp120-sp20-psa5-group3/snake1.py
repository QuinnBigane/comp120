"""
Module: Snake
Title: snake1.py

Authors:
Thomas Padova - tpadova@sandiego.edu
Quinn Bigane - qbigane@sandiego.edu

Date:
5/8/2020

Iteration 1: A program that displays the game window with 
the three frames (grid frame, control frame, score frame), 
each simply a solid color with no widgets. This will be similar 
to Iteration 1 of the life program, but you will have one more
 frame, and a different arrangement of frames. The program for 
 this iteration should be in a file named snake1.py
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
        self.grid_frame = tk.Frame(self.window, height = self.num_rows * self.CELL_SIZE,
                                width = self.num_cols * self.CELL_SIZE, bg = 'red')
        self.grid_frame.grid(row = 1, column = 1) # use grid layout manager

        # Create frame for controls
        self.control_frame = tk.Frame(self.window, width = (self.num_cols * self.CELL_SIZE) + self.SCORE_FRAME_WIDTH, 
                                height = self.CONTROL_FRAME_HEIGHT, bg = 'blue')
        self.control_frame.grid(row = 2, column = 1, columnspan = 2) # use grid layout manager     

        # Create frame for score
        self.score_frame = tk.Frame(self.window, width = self.SCORE_FRAME_WIDTH, height = self.num_rows * self.CELL_SIZE, bg = 'green')
        self.score_frame.grid(row = 1, column = 2) # use grid layout manager 
class SnakeModel:
    def __init__(self, num_rows, num_cols):
        """ initialize the model of the game """

if __name__ == "__main__":
   snake_game = Snake()
