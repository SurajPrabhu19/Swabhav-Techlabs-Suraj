______________________________________________START_________________________________________________________________________________

#---------------------------------------------Variables-----------------------------------------------------------------------------
score = 0       # score keeps track of total sum of value at each turn -> range = (0 to 20) 
turn = 1        # counts the number of turns -> initializing turn with 1

#-------------------------------------------initialize()----------------------------------------------------------------------------
def initialize():
    '''
        INITIALIZES THE VALUE OF DIE AND CHOICE

    Returns
    -------
    choice :  'roll' or 'hold' -> ('r' or 'h')
    die : value on a die -> (1 to 6)

    '''
    import random
    while(True):
        choice = input("Roll or hold? (r/h): ")     # choice can be 'roll'->'r' or 'hold'->'h'
        
        if choice=='r' or choice=='h' :
            break
        
        else :
            print("Enter only 'r' or 'h'!")         # warning
            continue
        
    die = random.randint(1,6)                       # die values ranges from (1 to 6)    
    
    return choice,die

#-------------------------------------------roll(turn_score, score, die)--------------------------------------------------------------
def roll(turn_score, score, die):
    '''
        UPDATES THE VALUE OF TURN_SCORE AND SCORE AT EACH ROLL/TURN

    Parameters
    ----------
    turn_score : initial value of turn_score
    score : initial value of score
    die : value on a die -> (1 to 6)

    Returns
    -------
    turn_score : updated value of turn_score
    score : updated value of score
    die : value on a die -> (1 to 6)

    '''
    print("Die: %d" %(die))
    turn_score+=die
    score+=die
    
    return turn_score, score, die

#-------------------------------------------main()-------------------------------------------------------------------------------------
def main()
    while(True and score<=20):
        #-------------------------TURN---------------------------------------------
        print("\n"+"TURN %d" %turn)                     # printing the number of turns
        turn_score = 0                                  # initializing the turn_score to 0 at each turn without changing the actual score
        
        #------------------------GAME_STARTS---------------------------------------
        while(True and score<=20):
            
            #--------------------INITIALIZATION------------------------------------
            choice, die = initialize()                               # initializing the choice and number on the die
            if die==1 : print("Die:",die)
            
            '''-------------------------------------------RULES---------------------------------------------------------------------------
                1.  When a die is rolled -> the value on die gets added to the score if score is value other then 1 ->
                    and if value on die = 1 then the score become 0 -> the game starts again 
                    
                2.  When 'h' or 'hold' option is inputed by the user -> the score retains its value till the previous role
                    and -> the game again starts with fresh value of turn_score (i.e score at each turn) 
                    
                3.  Now if the score at any point exceeds 20 ->  than the game ends and the final score is displayed at the output
            '''
            #---------------------ROLL---------------------------------------------
            if(choice == 'r' and die!=1):                           # executes the block of code when roll i.e 'r' is selected
            
                turn_score, score, die = roll(turn_score, score,die)
                #print("turn_score : ",turn_score)
                
            #---------------------HOLD---------------------------------------------        
            elif (choice == 'h'):
                
                print("Score for turn is:",turn_score)
                turn_score = 0                                      # resetting the turn_score to 0 at each hold of a die
                break
            
            #---------------------DIE = (1)----------------------------------------
            else: 
                
                score, turn_score = 0, 0                            # since value on die = 1 -> resetting the turn_score and score 
                print("Turn Over, No Score!")
                break
            
        turn+=1;                                                    # incrementing turn when die = 1 or hold is selected 
        if score!= 0 : print("score : ",score)                      # this line avoids printing score when die = 1 
    
    print("\nYou finished game in {} turns!".format(turn-1),"\nGame Over!")    # prints the turn at which score exceeds 20

#-----------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__' :
    main()
    
______________________________________________END_________________________________________________________________________________________


# while(score <= 20) : 
# 	if(score >= 20): break
# 	print("TURN %d" %count)
# 	count+=1 ; turn_score = 0
# 	while( choice!= 'h' or die != 1 ) : 

# 		choice = input("Roll or hold? (r/h): ")
# 		if(choice == 'r'):
# 			die = randint(1,6)
# 			if(score >= 20): 
# 				print("Score for turn: %d" %turn_score)
# 				print("Total Score: %d" %score)
# 				break
# 			print("Die: "+str(die))
# 			if(die ==  1):
# 				score = 0
# 				print("Turn over. No score")
# 				if(score >= 20): break
# 				break
# 			else : 
# 				turn_score += die
# 				score += die
# 		elif(choice == 'h') :
# 			print("Score for turn: %d" %turn_score)
# 			print("Total Score: %d" %score)
# 			break
# 		else : 		
# 			print("Invalid Option!") 
# 	print()
#------------------Game Over--------------------------------------------
