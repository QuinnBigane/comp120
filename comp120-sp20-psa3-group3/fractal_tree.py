"""
File: fractal_tree.py
Author:
Date:
Description: Displays fractal tree
"""
import tkinter as tk
import math
class FractalTree:
    def __init__(self):
        """ Initialize the fractal object. """
        #size of canvas
        self.SIZE = 400
        #length each line should shrink per recussive call
        self.recursive_length = .58
        #inital angle of the primary branch
        self.ANGLE = math.pi/2
        #change of angle of each branch
        self.ANGLE_CHANGE = math.pi/5
        # Create window, canvas, control frame, buttons
        self.window = tk.Tk()
        self.window.title("Fractal Tree")
        self.canvas = tk.Canvas(self.window, width = self.SIZE, height = self.SIZE, 
                        borderwidth = 1, relief = 'solid')
        self.canvas.grid(row = 1, column = 1)
        #create the frames
        self.control_frame = tk.Frame(self.window, width = self.SIZE, height = 50)
        self.control_frame.grid(row = 2, column = 1)
        self.control_frame.grid_propagate(False)
        #create the buttons
        self.advance_button = tk.Button(self.control_frame, text="Advance", command = self.advance)
        self.advance_button.grid(row=1, column=1)
        self.reset_button = tk.Button(self.control_frame, text="Reset", command = self.reset)
        self.reset_button.grid(row=1, column=2)
        self.quit_button = tk.Button(self.control_frame, text="Quit", command = self.quit)
        self.quit_button.grid(row=1, column=3)
        #grid the frames
        self.control_frame.grid_rowconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(2, weight = 1)
        self.control_frame.grid_columnconfigure(3, weight = 1)
        
        #create the primary branch
        self.canvas.create_line(self.SIZE//2, 
                                self.SIZE,
                                self.SIZE//2,
                                self.SIZE//3*2)
        # Init current levels of recursion, and draw the intial fractal
        self.current_levels_of_recursion = 0  
        self.draw_fractal(self.SIZE//2, self.SIZE//3*2, self.ANGLE,self.SIZE//3*2*self.recursive_length, self.current_levels_of_recursion)

        tk.mainloop()

    def advance(self):
        """ Advance one level of recursion """
        self.current_levels_of_recursion += 1
        # self.canvas.delete("all")
        self.draw_fractal(self.SIZE//2, self.SIZE//3*2, self.ANGLE,self.SIZE//3*2*self.recursive_length, self.current_levels_of_recursion)

    def reset(self):
        """ Reset to 0 levels of recursion """
        
        self.current_levels_of_recursion = 0

    def quit(self):
        """ Quit the program """
        self.window.destroy()

    #given parent basex, parent basey, parent angle relative to horizontal, parent length, level
    def draw_fractal(self, basex, basey, angle, length, levels_of_recursion):
        """ Draw fractal with levels_of_recursion in square whose upper level corner is
            (upper_left_x, upper_left_y), whose size is size and whose height is size. 
        """
        
        if levels_of_recursion == 0:
            return
        else:
            #create the clockwise branch
            self.canvas.create_line(basex,
                                    basey,
                                    (basex + (math.cos(angle - self.ANGLE_CHANGE)) * length *self.recursive_length),
                                    (basey - (math.sin(angle - self.ANGLE_CHANGE)) * length *self.recursive_length))
            
            #create the counter clockwise branch
            self.canvas.create_line(basex,
                                    basey,
                                    (basex + (math.cos(angle + self.ANGLE_CHANGE)) * length *self.recursive_length),
                                    (basey - (math.sin(angle + self.ANGLE_CHANGE)) * length *self.recursive_length)) 
            #recurssive call on the clockwise branch
            self.draw_fractal((basex + (math.cos(angle - self.ANGLE_CHANGE)) * length *self.recursive_length),
                             (basey - (math.sin(angle - self.ANGLE_CHANGE)) * length *self.recursive_length),
                             angle - self.ANGLE_CHANGE,
                             length*self.recursive_length,
                             levels_of_recursion -1)
            #recurssive call on the counter clockwise branch
            self.draw_fractal((basex + (math.cos(angle + self.ANGLE_CHANGE)) * length *self.recursive_length),
                              (basey - (math.sin(angle + self.ANGLE_CHANGE)) * length *self.recursive_length),
                              angle + self.ANGLE_CHANGE,
                              length*self.recursive_length,
                              levels_of_recursion -1)

if __name__ == "__main__":
    FractalTree()