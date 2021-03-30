from mysql.connector import connect
import connection
def conn():
    con = connect(host='127.0.0.1', username='root', password='abc123', database='pyintern')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

def new_disp_visitor():
    con,cursor = conn()
    cursor.execute('SELECT * FROM visitor')
    visitor = cursor.fetchall()
    close()
    return visitor

def retrieve_data_from_id(email):
    con,cursor = conn()
    try :
        cursor.execute('Select * from visitor where email_id="{}"'.format(email))
        visitor_data = cursor.fetchall()
        close()
        return visitor_data
    except Exception as e :
        return "error : ",e
def update_data(fname,lname,addr,pin_code,mob_no,email_id,date_of_birth,gender):
    con,cursor = conn()
    try :
        cursor.execute("update visitor set first_name='{}', last_name='{}', addr='{}', pin_code='{}', mob_no='{}', email_id='{}', date_of_birth=DATE_ADD('{}', INTERVAL 0 MINUte), gender='{}' where email_id='{}'".format(fname,lname,addr,pin_code,mob_no,email_id,date_of_birth,gender,email_id))
        visitor_data = cursor.fetchall()
        con.commit()
        # first_name = fname, last_name = lname, addr = addr, pin_code = pin_code, mob_no = mob_no, email_id = email_id, date_of_birth = date_of_birth, gender = gender
        close()
        print(visitor_data)
    except Exception as e :
        return "error : ",e

def get_venue_id(venue_id):
    key_venue_id = int(venue_id)
    venue_data = connection.get_venue_data_from_venue_id(int(venue_id))
    if venue_data == []:
        return "No Such data for Venue id:{} exists in the database, Try entering a valid Venue id!".format(key_venue_id)
    else:
        print(venue_data)
        venue_data = venue_data[0]
        venue_city = venue_data[1]
        venue_addr = venue_data[2]
        country_id = venue_data[3]
        state_id = venue_data[4]

        joined_data = connection.join_state_country_table()
        # return render_template('update_venue_page.html',data=joined_data, venue_city=venue_city ,venue_addr=venue_addr,country_id=country_id,state_id=state_id)
        print(joined_data)

def verify_state_id():
    state_table = connection.get_state_table()
    state_id_list = []
    for item in state_table:
        state_id_list.append(item[0])
    print(state_id_list)

def updateVenue_result(key_venue_id,venue_city,venue_addr,country_id,state_id):
    key_venue_id = int(key_venue_id)
    state_id = int(state_id)
    country_id = int(country_id)

    # state_id_verified => True or False
    state_id_verified = connection.verify_state_id(state_id)
    country_id_verified = connection.verify_country_id(country_id)
    print(state_id_verified)
    print(country_id_verified)
    if (state_id_verified=="verified") and (country_id_verified == "verified"):
        message = connection.update_venue_data(venue_city,venue_addr,country_id,state_id,key_venue_id)
        venue_table = connection.get_venue_table()
        print(message,"\n",venue_table)
        # return render_template('updateVenue_result.html',message = message,venue_table=venue_table)
    else :
        message = "Table not Updated!! : State ID is {} and Country Id is {}, Please enter valid data (REFER TABLE ON THE PREVIOUS PAGE)".format(state_id_verified,country_id_verified)
        # return render_template('updateVenue_result.html', message=message)
        print(message)


def extract_countryData_using_countryId(country_id):
    key_country_id = int(country_id)
    country_data = connection.get_country_data_from_country_id(key_country_id)
    if country_data == []:
        return "No Such data for Country Id:{} exists in the database, Try entering a valid Country id!".format(key_country_id)
    else:
        country_data = country_data[0]
        country_name = country_data[1][:]

        return render_template('update_country_page.html', country_name=country_name, key_country_id=key_country_id)
        # print(country_name)

def get_state_data_from_state_id(key_state_id)".format():
    con, cursor = conn()
    try:
        cursor.execute('Select * from state where state_id= {}'.format(key_state_id))
        state_data = cursor.fetchall()
        close()
        return state_data
    except Exception as e:
        return "error : ", e
# updateVenue_result(1,'Mumbai','Sion',4,10)
extract_countryData_using_countryId(3)


# get_venue_id(1)
#
# verify_state_id(1)
# def update_dataa(email):
#
#     visitor_data = retrieve_data_from_id(email)
#     if visitor_data == []:
#         print("None")
#         return render_template('new_update.html', data="No Such data for email:{} exists, Try entering a valid email id!".format(email))
#     else :
#         visitor_data=visitor_data[0]
#         print(visitor_data[1])
# update_data('Kanannnn', 'Sudhakaran', 'Mumbai', '400039', '87797982100', 'swabhav@somaiya.edu', '2020-01-01' ,'M')
'''
@app.route("/choose_id_or_num")
def choose_id_or_num():
        return render_template('new_choose_id_or_num.html')

@app.route("/get_id",methods = ['POST', 'GET'])
def get_id():
    if request.method == 'POST':
        email = request.form['email']
        return redirect(url_for('input_update_data', email=email))
    else:
        email = request.args.get('email')
        return redirect(url_for('input_update_data', email=email))

@app.route("/input_update_data/<email>")
def input_update_data(email):
    key_email_id = email
    visitor_data = connection.retrieve_data_from_id(email)
    if visitor_data == []:
        return "No Such data for email:{} exists, Try entering a valid email id!".format(key_email_id)
    else :
        visitor_data = visitor_data[0]
        fname=visitor_data[1]
        lname=visitor_data[2]
        addr=visitor_data[3]
        pin_code=visitor_data[4]
        mob_no=visitor_data[5]
        email_id=visitor_data[6]
        date_time=visitor_data[7]
        gender=visitor_data[8]
        # [(3, 'Kanan', 'Sudhakaran', 'Mumbai', '400039', '87797982100', 'swabhav@somaiya.edu', datetime.datetime(2020, 1, 1, 0, 0), 'M')]
        return render_template('new_update.html',fname=fname,lname=lname,addr=addr,pin_code=pin_code,mob_no=mob_no,email_id=email_id,date_time=date_time,gender=gender,key_email_id=key_email_id)

@app.route("/updation_process/<key_email_id>",methods = ['POST', 'GET'])
def updation_process(key_email_id):
    # / < fname > / < lname > / < addr > / < pin_code > / < mob_no > / < email_id > / < date_time > / < gender >
    # fname, lname, addr, pin_code, mob_no, email_id, date_time, gender
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        addr = request.form['addr']
        pin_code = request.form['pin_code']
        mob_no = request.form['mob_no']
        email_id = request.form['email_id']
        date_of_birth = request.form['date_time']
        gender = request.form['gender']
        message = connection.update_data(fname, lname, addr, pin_code, mob_no, email_id, date_of_birth, gender,key_email_id)
        return redirect(url_for('disp_message_visitor',message=message))
    else:

        fname = request.args.get('fname')
        lname = request.args.get('lname')
        addr = request.args.get('addr')
        pin_code = request.args.get('pin_code')
        mob_no = request.args.get('mob_no')
        email_id = request.args.get('email_id')
        date_of_birth = request.args.get('date_time')
        gender = request.args.get('gender')
        message = connection.update_data(fname, lname, addr, pin_code, mob_no, email_id, date_of_birth, gender)

        return redirect(url_for('disp_message_visitor', message=message))

@app.route("/disp_message_visitor/<message>")
def disp_message_visitor(message):
    table = connection.new_disp_visitor()
    return render_template('new_disp_message.html',message=message,table=table)
'''