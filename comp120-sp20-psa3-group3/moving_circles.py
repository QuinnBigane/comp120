"""
File: moving_circles.py 

Author: Quinn Bigane
        Kevin McDonald

Date: 3/6/2020

Description: Program that gets two circle locations from the
user, then draws a line between them, and 
displays the distance between them midway along
the line.  The user can drag either circle around,
and the distance is kept updated.
"""

# Imports
import tkinter as tk
from enum import Enum
import math



class MovingCircles:
    def __init__(self):

        #Creating window
        self.window = tk.Tk()  
        self.window.title("Moving Circles") 
        
        """ define any constants """

        #Canvas Constants
        self.canvas_width = 400
        self.canvas_height = 400
        #Circle Constants
        self.circle_radius = 20
        self.fill_color1 = "red"
        self.fill_color2 = "blue"

        self.circle1_x = None
        self.circle1_y = None

        self.circle2_x = None
        self.circle2_y = None

        self.line_length = None
        #State of program
        self.state = State.WAITING_FOR_CIRCLE1

        """GUI Layout"""
        #create the canvas/bindings
        self.canvas = tk.Canvas(self.window,
            width = self.canvas_width,
            height = self.canvas_height,
            bg = 'white')
        self.canvas.grid(row = 1, column = 1)
        self.canvas.bind("<Button-1>", self.mouse_click_handler)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_drag_handler)
        
        #Create button Frame
        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.grid(row = 2, column = 1)
        #Create Buttons
        self.add = tk.Button(self.bottom_frame, text="Clear", command = self.clear)
        self.add.grid(row = 1, column =1)

        self.first = tk.Button(self.bottom_frame, text="Quit", command = self.quit)
        self.first.grid(row = 1, column =2)
        
        """Main loop"""
        self.window.mainloop()

    """Class meathods"""


    """Clear button handler"""
    def clear(self):
        self.canvas.delete("all")
        self.state = State.WAITING_FOR_CIRCLE1

    """Quit button handler"""
    def quit(self):
        self.window.destroy()

    """Single M1 click handler"""
    def mouse_click_handler(self, event):
        """ Handle mouse click. """

        #first click
        if self.state == State.WAITING_FOR_CIRCLE1:
            # Get the pivot point
            self.circle1_x = event.x
            self.circle1_y = event.y
            self.canvas.create_oval(self.circle1_x - self.circle_radius,self.circle1_y - self.circle_radius,self.circle1_x + self.circle_radius,self.circle1_y + self.circle_radius,fill = self.fill_color1, tags = ["all", "circle1"])
            self.state = State.WAITING_FOR_CIRCLE2
       
        #second click
        elif self.state == State.WAITING_FOR_CIRCLE2:
            # Get the Bob point
            self.circle2_x = event.x
            self.circle2_y = event.y
            self.canvas.create_oval(self.circle2_x - self.circle_radius,self.circle2_y - self.circle_radius,self.circle2_x + self.circle_radius,self.circle2_y + self.circle_radius,fill = self.fill_color2, tags = ["all", "circle2"])
            self.canvas.create_line(self.circle1_x,self.circle1_y,self.circle2_x, self.circle2_y,fill = "black", tags = ["all", "line"])
            
                        
            """Calculate distance betweeen two points
            given their x and y coordinates"""
            self.line_length = round(math.sqrt((self.circle1_x - self.circle2_x)**2 + (self.circle1_y - self.circle2_y)**2), 2)

            if self.circle1_x > self.circle2_x:
                self.labelx = self.circle2_x +(self.circle1_x - self.circle2_x)/2
            else:
                self.labelx = self.circle1_x +(self.circle2_x - self.circle1_x)/2

            if self.circle1_y > self.circle2_y:
                self.labely =  self.circle2_y +(self.circle1_y - self.circle2_y)/2
            else:
                self.labely =  self.circle1_y+(self.circle2_y -self.circle1_y)/2
            
            self.canvas.create_text(self.labelx, self.labely,text = self.line_length, tags = ["all", "text"]) 
            self.state = State.COMPLETE

        #any click after second click
        elif self.state == State.COMPLETE:
            if  self.circle1_x - self.circle_radius < event.x < self.circle1_x + self.circle_radius:
                if self.circle1_y - self.circle_radius < event.y < self.circle1_y + self.circle_radius:
                    self.state = State.DRAG1
            if  self.circle2_x - self.circle_radius < event.x < self.circle2_x + self.circle_radius:
                if self.circle2_y - self.circle_radius < event.y < self.circle2_y + self.circle_radius:
                    self.state = State.DRAG2
    
    """Drag M1 handler"""                
    def mouse_drag_handler(self, event):
        """IF DRAGGING CIRCLE1"""
        if self.state == State.DRAG1:
            #delete circle1, line length text, line
            self.delete_items(["circle1", "text", "line"])
            #create new circle1 where dragging motion stops
            self.create_object("circle1", event.x, event.y)
            #create new line between circle1 and circle2
            self.create_object("line", 0, 0)
            #recalculate length of line between circle1 and circle2
            self.line_length = round(math.sqrt((self.circle1_x - self.circle2_x)**2 + (self.circle1_y - self.circle2_y)**2), 2)
            #decide if cicle1 or 2 is "lower" in the y of the canvas, create labely accordingly
            if self.circle1_x > self.circle2_x:
                self.labelx = self.circle2_x +(self.circle1_x - self.circle2_x)/2
            else:
                self.labelx = self.circle1_x +(self.circle2_x - self.circle1_x)/2

            if self.circle1_y > self.circle2_y:
                self.labely =  self.circle2_y +(self.circle1_y - self.circle2_y)/2
            else:
                self.labely =  self.circle1_y+(self.circle2_y -self.circle1_y)/2
            #create line length text in canvas
            self.canvas.create_text(self.labelx,self.labely,text = self.line_length, tags = ["text", "all"]) 
            #Change state to complete
            self.state = State.COMPLETE


        
        """IF DRAGING CIRCLE2"""
        if self.state == State.DRAG2:
            #delete circle2, line length text, line
            self.delete_items(["circle2", "text", "line"])
            #create new circle2 where dragging motion stops
            self.create_object("circle2", event.x, event.y)
            #create new line between circle1 and circle2
            self.create_object("line", 0, 0)
                        
            #recalculate the distance between circle1 and circle2
            self.line_length = round(math.sqrt((self.circle1_x - self.circle2_x)**2 + (self.circle1_y - self.circle2_y)**2), 2)
            
            #decide if circle1 or 2 is "lower" in the x of the canvas, create labelx accordingly
            if self.circle1_x > self.circle2_x:
                self.labelx = self.circle2_x +(self.circle1_x - self.circle2_x)/2
            else:
                self.labelx = self.circle1_x +(self.circle2_x - self.circle1_x)/2

           #decide if cicle1 or 2 is "lower" in the y of the canvas, create labely accordingly
            if self.circle1_y > self.circle2_y:
                self.labely =  self.circle2_y +(self.circle1_y - self.circle2_y)/2
            else:
                self.labely =  self.circle1_y+(self.circle2_y -self.circle1_y)/2
            #create line length text in canvas
            self.create_object("text", self.labelx, self.labely)
            #Change state to complete
            self.state = State.COMPLETE
    
    """Delete a list of tags"""
    def delete_items(self, lst):
        for tag in lst:
            self.canvas.delete(tag)
    
    """Create an object in canvas given name, x, y coords"""
    def create_object(self,name, x, y):
        #if passed circle1, create circle1 on canvas at x and y
        if name == "circle1":
            self.circle1_x = x
            self.circle1_y = y
            self.canvas.create_oval(self.circle1_x - self.circle_radius,self.circle1_y - self.circle_radius,self.circle1_x + self.circle_radius,self.circle1_y + self.circle_radius,fill = self.fill_color1, tags = ["all", "circle1"])
        #if passed circle2, create circle2 on canvas at x and y
        elif name == "circle2":
            self.circle2_x = x
            self.circle2_y = y
            self.canvas.create_oval(self.circle2_x - self.circle_radius,self.circle2_y - self.circle_radius,self.circle2_x + self.circle_radius,self.circle2_y + self.circle_radius,fill = self.fill_color2, tags = ["all", "circle2"])
        #if passed line, create line between circle1 and circle2
        elif name == "line":
            self.canvas.create_line(self.circle1_x,self.circle1_y,self.circle2_x,self.circle2_y,fill = "black", tags = ["all", "line"])
        #if passed text, create text label at x and y
        elif name == "text":
            self.canvas.create_text(x,y,text = self.line_length, tags = ["all", "text"])
            

""""Class defining the state of the program"""
class State(Enum):
    WAITING_FOR_CIRCLE1 = 1
    WAITING_FOR_CIRCLE2 = 2
    COMPLETE = 3
    DRAG1 = 4
    DRAG2 = 5




if __name__ == "__main__":
    # Create GUI
    MovingCircles() 