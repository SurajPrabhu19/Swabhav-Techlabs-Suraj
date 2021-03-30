from mysql.connector import connect


def conn():
    con = connect(host="127.0.0.1", username="root", password="abc123", database="pyintern")
    cursor = con.cursor()
    return con, cursor


def close():
    con, cursor = conn()
    con.close()


def new_disp_visitor():
    con, cursor = conn()
    cursor.execute("SELECT * FROM visitor")
    visitor = cursor.fetchall()
    close()
    return visitor


def add_contact(fname, lname, contact):
    data = con.cursor()
    print(fname, lname, contact)
    data.execute()
    con.commit()


def insert_visitor(
    first_name, last_name, addr, pin_code, mob_no, email_id, date_of_birth, gender
):
    con, cursor = conn()
    cursor.execute(
        "INSERT INTO visitor(first_name,last_name,addr,pin_code,mob_no,email_id,date_of_birth,gender) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            first_name,
            last_name,
            addr,
            pin_code,
            mob_no,
            email_id,
            date_of_birth,
            gender,
        ),
    )
    con.commit()
    close()


def insert_venue(venue_city, venue_addr, country_id, state_id):
    con, cursor = conn()
    cursor.execute(
        "INSERT INTO venue(venue_city,venue_addr,country_id,state_id) VALUES(%s,%s,%s,%s)",
        (venue_city, venue_addr, country_id, state_id),
    )
    con.commit()
    close()
    "insert into visitor values( {​​ }​​ ,{​​ }​​)".format(
        datetime.datetime(2020, 1, 1, 0, 0)
    )
    "insert into visitor values( { } ,{ })".format(
        datetime.datetime(2020, 1, 1, 0, 0), name
    )

