from mysql.connector import *

try :
        con = connect(host = 'localhost',
                      user = 'root',
                      password = 'abc123',
                      database = 'world')
        print("Connection : ",con.is_connected())
        cursor = con.cursor()
        cursor.execute('show tables')

except Exception as e:
        print("exception : ",e)
        
finally :
        if con!=None :
                con.close()
print("Done!")
