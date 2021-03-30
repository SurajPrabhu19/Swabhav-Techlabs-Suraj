from mysql.connector import *
def show_data(statement):
        cursor.execute(statement)
        data = cursor.fetchmany(10)
        for c in data :
                print("country :",c[1],"  ","pop :",c[6])
        
try :
        con = connect(host = '127.0.0.1',
                      user = 'root',
                      password = 'abc123',
                      database = 'world'
                      )
        print("Connection : ",con.is_connected())
        cursor = con.cursor()
        
        print("-------------------ASCENDING-------------------------")
        show_data('select * from country order by population')        

except Exception as e:
        print("exception : ",e)
        
finally :
        if con!=None :
                con.close()
print("Done!")

def delete_data(con,cursor):
    option = input("Delete by name or number? [name/num]: ")
    while(True):
        num_list = num_list(con,cursor)
        while(True) :
            if option == 'num' :
                num = int(input("Enter Mobile/Phone number to be updated : ")[:10])
                
                if num in num_list():
        
                    query = " delete from contacts where number = {}".format(num)
                    cursor.execute(query)
                    con.commit()
                    break
                else : print("Num does not exists!")
                    
            elif (opt == 'name') :
                first_name = input("Enter First name : ")
                last_name = input("Enter Last name : ")
                name_list = name_list(con,cursor)
                name = first_name+last_name
                if name in name_list:
                    num = int(input("Enter Mobile/Phone number to be updated : ")[:10])
                    query = "delete from contacts where first_name = '{}' and last_name = '{}'".format(first_name,last_name)
    
                    cursor.execute(query)
                    con.commit()
                    break
                else : print("name does not exists!")
            else :
                print("Option not valid! Enter your choice again!")
                continue