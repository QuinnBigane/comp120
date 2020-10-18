# File: addressbook.py
# Author:  

# Date:
# Description: 

import math 
import datetime
import tkinter as tk

class Display_Clock:
    def __init__(self):
        self.window = tk.Tk() # Create a window
        self.window.title("Current Time") # Set a title
        
        
        

        #Constants
        self.constant_width = 500
        self.constant_height = 300
        self.topx=125
        self.topy= 25
        self.bottomx=375
        self.bottomy=275
        self.time=""
    


        

        #Create Canvas
        self.canvas = tk.Canvas(self.window, bg = "white", 
                width = self.constant_width, height = self.constant_height,
                highlightcolor = "black", highlightbackground = "black",
                )
        self.canvas.grid(column=1, row=1)

        #Create cirle
        self.Main_Circle = self.canvas.create_oval(self.topx,self.topy,self.bottomx,self.bottomy, outline='black')
        self.number_12=self.canvas.create_text((self.topx+((self.bottomx-self.topx)/2)), (self.topy+7), text='12')

        self.number_3=self.canvas.create_text(self.bottomx -7, (self.topy+((self.bottomy-self.topy)/2)), text = '3')

        self.number_6=self.canvas.create_text((self.topx+((self.bottomx-self.topx)/2)), (self.bottomy-7), text='6')

        self.number_9=self.canvas.create_text(self.topx +7, (self.topy+((self.bottomy-self.topy)/2)), text='9')



        self.bottom_frame =tk.Frame(self.window)
        self.bottom_frame.grid(row=2,column=1)

        self.time_label=tk.Label(self.bottom_frame, text=self.time)
        self.time_label.grid(row=1,column=1)
        
        self.update_button=tk.Button(self.bottom_frame,text="Update",command=self.update)
        self.update_button.grid(row=2,column=1)

        self.clear_button=tk.Button(self.bottom_frame,text="Clear",command=self.clear)
        self.clear_button.grid(row=2,column=2)


        #Start Event Loop
        self.window.mainloop() 

    def update (self):
        pass
    def clear (self):
        pass
        
        

if __name__ == "__main__":
    Display_Clock()
