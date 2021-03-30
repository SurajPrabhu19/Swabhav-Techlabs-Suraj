from random import *

frequencies = {}
seed(2)
for i in range(1_00_000):
	value = randint(1,6)
	if frequencies.get(value) == None : 
		frequencies[value]=1
	else:
		frequencies[value]+=1
print(frequencies)