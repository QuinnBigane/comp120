"""
Module: pendulum.py 

Author:
COMP 120 class
Department of Computer Science
University of San Diego

Description:
Should display fractal H's.  The code starts
off as a copy of the fractal squares preogram.
"""
import tkinter as tk

class Fractal:
    def __init__(self, size):
        """ Initialize the fractal object. """

        self.SIZE = size

        # Create window, canvas, control frame, buttons
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width = self.SIZE, height = self.SIZE, 
                        borderwidth = 1, relief = 'solid')
        self.canvas.grid(row = 1, column = 1)

        self.control_frame = tk.Frame(self.window, width = self.SIZE, height = 50)
        self.control_frame.grid(row = 2, column = 1)
        self.control_frame.grid_propagate(False)

        self.advance_button = tk.Button(self.control_frame, text="Advance", command = self.advance)
        self.advance_button.grid(row=1, column=1)
        self.reset_button = tk.Button(self.control_frame, text="Reset", command = self.reset)
        self.reset_button.grid(row=1, column=2)
        self.quit_button = tk.Button(self.control_frame, text="Quit", command = self.quit)
        self.quit_button.grid(row=1, column=3)
        self.control_frame.grid_rowconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(2, weight = 1)
        self.control_frame.grid_columnconfigure(3, weight = 1)

        # Init current levels of recursion, and draw the intial fractal
        self.current_levels_of_recursion = 0  
        self.draw_fractal(0, 0, self.SIZE, self.current_levels_of_recursion)

        tk.mainloop()

    def advance(self):
        """ Advance one level of recursion """
        self.current_levels_of_recursion += 1
        self.canvas.delete("all")
        self.draw_fractal(0, 0, self.SIZE, self.current_levels_of_recursion)

    def reset(self):
        """ Reset to 0 levels of recursion """
        self.canvas.delete("all")
        self.current_levels_of_recursion = 0

    def quit(self):
        """ Quit the program """
        self.window.destroy()


    def draw_fractal(self, upper_left_x, upper_left_y, size, levels_of_recursion):
        """ Draw fractal with levels_of_recursion in square whose upper level corner is
            (upper_left_x, upper_left_y), whose size is size and whose height is size. 
        """
        if levels_of_recursion == 0:
            return
        else:
            self.canvas.create_rectangle(upper_left_x, upper_left_y, 
                                        upper_left_x + size // 2,
                                        upper_left_y + size // 2,
                                        fill = "black")
            self.draw_fractal(upper_left_x + size // 2,
                            upper_left_y,
                            size // 2, levels_of_recursion - 1)
            self.draw_fractal(upper_left_x,
                            upper_left_y + size // 2,
                            size // 2, levels_of_recursion - 1)
            self.draw_fractal(upper_left_x + size // 2,
                            upper_left_y + size // 2,
                            size // 2, levels_of_recursion - 1)

if __name__ == "__main__":
    fractal = Fractal(400)