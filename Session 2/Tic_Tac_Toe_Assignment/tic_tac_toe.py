# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:25:58 2021

@author: Suraj
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#_______________________________________START______________________________________________________________________________________

#--------------------------------------position()---------------------------------------------------------------------------------
def position():
    
    '''
        VALIDATING THE POSTION SO THAT ERROR IS AVOIDED DURING EXECUTION
    '''
    
    row = int(input("Enter the row value less than or equal to 3: ")) - 1      # Enter the row value less than or equal to 3
    col = int(input("Enter the column value less than or equal to 3: ")) - 1   # Enter the column value less than or equal to 3
    
    if row<=2 and row>=0 and col<=2 and col>=0 : return True,row,col           # returns True if row and col are less than 3
    else : return False,None,None                                              # returns False as the position is not valid 
    
#--------------------------------------enter(grid)---------------------------------------------------------------------------------
def enter(grid,turn,mark):
    '''
        THIS FUNCTION IS USED TO ENTER A MARK AT A PARTICULAR LOCATION/SPACE

    Parameters
    ----------
    grid : stores the initial grid of tic-tac-toe game.
    turn : stores the actual value of the turn of player going on - range(1 to 9).
    mark : stores either 'X' or 'O'.

    Returns
    -------
    grid : stores the updated grid of tic-tac-toe game.
    mark : stores either 'X' or 'O'.

    '''
    
    while(True) : 
        
        #---------------------------position_validation------------------------
        valid_position, row, col = position()                   # position function helps validating the location
            
        if valid_position == False :                            
            print("Enter rows and column values less than 3!")   # warning
            continue
        else:
        #---------------------------filling_the_mark_at_empty_space------------
            if  grid[row][col]=="_" :
                mark = mark_auto(turn,mark)                      # automatically marks at input position   
                grid[row][col] = mark                            # filling the given position with mark 
                display(grid)
                return grid,mark
            
            else :  print("Please enter only at empty postion!")         # this line warns the user if wrong mark is entered  
#--------------------------------------mark_assign()---------------------------------------------------------------------------------
def mark_assign():
    
    '''  
        THIS FUNCTION ONLY ALLOWS ENTRY OF "X" OR "O" IN MARK VARIABLE 
        ELSE FUNCTION WILL CONTINOUSLY ITERATE UNLESS AND UNTILL "X" OR "O" IS ENTERED
    '''
    
    while(True):
        mark = input("Starting with? (either 'X' or 'O)' : ").upper()
        if ( mark=='X' or mark=='O') :
            return mark
        else : 
            print("Please enter 'X' or 'O'!")               
            continue
    
#--------------------------------------mark_auto(turn, mark)---------------------------------------------------------------------------------
def mark_auto(turn,mark):
    '''
        THIS FUNCTION AUTOMATICALLY SELECTS THE MARK BASED ON PREVIOUS MARK

    Parameters
    ----------
    turn : stores the actual value of the turn of player going on - range(1 to 9).
    mark : stores either 'X' or 'O'.

    Returns
    -------
    mark : stores either 'X' or 'O'.

    '''
    option = {'X' : 'O' , 'O' : 'X'}
    
    if turn>=2 :
        mark = option.get(mark)
        
    elif turn == 1 : 
        if mark == 'X' : mark =  'X'
        else : mark = 'O'
    
    return mark
