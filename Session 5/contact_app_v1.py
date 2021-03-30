


from mysql.connector import *
 
def add_data(con,cursor):
    first_name = input("Enter First name : ")
    last_name = input("Enter Last name : ")
    num = int(input("Enter Mobile/Phone number : ")[:10])

    query = "insert into contacts values('{}','{}',{})".format(first_name,last_name,num)

    cursor.execute(query)
    con.commit()

def disp_data(cursor):
    query = "select * from contacts"
    cursor.execute(query)
    data = cursor.fetchmany(10)
    for d in data : 
        print("First name : {} Last name : {} Number : {}".format(d[0],d[1],d[2]))

def numlist(con,cursor):
    query = "select * from contacts"
    cursor.execute(query)
    data = cursor.fetchmany(50)
    number_list = []
    for  elem in data : 
        number_list.append(elem[2])
    number_list = list(map(int,number_list))
    return number_list

def namelist(con,cursor):
    query = "select * from contacts"
    cursor.execute(query)
    data = cursor.fetchmany(10)
    name_list = []
    for  elem in data : 
        name_list.append(elem[0]+elem[1])
    return name_list

#def update_data_by_name
def update_data(con,cursor):
    
    while(True):
        option = input("Update name or number? [name/num]: ")
        num_list = numlist(con,cursor)
        
        if option == 'name' :
            num = int(input("Enter Mobile/Phone number to be updated : ")[:10])
            
            if num in num_list:
                first_name = input("Enter First name : ")
                last_name = input("Enter Last name : ")
    
                query = "update contacts set first_name = '{}',last_name = '{}' where number = {}".format(first_name,last_name,num)
    
                cursor.execute(query)
                con.commit()
                break
            else : print("Number does not exists!")
        elif (option == 'num') :
            first_name = input("Enter First name : ")
            last_name = input("Enter Last name : ")
            name_list = namelist(con,cursor)
            name = first_name+last_name
            if name in name_list and name_list.count(name)==1 :
                new_num = int(input("Enter new Mobile/Phone number to be updated : ")[:10])
                query = "update contacts set number = {} where first_name = '{}' and last_name = '{}'".format(new_num,first_name,last_name)
                cursor.execute(query)
                con.commit()
                break
            elif name in name_list and name_list.count(name)>1:
    
                old_num = int(input("Enter old Mobile/Phone number to be updated : ")[:10])
                if old_num in num_list : 
                    new_num = int(input("Enter new Mobile/Phone number to be updated : ")[:10])
                    query = "update contacts set number = {} where first_name = '{}' and last_name = '{}' and number = {}".format(new_num,first_name,last_name,old_num)
                    cursor.execute(query)
                    con.commit()
                    break
                else : print("Num does not exists!")
            else : print("Name does not exists!")
                
        else :
            print("Option not valid! Enter your choice again!")
            continue

#----------------------------------------------------------------------------------------
        



def delete_data(con,cursor):
    
    while(True):
        
        option = input("Delete by name or number? [name/num]: ")
        num_list = numlist(con,cursor)

        if option == 'num' :
            num = int(input("Enter Mobile/Phone number to be deleted : ")[:10])
            
            if num in num_list:
    
                query = " delete from contacts where number = {}".format(num)
                cursor.execute(query)
                con.commit()
                break
            else : print("Num does not exists!")
                
        elif (option == 'name') :
            first_name = input("Enter First name : ")
            last_name = input("Enter Last name : ")
            name_list = namelist(con,cursor)
            name = first_name+last_name
            if name in name_list and name_list.count(name)==1:
                
                query = "delete from contacts where first_name = '{}' and last_name = '{}'".format(first_name,last_name)
                cursor.execute(query)
                con.commit()
                break

            elif name in name_list and name_list.count(name)>1:
                old_num = int(input("Enter old Mobile/Phone number to be deleted : ")[:10])
                if old_num in num_list :
                    query = "delete from contacts where number = {}".format(old_num)
                    cursor.execute(query)
                    con.commit()
                    break
                else : print("Num does not exists!")
            else : print("name does not exists!")
        else :
            print("Option not valid! Enter your choice again!")
            
#--------------------------------------------------------------------
def v2(con,cursor):
    def add_address(cursor,con):
        fname = input("Enter first name : ")
        lname = input("Enter last name : ")
        address = input("Enter the address : ")
        city = input("Enter city name : ")
        state = input("Enter State/Province : ")
        postal_code = input("Enter Postal code : ")
        name_list = namelist(con,cursor)
        if (fname + lname + address) not in name_list :  
            query = "insert into addressbook values('{}','{}','{}','{}','{}',{})".format(
            fname,lname,address,city,state,int(postal_code))
            cursor.execute(query)
            con.commit()
        else : print("data already present!")
        
    def namelist(con,cursor):
        query = "select * from addressbook"
        cursor.execute(query)
        data = cursor.fetchmany(10)
        name_list = []
        for  elem in data : 
            name_list.append(elem[0]+elem[1]+elem[2])
        return name_list
    
    def del_address(cursor,con):
        fname = input("Enter first name : ")
        lname = input("Enter last name : ")
        address = input("Enter the address : ")
        name_list = namelist(con,cursor)
        if (fname + lname + address) in name_list :  
            query = 'delete from addressbook where fname = "{}" and lname = "{}" and address = "{}"'.format(
                fname,lname,address)
            cursor.execute(query)
            con.commit()
        else : print("data not found")
    
        print("Connection established --> adddressbook.db!")
        
    def join_address(cursor,con):
        query = 'SELECT contacts.number , addressbook.number FROM contacts INNER JOIN addressbook ON contacts.number=addressbook.number '

        cursor.execute(query)
        con.commit()
        
    #add_address(cursor,con)
    #del_address(cursor,con)
    join_address(cursor,con)   
    
#--------------------------------------------------------------------
try :
    con = connect(host = '127.0.0.1',
                     user = 'root',
                     password = 'abc123',
                     database = 'ContactApp')
    print("Connection established!")
    cursor = con.cursor()

    #add_data(con,cursor)
    '''
    disp_data(cursor)
    add_data(con,cursor)
    disp_data(cursor)
    update_data(con,cursor)
    disp_data(cursor)
    delete_data(con,cursor)
    print(numlist(con,cursor))
    disp_data(cursor)
    print(namelist(con,cursor))'''
    v2(con,cursor)
    
except Exception as e :
    print("Error : "+e)
finally :
    if con!=None :
        con.close()
        print("Connection closed!")

print("Done!")
