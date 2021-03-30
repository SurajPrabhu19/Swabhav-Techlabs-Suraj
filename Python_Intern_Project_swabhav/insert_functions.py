from mysql.connector import connect


def conn():
    con = connect(host="127.0.0.1", username="root", password="abc123", database="pyintern")
    cursor = con.cursor()
    return con, cursor


def close():
    con, cursor = conn()
    con.close()


def insert_country(country_name):
    con, cursor = conn()
    query = f"INSERT INTO `country` (`country_name`) VALUES ('{country_name}');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_state(state_name, country_name):
    con, cursor = conn()
    cursor.execute(
        'SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name)
    )
    country_id = cursor.fetchall()
    query = f"INSERT INTO `state` (`state_name`,`country_id`) VALUES ('{state_name}',{country_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_venue(venue_city, venue_addr, state_name, country_name):
    con, cursor = conn()
    cursor.execute(
        'SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name)
    )
    state_id = cursor.fetchall()
    cursor.execute(
        'SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name)
    )
    country_id = cursor.fetchall()
    query = f"INSERT INTO `venue` (`venue_city`,`venue_addr`,`state_id`,`country_id`) VALUES ('{venue_city}','{venue_addr}',{state_id[0][0]},{country_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_stall(stall_no, stall_price, stall_size, is_booked, event_name):
    con, cursor = conn()
    cursor.execute(
        'SELECT event_id  FROM eventt WHERE event_name = "{}"'.format(event_name)
    )
    event_id = cursor.fetchall()
    query = f"INSERT INTO `stall` (`stall_no`,`stall_price`,`stall_size`,`is_booked`,`event_id`) VALUES ({stall_no},{stall_price},{stall_size},'{is_booked}',{event_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_industry(industry_name):
    con, cursor = conn()
    query = f"INSERT INTO `industry` (`industry_name`) VALUES ('{industry_name}');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_exhibitor(
    exhibitor_name,
    email_id,
    phone_no,
    company_name,
    company_description,
    company_addr,
    company_pin_code,
    industry_name,
    state_name,
    country_name,
):
    con, cursor = conn()
    cursor.execute(
        'SELECT industry_id  FROM industry WHERE industry_name = "{}"'.format(
            industry_name
        )
    )
    industry_id = cursor.fetchall()
    cursor.execute(
        'SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name)
    )
    state_id = cursor.fetchall()
    cursor.execute(
        'SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name)
    )
    country_id = cursor.fetchall()
    query = f"INSERT INTO `exhibitor` (`exhibitor_name`,`email_id`,`phone_no`,`company_name`,`company_description`,`company_addr`,`company_pin_code`,`industry_id`,`state_id`,`country_id`) VALUES ('{exhibitor_name}','{email_id}','{phone_no}','{company_name}','{company_description}','{company_addr}',{company_pin_code},{industry_id[0][0]},{state_id[0][0]},{country_id[0][0]});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_mccard(spend_amt, spend_date, payment_mode, event_name, email_id):
    con, cursor = conn()
    # get_id(table_name, col_name, col_val,id_name)
    # event_id = connection.get_id("eventt", "event_name", event_name,"event_id")

    cursor.execute(
        'SELECT event_id FROM eventt WHERE event_name = "{}"'.format(event_name)
    )
    event_id = cursor.fetchall()[0][0]

    cursor.execute(
        "SELECT booking_id FROM booking WHERE event_id = {}".format(event_id)
    )
    booking_id = cursor.fetchall()[0][0]

    cursor.execute(
        'SELECT visitor_id FROM visitor WHERE email_id = "{}"'.format(email_id)
    )
    visitor_id = cursor.fetchall()[0][0]

    # visitor_id = connection.get_id("visitor","email_id",email_id,"visitor_id")
    query = 'insert into megaconsumercard values(null,{},DATE_ADD("{}", INTERVAL 0 MINUTE),"{}",{},{},{})'.format(
        spend_amt, spend_date, payment_mode, event_id, booking_id, visitor_id
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def insert_booking(booking_date, total_amount, event_name, email_id):
    con, cursor = conn()

    # get_id(table_name, col_name, col_val,id_name)
    total_amount = float(total_amount)

    # event_id = int(connection.get_id("eventt", "event_name", event_name,"event_id"))
    cursor.execute(
        'SELECT event_id FROM eventt WHERE event_name = "{}"'.format(event_name)
    )
    event_id = cursor.fetchall()[0][0]

    cursor.execute(
        'SELECT exhibitor_id FROM exhibitor WHERE email_id = "{}"'.format(email_id)
    )
    exhibitor_id = cursor.fetchall()[0][0]
    # booking_date | total_amount | event_id | exhibitor_id

    query = 'insert into booking values(null,DATE_ADD("{}", INTERVAL 0 MINUTE),{},{},{})'.format(
        booking_date, total_amount, event_id, exhibitor_id
    )
    cursor.execute(query)

    con.commit()
    cursor.close()
    con.close()


def insert_visitor(
    first_name, last_name, addr, pin_code, mob_no, email_id, date_of_birth, gender
):
    con, cursor = conn()

    query = f'insert into visitor values(null,"{first_name}","{last_name}","{addr}","{pin_code}","{mob_no}","{email_id}",DATE_ADD("{date_of_birth}", INTERVAL 0 MINUTE),"{gender}")'
    cursor.execute(query)

    con.commit()
    cursor.close()
    con.close()


def insert_event(
    event_name, booking_start_date, event_start_date, event_end_date, venue_city
):
    con, cursor = conn()
    cursor.execute(
        'SELECT venue_id  FROM venue WHERE venue_city = "{}"'.format(venue_city)
    )
    venue_id = cursor.fetchall()[0][0]
    query = (
        f'insert into eventt values(null,"{event_name}",DATE_ADD("{booking_start_date}", INTERVAL 0 MINUTE),'
        f'DATE_ADD("{event_start_date}", INTERVAL 0 MINUTE),DATE_ADD("{event_end_date}", INTERVAL 0 MINUTE),'
        f"{venue_id})"
    )
    cursor.execute(query)

    con.commit()
    cursor.close()
    con.close()


# insert_booking("2021-02-19 00:00:00", "1111", "iimft_1", "pantaloons@gmail.com")
