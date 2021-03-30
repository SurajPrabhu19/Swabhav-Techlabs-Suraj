from mysql.connector import connect


def conn():
    con = connect(host="127.0.0.1", username="root", password="abc123", database="pyintern")
    cursor = con.cursor()
    return con, cursor


def close():
    con, cursor = conn()
    con.close()


def update_country(country_name, country_id):
    con, cursor = conn()
    query = 'UPDATE country  SET country_name="{}" WHERE country_id = {}'.format(
        country_name, country_id
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_state(state_id, state_name, country_name):
    con, cursor = conn()
    cursor.execute(
        'SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name)
    )
    country_id = cursor.fetchall()
    query = 'UPDATE state  SET state_name="{}",country_id={} WHERE state_id = {}'.format(
        state_name, country_id[0][0], state_id
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_venue(venue_id, venue_city, venue_addr, state_name, country_name):
    con, cursor = conn()
    cursor.execute(
        'SELECT state_id  FROM state WHERE state_name = "{}"'.format(state_name)
    )
    state_id = cursor.fetchall()
    cursor.execute(
        'SELECT country_id  FROM country WHERE country_name = "{}"'.format(country_name)
    )
    country_id = cursor.fetchall()
    query = 'UPDATE venue  SET venue_city="{}",venue_addr="{}",state_id={},country_id={} WHERE venue_id = {}'.format(
        venue_city, venue_addr, state_id[0][0], country_id[0][0], venue_id
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_stall(stall_id, stall_no, stall_price, stall_size, is_booked, event_name):
    con, cursor = conn()
    cursor.execute(
        'SELECT event_id  FROM eventt WHERE event_name = "{}"'.format(event_name)
    )
    event_id = cursor.fetchall()
    query = 'UPDATE stall  SET stall_no={},stall_price={},stall_size={},is_booked="{}",event_id={} WHERE stall_id = {}'.format(
        stall_no, stall_price, stall_size, is_booked, event_id[0][0], stall_id
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_industry(industry_name, industry_id):
    con, cursor = conn()
    query = 'UPDATE industry  SET industry_name="{}" WHERE industry_id = {}'.format(
        industry_name, industry_id
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_exhibitor(
    exhibitor_id,
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
    query = 'UPDATE exhibitor SET exhibitor_name="{}",email_id="{}",phone_no="{}",company_name="{}",company_description="{}",company_addr="{}",company_pin_code={},industry_id={},state_id={},country_id={} WHERE exhibitor_id = {}'.format(
        exhibitor_name,
        email_id,
        phone_no,
        company_name,
        company_description,
        company_addr,
        company_pin_code,
        industry_id[0][0],
        state_id[0][0],
        country_id[0][0],
        exhibitor_id,
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_mccard(card_id, spend_amt, spend_date, payment_mode, event_name, email_id):
    con, cursor = conn()
    # get_id(table_name, col_name, col_val,id_name)
    cursor.execute(
        'SELECT event_id FROM eventt WHERE event_name = "{}"'.format(event_name)
    )
    event_id = cursor.fetchall()[0][0]

    cursor.execute(
        "SELECT booking_id FROM booking WHERE event_id = {}".format(event_id)
    )
    booking_id = cursor.fetchall()

    cursor.execute(
        'SELECT visitor_id FROM visitor WHERE email_id = "{}"'.format(email_id)
    )
    visitor_id = cursor.fetchall()[0][0]

    # visitor_id = connection.get_id("visitor", "email_id", email_id, "visitor_id")

    query = (
        'UPDATE megaconsumercard  SET spend_amt={},spend_date=DATE_ADD("{}", INTERVAL 0 MINUte),'
        'payment_mode="{}",event_id={},booking_id={},visitor_id={} '
        "WHERE card_id = {}".format(
            spend_amt,
            spend_date,
            payment_mode,
            event_id,
            booking_id[0][0],
            visitor_id,
            card_id,
        )
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_booking(booking_id, booking_date, total_amount, event_name, email_id):
    con, cursor = conn()

    # get_id(table_name, col_name, col_val,id_name)
    total_amount = float(total_amount)

    cursor.execute(
        'SELECT event_id FROM eventt WHERE event_name = "{}"'.format(event_name)
    )
    event_id = cursor.fetchall()[0][0]

    cursor.execute(
        'SELECT exhibitor_id FROM exhibitor WHERE email_id = "{}"'.format(email_id)
    )
    exhibitor_id = cursor.fetchall()[0][0]

    # exhibitor_id = int(connection.get_id("exhibitor", "email_id", email_id, "exhibitor_id"))

    query = (
        'UPDATE booking SET booking_date=DATE_ADD("{}", INTERVAL 0 MINUte),'
        "total_amount={},event_id={},exhibitor_id={} "
        "WHERE booking_id = {}".format(
            booking_date, total_amount, event_id, exhibitor_id, booking_id
        )
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_visitor(
    visitor_id,
    first_name,
    last_name,
    addr,
    pin_code,
    mob_no,
    email_id,
    date_of_birth,
    gender,
):
    con, cursor = conn()
    # < !--first_name | last_name | addr | pin_code | mob_no | email_id | date_of_birth | gender -->

    # query = f'UPDATE visitor SET first_name="{first_name}",' \
    #         f'last_name="{last_name}",addr="{addr}",pin_code="{pin_code}",mob_no="{mob_no}",' \
    #         f'email_id="{email_id}",date_of_birth=DATE_ADD("{date_of_birth}", INTERVAL 0 MINUte),gender="{gender}" ' \
    #         f'WHERE visitor_id = {visitor_id}'
    query = (
        'UPDATE visitor SET first_name="{}",'
        'last_name="{}",addr="{}",pin_code="{}",mob_no="{}",'
        'email_id="{}",date_of_birth=DATE_ADD("{}", INTERVAL 0 MINUte),gender="{}" '
        "WHERE visitor_id = {}".format(
            first_name,
            last_name,
            addr,
            pin_code,
            mob_no,
            email_id,
            date_of_birth,
            gender,
            visitor_id,
        )
    )
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


def update_event(
    event_id,
    event_name,
    booking_start_date,
    event_start_date,
    event_end_date,
    venue_city,
):
    con, cursor = conn()

    cursor.execute(
        'SELECT venue_id  FROM venue WHERE venue_city = "{}"'.format(venue_city)
    )
    venue_id = cursor.fetchall()[0][0]

    query = (
        'UPDATE eventt SET event_name="{}",'
        'booking_start_date=DATE_ADD("{}", INTERVAL 0 MINUte),'
        'event_start_date=DATE_ADD("{}", INTERVAL 0 MINUte),'
        'event_end_date=DATE_ADD("{}", INTERVAL 0 MINUte), venue_id = {} '
        "WHERE event_id = {}".format(
            event_name,
            booking_start_date,
            event_start_date,
            event_end_date,
            venue_id,
            event_id,
        )
    )

    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()


# update_visitor(5,"Suraj","Prabhu","Vidyanagar, Vidyavihar (W)","400077","8652825823","surajprabhu19@gmail.com",
#                "2000-02-19 00:00:00","M")
