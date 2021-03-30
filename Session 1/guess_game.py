import random
print("Guess the Number!\I'm thinking of a number from 1 to 10")

value = random.randint(1,10)
count = 0
print(value)
while(True):
	count+=1
	guess = int(input("Your guess : "))

	if guess < value :	print("Too Low")
	
	elif guess == value : 	
		print("You guessed it in %d tries"%count)
		response = input("Would you like to play again? (y/n) : ")
		
		if response == 'y':	
			value = random.randint(1,10)
			count = 0
			continue
		else : 	
			print("Bye!")
			break
	else : 	print("Too High")
	
	


	