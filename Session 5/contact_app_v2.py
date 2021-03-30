
from mysql.connector import *
def v2():
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
    try :
        con = connect(host = '127.0.0.1',
                         user = 'root',
                         password = 'abc123',
                         database = 'ContactApp')
        print("Connection established --> adddressbook.db!")
        
        cursor = con.cursor()

        add_address(cursor,con)
        del_address(cursor,con)
        
    except Exception as e :
        print("Error : "+e)
    finally :
        if con!=None :
            con.close()
            print("Connection closed!")
v2()
print("Done!")

