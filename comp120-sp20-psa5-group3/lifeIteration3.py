"""
Module: lifeIteration3

Author:
John Glick
Department of Computer Science
University of San Diego

Description:
A Python implementation of Conway's game of life, using Tkinter, and implemented
using the model-view-controller design pattern.

Iteration 3: 
Create and display the controls in the control frame: 
   Start button - start the simulation
   Pause button - pause the simulation
   Step button - take one step of simulation
   Step speed slider - adjust speed of simulation
   Reset button - reset the simulation to an empty grid
   quit button - quit the life program
The controls are not connected to anything yet
"""
import tkinter as tk

class Life:
    """ The controller. """
    def __init__(self):
        """ Initializes the game of life """
        # Define parameters
        self.NUM_ROWS = 30
        self.NUM_COLS = 30

        # Create view
        self.view = LifeView(self.NUM_ROWS, self.NUM_COLS)

        # Start the simulation
        self.view.window.mainloop()

            
class LifeView:
    """ The view """

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
         self.step_button, self.step_speed_slider, 
         self.reset_button, self.quit_button) = self.add_control()
        # Create frame for score
        self.score_frame = tk.Frame(self.window, width = self.SCORE_FRAME_WIDTH, height = self.num_rows * self.CELL_SIZE, bg = 'green')
        self.score_frame.grid(row = 1, column = 2) # use grid layout manager 
    

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
        control_panel_padx = ((self.num_cols * self.CELL_SIZE) + self.SCORE_FRAME_WIDTH)/20
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
        return (start_button, pause_button, wraparound_button, step_speed_slider, 
                reset_button, quit_button)

if __name__ == "__main__":
    game_of_life = Life()