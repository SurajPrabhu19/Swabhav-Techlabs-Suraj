from mysql.connector import *
def show_data(query):
        cursor.execute(query)
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
        code = (input("Enter country code : ").upper())[:3]
        query = "select * from country where Code = '{}'".format(code)
        print(query)
        show_data(query)
except Exception as e:
        print("exception : ",e)
        
finally :
        if con!=None :
                con.close()
print("Done!")

 
      