#--------------------------------------check(grid)---------------------------------------------------------------------------------
def check(grid):
    '''
        CHECKS ALL POSSIBLE PATTERNS OF 'X' AND 'O's ON THE GRID AND
        RETURNS THE MARK OF THE RESPECTTIVE PATTERN FORMED ELSE RETURNS 'None'

    Parameters
    ----------
    grid : stores the initial grid of tic-tac-toe game.

    Returns
    -------
    'X' OR 'O' OR 'None' DEPENDING ON WHETHER A PATTERN IS DETECTED OR NOT

    '''
    #---------------------------checking only 'X' patterns---------------------
    if(    (grid[0][1] == 'X' and grid[0][2] == 'X' and grid[0][0] == 'X') or   # top horizontal line
           (grid[0][2] == 'X' and grid[1][2] == 'X' and grid[2][2] == 'X') or   # right vertical line
           (grid[0][0] == 'X' and grid[1][0] == 'X' and grid[2][0] == 'X') or   # left vertical line
           (grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X') or   # bottom horizontal line
           (grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X') or   # center horizontal line
           (grid[0][1] == 'X' and grid[1][1] == 'X' and grid[2][1] == 'X') or   # center vertical line
           (grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X') or   # backward diagonal line
           (grid[0][2] == 'X' and grid[1][1] == 'X' and grid[2][0] == 'X')      # forward diagonal line
           ):
        return 'X'
    #---------------------------checking only 'O' patterns---------------------
    elif(  (grid[0][1]== 'O' and grid[0][2]== 'O' and grid[0][0]== 'O') or      # top horizontal line
           (grid[0][2]== 'O' and grid[1][2]== 'O' and grid[2][2]== 'O') or      # right vertical line
           (grid[0][0]== 'O' and grid[1][0]== 'O' and grid[2][0]== 'O') or      # left vertical line
           (grid[2][0]== 'O' and grid[2][1]== 'O' and grid[2][2]== 'O') or      # bottom horizontal line
           (grid[1][0]== 'O' and grid[1][1]== 'O' and grid[1][2]== 'O') or      # center horizontal line
           (grid[0][1]== 'O' and grid[1][1]== 'O' and grid[2][1]== 'O') or      # center vertical line
           (grid[0][0]== 'O' and grid[1][1]== 'O' and grid[2][2]== 'O') or      # backward diagonal line
           (grid[0][2]== 'O' and grid[1][1]== 'O' and grid[2][0]== 'O')         # forward diagonal line
           ):
        return 'O' 
    #---------------------------No pattern detected----------------------------
    else : 
        return None                             # returns None if no pattern is detected
    
#--------------------------------------final_res(result,grid)----------------------------------------------------------------------
def final_res(result,turn):
    '''
        THIS FUNCTION DECLARES THE FINAL RESULT BASED ON WHETHER A PATTERN IS DETECTED OR NOT
        
    Parameters
    ----------
    result : 'X' or 'O' or None -> contains the mark of resultant pattern formed.
    turn : stores the actual value of the turn of player going on - range(1 to 9).

    Returns
    -------
    start : True or False -> helps to continue or discontinue the game.

    '''
    if      result == 'X' or result == 'O' :    # case 1 : if block runs when a pattern of 'X' or 'O' is detected
        print("{} wins!".format(result))
        start =  False
    
    elif    result == None and turn == 9   :    # case 2 : this elif block runs if no pattern is detected or turn = 9
        print("Its a draw!")
        start =  False
        
    else : start =  True                          # returns True to continue the loop in main function
    
    return start
#--------------------------------------display(grid)------------------------------------------------------------------------------
def display(grid):  
    ''' 
        DISPLAYS THE ENTIRE GRID
    '''
    for sub_list in grid : print(sub_list)
    
#--------------------------------------main()------------------------------------------------------------------------------------

def main():

    #---------CREATING 3X3 ARRAY/GRID AS A BASE FOR TIC-TAC-TOE GAME-----------
    grid = [["_" for i in range(3)] for j in range(3)]     # list comprehension
    display(grid)
    #-------------------------------variable_assignment-----------------------
    start = True                                           # helps to continue the game for turn < 9 -> (True or False)
    turn = 0                                               # turn - range(1 to 9)
    mark = mark_assign()                                   # assigns a intial value of mark given by the user -> ('X' or 'O')
    #-------------------------------start_of_game------------------------------
    while(start):
        turn+=1                                            # turn can increment upto 9 and finally end the game at 9th turn (i.e the last turn)
        #-------------------------------STEP_1---------------------------------
        
        '''IN THE BELOW CODE WE USE "enter(grid)" FUNCTION TO ENTER "X" OR "O" '''
        new_grid,mark = enter(grid,turn,mark)              # enter mark ('X' or 'O') in the grid at a particular location
        
        #-------------------------------STEP_2---------------------------------
        
        ''' IN THE CODE BELOW, 'CHECK(GRID)' FUNCTION CHECKS ALL THE POSSIBLE PATTERNS
            (i.e A COMPLETE PATTERN) AND RETURNS EITHER 'X' OR 'O' OR 'None', DEPENDING 
            ON THE PATTEN FORMED AND STORES THE RETURNED VALUE IN "result" variable  '''
        result = check(new_grid)            
    
        #-------------------------------STEP_3---------------------------------
        
        ''' IN THE CODE BELOW, FINAL RESULT IS DECLARED AND GAME IS CONTINUED
            OR DISCONTINUED'''
        start = final_res(result,turn)                   # final_res(result,turn) declares the result (under a specific condition)
        
#--------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__" :
    main()
    
#_______________________________________END______________________________________________________________________________________
