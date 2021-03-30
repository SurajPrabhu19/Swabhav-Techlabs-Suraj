from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='abc123', database='ContactApp')
    cursor = con.cursor()
    return con,cursor

def get_contact_data():
    con,cursor = conn()
    cursor.execute("SELECT * FROM CONTACTS")
    contact_data =cursor.fetchall()
    close()
    return contact_data

def get_address_data():
    con,cursor = conn()
    cursor.execute("SELECT * FROM addressbook")
    address_data =cursor.fetchall()
    close()
    return address_data

def get_contact_address_data():
    con,cursor = conn()
    cursor.execute("select * from contacts inner join addressbook on contacts.number = addressbook.number")
    contact_address_data = cursor.fetchall()
    close()
    return contact_address_data
    # print(con)
def address_detail_dict():
    contact_address_data = get_contact_address_data()
    addr_count = 0
    detail_dict = {}
    for data in contact_address_data:
        details = ('''
        <head>
           Full Name : {}<br>
           Address : {}<br>
           Postal Code : {}<br>
           City : {}<br>
           State : {}<br>
           Number : {}<br>
           Email Id : {}<br>
        </head>
           '''.format(data[0] + " " + data[1], data[4], data[7], data[5], data[6], data[3],data[8]))
        if detail_dict.get(data[3]) == None:
            detail_dict[data[3]] = details
        else : detail_dict[data[3]] = details
        addr_count+=1
    return detail_dict

def get_passwords():
    con,cursor = conn()
    cursor.execute('SELECT * FROM passwords')
    password_data = cursor.fetchall()
    close()
    return password_data
def validate_password(fname,lname,pwd,password):
    con,cursor = conn()
    cursor.execute("select * from passwords where fname = '{}' and lname = '{}'".format(fname,lname))
    data = cursor.fetchall()
    # if (str(pwd) == str(password)):
    #     return "Success" + str(pwd) + str(password)
    # else:
    #     return "Failure" + str(pwd) + str(password)
    close()
    return data
def register_contact(fname, lname, number):
    con,cursor = conn()
    try :
        cursor.execute("insert into contacts values('{}','{}',{})".format(fname, lname, number))
        con.commit()
        message =  "Contact Added"
    except Exception as e :
        error_mess = "error : "+str(e)
        message =  error_mess
    close()
    return message
def register_address(number,addr,city,state,p_code,id):
    con, cursor = conn()
    try:
        cursor.execute("insert into addressbook values({},'{}','{}','{}','{}','{}')".format(number,addr,city,state,p_code,id))
        con.commit()
        message = "Address Added"
    except Exception as e:
        error_mess = "error : " + str(e)
        message = error_mess
    close()
    return message

def close():
    con,cursor = conn()
    con.close()
    # ------------------------------------------------------------------------------------------------------------------------
def new_disp_visitor():
    con,cursor = conn()
    cursor.execute('SELECT * FROM visitor')
    visitor = cursor.fetchall()
    close()
    return visitor

def update_name(fname,lname,email):
    con,cursor = conn()
    cursor.execute("update visitor set first_name='{}',last_name='{}' where email_id='{}'".format(fname,lname,email))
    visitor = cursor.fetchall()
    con.commit()
    close()
    return visitor
def update_data_by_id():
    con,cursor = conn()
    cursor.execute('')

    close()
    return


# address_detail_dict()
# get_contact_address_data()