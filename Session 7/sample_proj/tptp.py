import connection
from flask import Flask,redirect,url_for
# def success(name,password):
#     print("enter")
#     password_data = connection.get_passwords()
#     for data in password_data:
#         pwd = (data[2])
#         if str(password) == str(pwd):
#             # return True
#             return "Password Correct "
#     return "Password InCorrect "
#     #    name_data = data[0]+" "+data[1]
#     #    pwd = data[2]
#     #    if name == name_data :
#     #       if str(pwd) == str(password):
#     #          return 'Success'+str(pwd)+str(password)
#     #       else :
#     #          return 'Faliure'+str(pwd)+str(password)

from mysql.connector import connect

con = connect(host='127.0.0.1',username = 'root', password = 'abc123' ,database = 'ContactApp')
cursor = con.cursor()
# def register_contact(fname, lname, number):
#     try :
#         cursor.execute("insert into contacts values('{}','{}',{})".format(fname, lname, number))
#         con.commit()
#         return "Contact Added"
#     except Exception as e :
#         error_mess = "error :",e
#         return error_mess
#
# def register(fname,lname,number):
#    message = register_contact(fname, lname, number)
#    print(message)
#    # return redirect(url_for('open_addcontact'))
#
# # data= success('Suraj',12345)
# # print(data)
# register('Suraj','Prabhu',1234567890)
def get_contact_address_data():
    cursor.execute("select * from contacts inner join addressbook on contacts.number = addressbook.number;")
    contact_address_data = cursor.fetchall()
    # print(contact_address_data)
    x = ""
    for data in contact_address_data :
        x = ('''
        Name : {}
        Address : {}
        Postal_Code : {}
        City : {}
        State : {}
        Number : {}
        '''.format(data[0]+" "+data[1],data[4],data[7],data[5],data[6],data[3])) + x
    print(x)

