def add(a,b):
	print(f'{a:,.2f} + {b:,.2f} = {a+b:>10,.2f}')

def foo(a,b):
	print(a,b)

shares = (10_000.567,10_000.567)
#add(shares)	#this will give an error as the tuple will itself form a single arg and get stored in a and thus 2nd arg i.e b will remain empty
add(*shares)
add(*[10_000.567,10_000.567])
foo(*"Hi")