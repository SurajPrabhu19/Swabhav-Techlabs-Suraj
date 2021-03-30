#--------------Ex#01-----------------------------------------
import random

#----creating a list of random numbers using list comprehension :
l1 =[random.randint(1,5) for i in range(5)]
print("creating a list of random numbers using list comprehension : ",l1)

#--------------Ex#02-----------------------------------------
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

#----performing flattening using list comprehension : 
#new_list = [ elem for elem in sub_list for sub_list in list_of_lists]
new_list = [y for x in list_of_lists for y in x]
print("new_list : ",(new_list))

#-----------------------1---------------------------------

names = ['MUMBAI','PUNE','DELHI']
print(names)

#---mapping upper case words to lower case using list comprehension : 
lower_names = [(i.lower()) for i in names]
print("mapping upper case words to lower case using list comprehension :",lower_names)

nums = [10,20,30,40]
print(nums)

#----squaring the nos in the nums list using list_comprehension 

squared_nos = [i*i for i in nums]
print("squaring the nos in the nums list using list_comprehension :",squared_nos)

#-----------------------2---------------------------------

my_list = [10,20,30,40]
print("my_list :",my_list)

#----list containing num greater than 20------
new_list1 = [ i for i in my_list if i>20 ]
print("new_list1 : ",new_list1)

#----list containing num greater than 20 else 0------
new_list2 = [ i if i>20 else 0 for i in my_list ]
print("new_list2 : ",new_list2)