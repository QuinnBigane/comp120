# File: statement-eval.py
# Author: Quinn Bigane and Kevin McDonald
# Date: 2/15/2020
# Description: Program that reads and interprets a
#    file containing simple expression and assignment
#    statements.

from pathlib import Path
import re  # For regular expressions

class BadStatement(Exception): 
    pass

def interpret_statements(filename):
    """
    Algorithm:
    Take in file from user
    Open and read the file -if can't open raise error and tell the user why it cant work
    See if the line has comments
    split the line into tokens
    

    """


    """ Given a file, this function should open that file, loop through it 
    by line, prepare it to be split into tokens by removing any comments, 
    split it into tokens, and feed that to the helper function  """


    """
    1. Try and open the file passed to the funciton, if not possible return error
    2. Loop through all the lines in the file
        a. Remove all comments
        b. split line into seperate strings for each part of the statment
        c. feed the tokens and previously known variables to the interpret_one_statement function
    3. When done interpreting the line, print the line number and solution or bad statment
    """


    try:
        #open file for reading
        infile = open(filename, "r")
    except OSError:
        print("Could not open or access file.")
    #declare storage place for variables
    variables = {}
    #declare counter for lines
    counter = 0
    #creating a class for bad lines
  
    #loop through each line in file
    for line in infile:
        try:
            try:
                counter += 1
                #check for comments in line, if so remove
                loc_hashtag = line.find("#")
                if loc_hashtag >= 0:
                    line = line[0:loc_hashtag]
                #split lines into tokens on spaces
                tokens=line.split()
                #only feed tokens if there is data to feed
                if len(tokens) > 0:
                    #feed tokens and current known variables to the interpret_one_line func
                    variables = interpret_one_statement(tokens, variables)
                    #print line number and associated variable change
                    print("Line " + str(counter) + ": " + str(tokens[0]) + " = " + str(variables[tokens[0]]))
            except TypeError:
                raise BadStatement
            except KeyError:
                raise BadStatement
            except ValueError:
                raise BadStatement
        except BadStatement:
            print("Line " + str(counter) + ": Invalid statement")

    return 

def interpret_one_statement(tokens, variables):
    """ Given a list of tokens and variables previously known, this
     function should check if the current variable already is known,
    variables values """

    """
    1. Confirm the first variable is a valid variable and whether or not it is alraedy assigned
    2. Place all the even tokens in a numbers list
    3. Place all the odd tokens in a operator list
    4. add the first number in the list
    5. check what the next operator is
    6. Add or subtract the next number based on the previous opperator
    7. repeat steps 5 and 6 until done
    8. store the sum as the value of the variable in the dictionary 
    """

    #check if the variable being operated on is known, if not declare

    if re.fullmatch("[a-zA-Z_][a-zA-Z0-9_]*",tokens[0]):
        if tokens[0] not in variables:
            variables[tokens[0]]= 0
    else:
        raise TypeError

    
    #create a list to store all the numbers being added to the variable
    nums=[]
    #loop over the even tokens, starting at index 2, ending at the length of the list of tokens
    for i in range(2,len(tokens),2):
        #try to append the token to the list as a float
        if re.fullmatch("[-]?[0-9]*[.]?[0-9]*", tokens[i]):
            nums.append(float(tokens[i]))
        #if a ValueError is raised, try to use that string as a known variable and append the value associated with it
        else:
            nums.append(float(variables[tokens[i]]))


    #create a list to store all the operators for the statement
    oper=[]
    #loop over the odd tokens, starting at 3, ending at the length of the list of tokens
    for i in range(3,len(tokens),2):
        if re.fullmatch("[+|-]", tokens[i]):
            oper.append(tokens[i])
        else:
            raise BadStatement
    #check ratio of nums to operators
    if((len(oper)+1)!=len(nums)):
        raise BadStatement
    #check to see if the 
    #add the first number to the variable
    new_sum=0
    new_sum += nums[0]
    #check if the = is there
    if tokens[1] != "=":
        raise BadStatement
    #loop over the remaining opperators
    for i in range(len(oper)):
        #if the next opperator is a plus, add the next number
        if oper[i]=="+":
            new_sum +=nums[i+1]
        #if the next opperator is a minus, subtract the next number
        if oper[i]=="-":
            new_sum-=nums[i+1]
    variables[tokens[0]] = format(new_sum, ".6f")
    return variables


# You can add additional helper method(s) if you want.




if __name__ == "__main__":
    file_name = "statements.txt"  # you can create another file with statements
                                  # and change the name of this variable to that
                                  # filename.

    interpret_statements(file_name)