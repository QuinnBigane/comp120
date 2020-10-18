# File: addressbook.py
# Author: 
# Date:
# Description:

import tkinter as tk
from tkinter import ttk
class Address:
    def __init__(self, name, street, city, state, zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

print(int(2.2))
class AddressBook:


    def __init__(self):
        """ Constructor for AddressBook class """

        """Create window."""
        #Create the basic window structure
        self.window = tk.Tk()  
        self.window.title("AddressBook") 
        self.window.geometry("1000x400")

        #define any constants
        self.DEFAULT_GREETING_STRING = "            "
        self.button_padx = 6
        self.address_index = 0
        self.list_of_addresses = []
        #create the frames
        self.top_frame = tk.Frame(self.window)
        self.top_frame.grid(row=1,column =1)

        self.middle_frame = tk.Frame(self.window)
        self.middle_frame.grid(row=2,column =1)
        
        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.grid(row=3,column =1)

        """You will add code here. """

        #Create all Label widgets in the top frame
        self.name_label = tk.Label(self.top_frame, text = "Name:")
        self.name_label.grid(row = 1, column = 1)
        
        self.street_label = tk.Label(self.top_frame, text = "Street:")
        self.street_label.grid(row = 2, column = 1)

        self.city_label = tk.Label(self.top_frame, text = "City:")
        self.city_label.grid(row = 3, column = 1)

        self.state_label = tk.Label(self.top_frame, text = "State:")
        self.state_label.grid(row = 3, column = 3)
    
        self.zip_label = tk.Label(self.top_frame, text = "Zip:")
        self.zip_label.grid(row = 3, column = 5)

        #Create all Entry widgets in the top frame
        self.name = tk.Entry(self.top_frame, width = 40)
        self.name.grid(row=1, column = 2, columnspan = 5)

        self.street = tk.Entry(self.top_frame, width = 40)
        self.street.grid(row=2, column = 2, columnspan = 5)

        self.city = tk.Entry(self.top_frame, width = 20)
        self.city.grid(row=3, column = 2) 

        self.state = tk.Entry(self.top_frame, width = 2)
        self.state.grid(row=3, column = 4)

        self.zip = tk.Entry(self.top_frame, width = 5)
        self.zip.grid(row=3, column = 6)

        #Create all button widgets in middle frame
        self.add = tk.Button(self.middle_frame, text="Add", command = self.add_to_list)
        self.add.grid(row = 1, column =1, padx = self.button_padx)

        self.first = tk.Button(self.middle_frame, text="Delete", command = self.delete_in_list)
        self.first.grid(row = 1, column =2, padx = self.button_padx)
        
        self.next = tk.Button(self.middle_frame, text="First", command = self.first_in_list)
        self.next.grid(row = 1, column =3, padx = self.button_padx)
        
        self.previous = tk.Button(self.middle_frame, text="Next", command = self.next_in_list)
        self.previous.grid(row = 1, column =4, padx = self.button_padx)
        
        self.last = tk.Button(self.middle_frame, text="Previous", command = self.previous_in_list)
        self.last.grid(row = 1, column =5, padx = self.button_padx)

        self.last = tk.Button(self.middle_frame, text="Last", command = self.last_in_list)
        self.last.grid(row = 1, column =6, padx = self.button_padx)
        
        #Create all Label and Entry widgets in the bottom frame
        self.filename_label = tk.Label(self.bottom_frame, text = "Filename")
        self.filename_label.grid(row = 1, column = 1)

        self.filename = tk.Entry(self.bottom_frame, width = 20)
        self.filename.grid(row=1, column = 2)


        #Create all Button widgets in the bottom frame
        self.last = tk.Button(self.bottom_frame, text="Quit", command = self.quit)
        self.last.grid(row = 1, column =5)

        self.last = tk.Button(self.bottom_frame, text="Save to File", command = self.save_to_file)
        self.last.grid(row = 1, column =4)

        self.last = tk.Button(self.bottom_frame, text="Load File", command = self.load_file)
        self.last.grid(row = 1, column =3)
        #upon init, start main loop
        self.window.mainloop()
        

    """You will  other methods."""


    def quit(self):
        """ Quit the window """
        self.window.destroy()
        print("Entered Quit")


    def save_to_file(self):
        """ The user can store an address list to a file by entering
        a filename in the “Filename” entry field, and hitting the
        “Save to File” button. If the filename entry field is empty,
        or if the file cannot be opened, then the button should not
        do anything. If the file can be opened, the current address 
        list should be written to the file. The format of the file is 
        illustrated by the sample file in the repository. (5 lines for 
        each address – one line for each field of the address.)"""
        print("Entered save")
        #recieve the text entered into filename entry
        filename = self.filename.get()
        #try to open file
        try:
            f= open(filename, "w")
            #loop through current addresses and add their name, street, city, state, zip to the file
            for address in self.list_of_addresses:
                f.write(address.name + "\n")
                f.write(address.street + "\n")
                f.write(address.city + "\n")
                f.write(address.state + "\n")
                f.write(address.zip + "\n")
            #close the file
            f.close()
            self.clear_boxes()
        except OSError:
            print("bad file")


    def load_file(self):
        """The user can load an address list from a file by entering a
        filename in the “Filename” entry field, and hitting the “Load 
        File” button. If the filename entry field is empty, or if the 
        file cannot be opened, then the button should not do anything.
        If the file can be opened, the current address list should be 
        deleted, and replaced by the contents of the file. The format 
        of the file is illustrated by the sample file in the repository. 
        (5 lines for each address – one line for each field of the address.)
        You can assume that an address file has the correct format,
        so you do not have to do any exception handling while reading 
        the file. After reading in a file, the current address should 
        be the first address that was read in from the file. """
        print("Entered load")
        #retrieve the filename from the filename entry field
        filename = self.filename.get()
        #try to open that file
        try:
            f= open(filename, "r")
            #store the data in that file
            data= f.read()
            #split the data into tokens to be looped through
            tokens=data.splitlines()

            #loop through the tokens and store in local variables
            n = 0
            while(n<len(tokens)):
                name = tokens[n]
                n += 1
                street = tokens[n]
                n += 1
                city = tokens[n]
                n+=1
                state = tokens[n]
                n+=1
                zip = tokens[n]
                #create an instance of the class Address passing the local variables stored
                instance = Address(name,street,city,state,zip)
                #add that instance of Address to the list of addresses
                self.list_of_addresses.append(instance)
                n+=1

            


        except OSError:
            print("bad file")


    def add_to_list(self):
        """If an address is displayed in the entry fields, the user
        can edit it in any way they want, and then add that address 
        to the address book by hitting the “Add” button. The address 
        should be added directly after the current address that was 
        being displayed. If there was no current address (because the 
        list is empty), then the added address should go at the 
        beginning of the list. After an add, the newly added address 
        should become the current address being displayed. """
        #store the text in the entry fields as an instance of Address class
        instance = Address(self.name.get(),self.street.get(), self.city.get(),self.state.get() ,self.zip.get())
        #append that instant to the list of instances
        self.list_of_addresses.append(instance)
        print("Entered add")

    def first_in_list(self):
        """ The “First” button displays the first address in the address
        list. The address is displayed in the entry name, street, city,
        state, and zip fields. So the entry fields double as display 
        fields. If there is no first address (the address list is empty),
        the button should not do anything."""
        print("Entered first")
        #empty the entry fields
        self.clear_boxes()
        #set address index to 0 for first address
        self.address_index = 0
        #add the current address index instance objects to the appropriate entry field
        self.name.insert(0,self.list_of_addresses[self.address_index].name)
        self.street.insert(0,self.list_of_addresses[self.address_index].street)
        self.city.insert(0,self.list_of_addresses[self.address_index].city)
        self.state.insert(0,self.list_of_addresses[self.address_index].state)
        self.zip.insert(0,self.list_of_addresses[self.address_index].zip)



    def next_in_list(self):
        """The “Next” button displays the next address in the address list
        (the next address after the one currently being displayed). This
        suggests that the program should keep track of the index of the
        address currently being displayed. If there is no next address
        (the last address is already being displayed, or the list is 
        empty), the button should not do anything. """
        #make sure not at end of list
        if len(self.list_of_addresses) > 0:
            if self.address_index < len(self.list_of_addresses)-1:
                #clear entry fields
                self.clear_boxes()
                #add 1 to address index
                self.address_index += 1
                #add the current address index instance objects to the appropriate entry field
                self.name.insert(0,self.list_of_addresses[self.address_index].name)
                self.street.insert(0,self.list_of_addresses[self.address_index].street)
                self.city.insert(0,self.list_of_addresses[self.address_index].city)
                self.state.insert(0,self.list_of_addresses[self.address_index].state)
                self.zip.insert(0,self.list_of_addresses[self.address_index].zip)
        print("Entered next")


    def previous_in_list(self):
        """The “Previous” button should display the previous address in
        the address list. If there is no previous address, the button
        should not do anything. """
        #make sure not at begining of list
        if len(self.list_of_addresses) > 0:
            if self.address_index > 0:
                #clear entry fieilds
                self.clear_boxes()
                #subtract 1 from current address index
                self.address_index-=1
                #add the current address index instance objects to the appropriate entry field
                self.name.insert(0,self.list_of_addresses[self.address_index].name)
                self.street.insert(0,self.list_of_addresses[self.address_index].street)
                self.city.insert(0,self.list_of_addresses[self.address_index].city)
                self.state.insert(0,self.list_of_addresses[self.address_index].state)
                self.zip.insert(0,self.list_of_addresses[self.address_index].zip)
        print("Entered prev")


    def last_in_list(self):
        """The “Last” button should display the last address in the
        address list. If there is no last address (the list is
        empty), the button should do nothing. """
        #clear the boxes
        self.clear_boxes()
        #set the address index to the last in the list
        self.address_index = len(self.list_of_addresses)-1
        #add the current address index instance objects to the appropriate entry field
        self.name.insert(0,self.list_of_addresses[self.address_index].name)
        self.street.insert(0,self.list_of_addresses[self.address_index].street)
        self.city.insert(0,self.list_of_addresses[self.address_index].city)
        self.state.insert(0,self.list_of_addresses[self.address_index].state)
        self.zip.insert(0,self.list_of_addresses[self.address_index].zip)
        print("Entered last")


    def delete_in_list(self):
        """If the user hits the “Delete” button, the currently
        displayed address should be deleted from the address
        list. If there is no currently displayed address
        (because the list is empty), the button should not
        do anything. After an address is deleted, the
        currently displayed address should be the address
        after the deleted address, and if there is not next 
        address, the previous address, and if there is also no 
        previous address (because the list is now empty), 
        nothing should be displayed. """
        print("Entered Delete")
        #remove current address index from list
        self.list_of_addresses.pop(self.address_index)
        #clear the entry fields
        self.clear_boxes()
        #add the current address index to the entry fields
        #because you removed the old current index, the new values at that index were the next values previously
        self.name.insert(0,self.list_of_addresses[self.address_index].name)
        self.street.insert(0,self.list_of_addresses[self.address_index].street)
        self.city.insert(0,self.list_of_addresses[self.address_index].city)
        self.state.insert(0,self.list_of_addresses[self.address_index].state)
        self.zip.insert(0,self.list_of_addresses[self.address_index].zip)
        
    def clear_boxes(self):
        """ Clear all entry boxes in the window"""
        #clear all entry fields of any text
        self.name.delete(0,'end')
        self.state.delete(0,'end')
        self.zip.delete(0,'end')
        self.city.delete(0,'end')
        self.street.delete(0,'end')




if __name__ == "__main__":
    # Create GUI
    AddressBook()
