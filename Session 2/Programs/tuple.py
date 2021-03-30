t1 = (10,20)
print("-----------------------------------------------")
print("t1 : ",t1)
print("id of t1 : ",id(t1))
t1+=(3,4)
t1+=({78},)
#t1-=(3,4)
print()

print("After t1+=(3,4) operation : ",t1)
print("id of t1 after operation : ",id(t1))
print("-----------------------------------------------")

l1 = [10,20]
print("id of l1 : ",id(l1))
print("l1 :",l1)
print()
l1+=(30,40)
l1+="hello"

print("id of l1 after operations: ",id(l1))
print("l1 :",l1)
print("-----------------------------------------------")

student_tuple = ("Swabhav",[10,20,30])
print("student_tuple : ",student_tuple)
print("id of student_tuple: ",id(student_tuple),"\n")

print("student_tuple[0][3] : ",student_tuple[0][3])
print("student_tuple[1][1] : ",student_tuple[1][1],"\n")

print("id of student_tuple[1]: ",id(student_tuple[1]))
student_tuple[1][0] = 100
student_tuple[1].append(1234)
print("student_tuple : ",student_tuple)
print("id of student_tuple after student_tuple[1][0] = 100: ",id(student_tuple))
print("id of student_tuple[1]: ",id(student_tuple[1]))

#The code below will give TypeError: 'tuple' object does not support item assignment
#student_tuple[1] = [10,20]
#print("student_tuple : ",student_tuple)
#print("id of student_tuple after student_tuple[1] = [10,20]: ",id(student_tuple))

print("-----------------------------------------------")

'''
a tuple can contain all mutable as well as imutable data structures
we can conclude that tuple can concatenate only a tuple
tuple cahnge their loc on concatenation cuz they are immutable

list can also contain mutable as well as immutable dstructures
lists dont change the location as they are mutable


'''
