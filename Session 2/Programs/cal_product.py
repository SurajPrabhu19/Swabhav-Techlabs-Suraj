def calculate_product(*prices):
	prod = 1	
	for i in prices : 
		prod*=i
			
	return prod

result1 = calculate_product(10,20,30)
print(result1)

list1 = [num for num in range(1,6,2)]
result2 = calculate_product(*list1)
print(result2)