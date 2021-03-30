from mysql.connector import connect

def conn():
    con = connect(host='127.0.0.1', username='root', password='root', database='iimft')
    cursor = con.cursor()
    return con,cursor
def close():
    con,cursor = conn()
    con.close()

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


def insert_state(state_name,country_id):
    con,cursor = conn()
    cursor.execute("INSERT INTO state(state_name,country_id) VALUES(%s,%s)",(state_name,country_id))
    con.commit()
    close()

def display_booking():
    con, cursor = conn()
    cursor.execute("SELECT * FROM BOOKING")
    all_rows = cursor.fetchall()
    return all_rows

def display_bookstall_map():
    con, cursor = conn()
    cursor.execute("SELECT * FROM BOOKSTALL_MAP")
    all_rows = cursor.fetchall()
    return all_rows

def display_country():
    con, cursor = conn()
    cursor.execute("SELECT * FROM COUNTRY")
    all_rows = cursor.fetchall()
    return all_rows

def display_eventt():
    con, cursor = conn()
    cursor.execute("SELECT * FROM EVENTT")
    all_rows = cursor.fetchall()
    return all_rows

def display_exhibitor():
    con, cursor = conn()
    cursor.execute("SELECT * FROM EXHIBITOR")
    all_rows = cursor.fetchall()
    return all_rows

def display_industry():
    con, cursor = conn()
    cursor.execute("SELECT * FROM INDUSTRY")
    all_rows = cursor.fetchall()
    return all_rows

def display_megaconsumercard():
    con, cursor = conn()
    cursor.execute("SELECT * FROM MEGACONSUMERCARD")
    all_rows = cursor.fetchall()
    return all_rows

def display_stall():
    con, cursor = conn()
    cursor.execute("SELECT * FROM STALL")
    all_rows = cursor.fetchall()
    return all_rows

def display_state():
    con, cursor = conn()
    cursor.execute("SELECT * FROM STATE")
    all_rows = cursor.fetchall()
    return all_rows

def display_venue():
    con, cursor = conn()
    cursor.execute("SELECT * FROM VENUE")
    all_rows = cursor.fetchall()
    return all_rows

def display_visitor():
    con, cursor = conn()
    cursor.execute("SELECT * FROM VISITOR")
    all_rows = cursor.fetchall()
    return all_rows

print(display_visitor());