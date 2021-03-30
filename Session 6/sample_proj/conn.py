import mysql.connector as mysql
con = mysql.connect(user='root', password='abc123', host='127.0.0.1', database='ContactApp')
def return_data():
    data = con.cursor()
    data.execute("SELECT * FROM contacts")
    ans = data.fetchall()
    return ans