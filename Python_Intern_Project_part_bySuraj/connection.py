from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='root', database='iimft')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()


####################################______VisitorTable_related_functions_____###################################################
def get_visitor_data_from_visitor_id(key_visitor_id):
    con,cursor = conn()
    try :
        cursor.execute('Select * from visitor where visitor_id="{}"'.format(key_visitor_id))
        visitor_data = cursor.fetchall()
        close()
        return visitor_data
    except Exception as e :
        return "error : ",e

def update_visitor_data(fname,lname,addr,pin_code,mob_no,email_id,date_of_birth,gender,key_email_id):
    con,cursor = conn()
    try :
        cursor.execute("update visitor set "
                       "first_name='{}',"
                       " last_name='{}',"
                       " addr='{}',"
                       " pin_code='{}',"
                       " mob_no='{}',"
                       " email_id='{}',"
                       " date_of_birth=DATE_ADD('{}', INTERVAL 0 MINUte),"
                       " gender='{}'"
                       " where visitor_id='{}'".format(fname,lname,addr,pin_code,mob_no,email_id,
                                                     date_of_birth,gender,key_email_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ",e
####################################______VenueTable_related_functions_____###################################################
def get_venue_data_from_venue_id(venue_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from venue where venue_id="{}"'.format(venue_id))
        venue_data = cursor.fetchall()
        close()
        return venue_data
    except Exception as e:
        return "error : ", e

def update_venue_data(venue_city,venue_addr,country_id,state_id,key_venue_id):
    con,cursor = conn()
    try :
        # key_venue_id = int(key_venue_id)
        # state_id = int(state_id)
        # country_id = int(country_id)
        cursor.execute("update venue set venue_city='{}', venue_addr='{}', country_id={}, state_id={} where venue_id={}".format(venue_city,venue_addr,country_id,state_id,key_venue_id))
        # visitor_data = cursor.fetchall()
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ",e

####################################______EventTable_related_functions_____###################################################
def get_event_data_from_event_id(event_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from eventt where event_id= {}'.format(event_id))
        event_data = cursor.fetchall()
        close()
        return event_data
    except Exception as e:
        return "error : ", e

def update_event_data(key_event_id,event_name,booking_start_date,event_start_date,event_end_date,venue_id):
    con,cursor = conn()
    try :
           # event_name | booking_start_date | event_start_date | event_end_date | venue_id |

        cursor.execute("update eventt set"
                       " event_name='{}',"
                       " booking_start_date=DATE_ADD('{}', INTERVAL 0 MINUte),"
                       " event_start_date=DATE_ADD('{}', INTERVAL 0 MINUte),"
                       " event_end_date=DATE_ADD('{}', INTERVAL 0 MINUte),"
                       " venue_id={} where event_id={}".format(event_name,
                                                               booking_start_date,
                                                               event_start_date,
                                                               event_end_date,
                                                               venue_id,
                                                               key_event_id))
        # visitor_data = cursor.fetchall()
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ",e


####################################______StallTable_related_functions_____###################################################
def get_stall_data_from_stall_id(stall_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from stall where stall_id= {}'.format(stall_id))
        stall_data = cursor.fetchall()
        close()
        return stall_data
    except Exception as e:
        return "error : ", e

def update_stall_data(key_stall_id, stall_no, stall_price, stall_size, is_booked, event_id):
    con,cursor = conn()
<<<<<<< HEAD

    try :
        cursor.execute("update stall set"
                       " stall_no={},"
                       " stall_price={},"
                       " stall_size={},"
                       " is_booked='{}',"
                       " event_id={} where stall_id={}".format(stall_no,
                                                               stall_price,
                                                               stall_size,
                                                               is_booked,
                                                               event_id,
                                                               key_stall_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ",e

####################################______ExhibitorTable_related_functions_____###################################################
def get_exhibitor_data_from_exhibitor_id(exhibitor_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from exhibitor where exhibitor_id= {}'.format(exhibitor_id))
        exhibitor_data = cursor.fetchall()
        close()
        return exhibitor_data
    except Exception as e:
        return "error : ", e

def update_exhibitor_data(key_exhibitor_id, exhibitor_name, email_id, phone_no,
                          company_name,company_description, company_addr, company_pin_code,
                          industry_id, country_id, state_id):
    con, cursor = conn()

    try :
        # exhibitor_id | exhibitor_name | email_id | phone_no | company_name | company_description | company_addr | company_pin_code |
        # industry_id | country_id | state_id
        cursor.execute("update exhibitor set"
                       " exhibitor_name='{}',"
                       " email_id='{}',"
                       " phone_no='{}',"
                       " company_name='{}',"
                       " company_description='{}',"
                       " company_addr='{}',"
                       " company_pin_code={},"
                       " industry_id={},"
                       " country_id={},"
                       " state_id={} "
                       " where exhibitor_id={}".format(exhibitor_name, email_id, phone_no,
                                                       company_name, company_description, company_addr, company_pin_code,
                                                       industry_id, country_id, state_id, key_exhibitor_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ", e

####################################______BookingTable_related_functions_____###################################################
def get_booking_data_from_booking_id(booking_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from booking where booking_id= {}'.format(booking_id))
        booking_data = cursor.fetchall()
        close()
        return booking_data
    except Exception as e:
        return "error : ", e

def update_booking_data(key_booking_id, total_amount,booking_date, exhibitor_id,event_id ):
    con, cursor = conn()
    # key_booking_id, total_amount, booking_date, exhibitor_id, event_id
    try :
        cursor.execute("update booking set"
                       " total_amount ={},"
                       " booking_date = DATE_ADD('{}', INTERVAL 0 MINUte),"
                       " exhibitor_id={},"
                       " event_id={}"
                       " where booking_id={}".format(total_amount, booking_date, exhibitor_id, event_id, key_booking_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ", e

####################################______Mega_Consumer_Card_Table_related_functions_____###################################################
def get_mccard_data_from_mccard_id(mccard_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from megaconsumercard where card_id= {}'.format(mccard_id))
        mccard_data = cursor.fetchall()
        close()
        return mccard_data
    except Exception as e:
        return "error : ", e

def update_mccard_data(key_mccard_id, spend_amt, spend_date, payment_mode, event_id, booking_id, visitor_id):
    con, cursor = conn()
    # key_booking_id, total_amount, booking_date, exhibitor_id, event_id
    try :
        cursor.execute("update megaconsumercard set"
                       " spend_amt ={},"
                       " spend_date = DATE_ADD('{}', INTERVAL 0 MINUte),"
                       " payment_mode='{}',"
                       " event_id={},"
                       " booking_id={},"
                       " visitor_id={}"
                       " where card_id={}".format(spend_amt, spend_date, payment_mode, event_id, booking_id,
                                                  visitor_id, key_mccard_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ", e


####################################______Industry_Table_related_functions_____###################################################
def get_industry_data_from_industry_id(key_industry_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from industry where industry_id= {}'.format(key_industry_id))
        industry_data = cursor.fetchall()
        close()
        return industry_data
    except Exception as e:
        return "error : ", e

def update_industry_data(key_industry_id, industry_name):
    con, cursor = conn()
    try :
        cursor.execute("update industry set"
                       " industry_name ='{}'"
                       " where industry_id={}".format(industry_name, key_industry_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ", e
####################################______State_Table_related_functions_____###################################################
def get_state_data_from_state_id(key_state_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from state where state_id= {}'.format(key_state_id))
        state_data = cursor.fetchall()
        close()
        return state_data
    except Exception as e:
        return "error : ", e

def update_state_data(key_state_id, state_name):
    con, cursor = conn()
    try :
        cursor.execute("update state set"
                       " state_name ='{}'"
                       " where state_id={}".format(state_name, key_state_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ", e
####################################______Country_Table_related_functions_____###################################################
def get_country_data_from_country_id(key_country_id):
    con, cursor = conn()
    try:
        cursor.execute('Select * from country where country_id= {}'.format(key_country_id))
        country_data = cursor.fetchall()
        close()
        return country_data
    except Exception as e:
        return "error : ", e

def update_country_data(key_country_id, country_name):
    con, cursor = conn()
    try :
        cursor.execute("update country set"
                       " country_name ='{}'"
                       " where country_id={}".format(country_name, key_country_id))
        con.commit()
        close()
        return "Table Updated!"
    except Exception as e :
        return "error : ", e

####################################______Verification_functions_____###################################################

# -------------------------------------verify_state_id------------------------------------------------------------------
def verify_state_id(state_id):
    state_table = get_state_table()
    state_id_list = []
    for item in state_table:
        state_id_list.append(item[0])
    if state_id in set(state_id_list):
        return "Verified"
    else: return 'Not Verified'
# -------------------------------------verify_country_id----------------------------------------------------------------
def verify_country_id(country_id):
    country_table = get_country_table()
    country_id_list = []
    for item in country_table:
        country_id_list.append(item[0])

    if country_id in set(country_id_list):
        return "Verified"
    else: return 'Not Verified'

# -------------------------------------verify_venue_id------------------------------------------------------------------
def verify_venue_id(venue_id):
    venue_table = get_venue_table()
    venue_id_list = []
    for item in venue_table:
        venue_id_list.append(item[0])

    if venue_id in set(venue_id_list):
        return "Verified"
    else:
        return 'Not Verified'

# -------------------------------------verify_stall_id------------------------------------------------------------------
def verify_stall_id(stall_id):
    stall_table = get_stall_table()
    stall_id_list = []
    for item in stall_table:
        stall_id_list.append(item[0])

    if stall_id in set(stall_id_list):
        return "Verified"
    else:
        return 'Not Verified'

# -------------------------------------verify_event_id------------------------------------------------------------------
def verify_event_id(event_id):
    event_table = get_event_table()
    event_id_list = []
    for item in event_table:
        event_id_list.append(item[0])

    if event_id in set(event_id_list):
        return "Verified"
    else:
        return 'Not Verified'

# -------------------------------------verify_industry_id------------------------------------------------------------------
def verify_industry_id(industry_id):
    industry_table = get_industry_table()
    industry_id_list = []
    for item in industry_table:
        industry_id_list.append(item[0])

    if industry_id in set(industry_id_list):
        return "Verified"
    else:
        return 'Not Verified'
# -------------------------------------verify_exhibitor_id------------------------------------------------------------------
def verify_exhibitor_id(exhibitor_id):
    exhibitor_table = get_exhibitor_table()
    exhibitor_id_list = []
    for item in exhibitor_table:
        exhibitor_id_list.append(item[0])

    if exhibitor_id in set(exhibitor_id_list):
        return "Verified"
    else:
        return 'Not Verified'
# -------------------------------------verify_booking_id------------------------------------------------------------------
def verify_booking_id(booking_id):
    booking_table = get_booking_table()
    booking_id_list = []
    for item in booking_table:
        booking_id_list.append(item[0])

    if booking_id in set(booking_id_list):
        return "Verified"
    else:
        return 'Not Verified'

# -------------------------------------verify_visitor_id------------------------------------------------------------------
def verify_visitor_id(visitor_id):
    visitor_table = get_visitor_table()
    visitor_id_list = []
    for item in visitor_table:
        visitor_id_list.append(item[0])

    if visitor_id in set(visitor_id_list):
        return "Verified"
    else:
        return 'Not Verified'
####################################______GetTable_functions_____###################################################

#----------------------get_state_table------------------------------------------------------------------------------
def get_state_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from state')
        state_table = cursor.fetchall()
        close()
        return state_table
    except Exception as e:
        return "error : ", e
#----------------------get_country_table----------------------------------------------------------------------------
def get_country_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from country')
        country_table = cursor.fetchall()
        close()
        return country_table
    except Exception as e:
        return "error : ", e
#----------------------get_event_table------------------------------------------------------------------------------
def get_event_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from eventt')
        event_table = cursor.fetchall()
        close()
        return event_table
    except Exception as e:
        return "error : ", e

#----------------------get_venue_table------------------------------------------------------------------------------
def get_venue_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from venue')
        state_table = cursor.fetchall()
        close()
        return state_table
    except Exception as e:
        return "error : ", e


#----------------------get_stall_table------------------------------------------------------------------------------
def get_stall_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from stall')
        stall_table = cursor.fetchall()
        close()
        return stall_table
    except Exception as e:
        return "error : ", e

#----------------------get_exhibitor_table------------------------------------------------------------------------------
def get_exhibitor_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from exhibitor')
        exhibitor_table = cursor.fetchall()
        close()
        return exhibitor_table
    except Exception as e:
        return "error : ", e

#----------------------get_industry_table------------------------------------------------------------------------------
def get_industry_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from industry')
        industry_table = cursor.fetchall()
        close()
        return industry_table
    except Exception as e:
        return "error : ", e

#----------------------get_booking_table------------------------------------------------------------------------------
def get_booking_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from booking')
        booking_table = cursor.fetchall()
        close()
        return booking_table
    except Exception as e:
        return "error : ", e

#----------------------get_mega_consumner_card_table------------------------------------------------------------------------------
def get_mega_consumner_card_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from megaconsumercard')
        megaconsumercard_table = cursor.fetchall()
        close()
        return megaconsumercard_table
    except Exception as e:
        return "error : ", e

#----------------------get_visitor_table------------------------------------------------------------------------------
def get_visitor_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from visitor')
        visitor_table = cursor.fetchall()
        close()
        return visitor_table
    except Exception as e:
        return "error : ", e

#----------------------join_state_country_table----------------------------------------------------------------------------
def join_state_country_table():
    con, cursor = conn()
    try:
        cursor.execute('Select * from state natural join country')
        joined_data = cursor.fetchall()
        close()
        return joined_data
    except Exception as e:
        return "error : ", e
#----------------------join_exhibitor_state_country_table----------------------------------------------------------------------------
def join_exhibitor_state_country_table():
    con, cursor = conn()
    try:
        #
        cursor.execute('select country_id, country_name, state_id, state_name, industry_id, industry_name'
                       ' from industry outer join country natural join state')
        joined_data = cursor.fetchall()
        close()
        return joined_data
    except Exception as e:
        return "error : ", e
=======
    cursor.execute('SELECT * FROM visitor')
    visitor = cursor.fetchall()
    close()
    return visitor

def add_contact(fname,lname,contact):
    data = con.cursor()
    print(fname,lname,contact)
    data.execute()
    con.commit()

def insert_visitor(first_name,last_name,addr,pin_code,mob_no,email_id,date_of_birth,gender):
    con,cursor = conn()
    cursor.execute("INSERT INTO visitor(first_name,last_name,addr,pin_code,mob_no,email_id,date_of_birth,gender) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(first_name,last_name,addr,pin_code,mob_no,email_id,date_of_birth,gender))
    con.commit()
    close()

def insert_venue(venue_city,venue_addr,country_id,state_id):
    con,cursor = conn()
    cursor.execute("INSERT INTO venue(venue_city,venue_addr,country_id,state_id) VALUES(%s,%s,%s,%s)",(venue_city,venue_addr,country_id,state_id))
    con.commit()
    close()
    "insert into visitor values( {​​ }​​ ,{​​ }​​)".format(datetime.datetime(2020, 1, 1, 0, 0))
    "insert into visitor values( { } ,{ })".format(datetime.datetime(2020, 1, 1, 0, 0), name)
>>>>>>> 1bd8e154d9ce5e8e68956cf2690f086d973f5af8
