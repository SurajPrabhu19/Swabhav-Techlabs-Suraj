rainbow = ['green', 'orange', 'violet']
print("rainbow : ",rainbow)

#---------------violet's index-------------------------------
violet_ind = rainbow.index("violet")
print("index of violet : ",violet_ind)

#---------insert 'red ' at violet location-----------------
rainbow.insert(violet_ind,"red")
print("rainbow : ",rainbow)

#---------------appending 'yellow'---------------------------
rainbow.append("yellow")
print("rainbow after appending 'yellow' : ",rainbow)

#----------------reversing the elem-------------------------
rainbow.reverse()
print("Reversing rainbow :",rainbow)

#--------------------remove 'orange'----------------------
rainbow.remove('orange')
print("rainbow after removing orange :",rainbow)
