# File: pentagonal.py
# Date: April 30, 2020
# Author: COMP 120 class
# Description: An interator for pentagonal numbers.

class PentagonalIterator:
    def __init__(self):
        """ Initialize the iterator """
        self.pent_n = 1
    
    def __iter__(self):
        """ Returns the iterator """
        return self

    def __next__(self):
        """ Returns the next pentagonal number """
        pent_number = self.pent_n*((3*self.pent_n) - 1 )//2
        self.pent_n += 1
        return pent_number

def main():  
    iterator = PentagonalIterator()
    
    while(True):
        lst = ""
        for i in range(10): 
            next_pent = iterator.__next__()
            if next_pent < 1000:
                lst += str(next_pent)+ " "
            else: 
                return print (lst)
        print(lst)


main()