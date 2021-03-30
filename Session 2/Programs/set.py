#-----------creating a set-----------------------
# s1 = {10,20}
s1 = set([10,20])
print(s1)
print("id(s1)",id(s1))
#------------adding (30,40) to set s1---------------
s1.add((30,40))
print("s1.add((30,40)) : ",s1)

#------------adding ([50,60]) to set s1----------------
'''s1.add([50,60])
print("s1.add([50,60]) : ",s1)'''

#--------------adding hello-----------------------------
s1.add('hello')
print("s1.add('hello') : ",s1)
print("id(s1)",id(s1))

'''
in a set we can add immutable string and tuple
but set is unable to add mutable list cuz they are unhashable 
'''