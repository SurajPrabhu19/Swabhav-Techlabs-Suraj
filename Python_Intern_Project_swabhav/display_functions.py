from mysql.connector import connect


def conn():
    con = connect(host="127.0.0.1", username="root", password="abc123", database="pyintern")
    cursor = con.cursor()
    return con, cursor


def close():
    con, cursor = conn()
    con.close()


def display_country():
    con, cursor = conn()
    cursor.execute("SELECT * FROM country")
    country = cursor.fetchall()
    close()
    return country


def display_state():
    con, cursor = conn()
    cursor.execute(
        "SELECT state_id,state_name,country_name FROM state JOIN country ON state.country_id=country.country_id"
    )
    state = cursor.fetchall()
    close()
    return state


def display_venue():
    con, cursor = conn()
    cursor.execute(
        "SELECT venue_id,venue_city,venue_addr,state_name,country_name FROM venue JOIN state ON venue.state_id=state.state_id JOIN country ON venue.country_id=country.country_id "
    )
    venue = cursor.fetchall()
    close()
    return venue


# -----------------------------------------
def display_event():
    con, cursor = conn()
    cursor.execute("SELECT * FROM eventt")
    event = cursor.fetchall()
    close()
    return event


def display_stall():
    con, cursor = conn()
    cursor.execute(
        "SELECT stall_id,stall_no,stall_price,stall_size,is_booked,event_name FROM stall JOIN eventt ON stall.event_id=eventt.event_id"
    )
    stall = cursor.fetchall()
    close()
    return stall


def display_industry():
    con, cursor = conn()
    cursor.execute("SELECT * FROM industry")
    industry = cursor.fetchall()
    close()
    return industry


def display_exhibitor():
    con, cursor = conn()
    cursor.execute(
        "SELECT exhibitor_id,exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_name,state_name,country_name FROM exhibitor JOIN industry ON exhibitor.industry_id=industry.industry_id JOIN state ON exhibitor.state_id=state.state_id JOIN country ON exhibitor.country_id=country.country_id "
    )
    exhibitor = cursor.fetchall()
    close()
    return exhibitor


# ------------------------------


def display_mccard():
    con, cursor = conn()
    cursor.execute(
        " SELECT card_id,spend_amt, spend_date, payment_mode, event_name, email_id FROM megaconsumercard"
        " JOIN eventt ON megaconsumercard.event_id=eventt.event_id"
        " JOIN visitor ON megaconsumercard.visitor_id=visitor.visitor_id order by card_id;"
    )
    mccard_data = cursor.fetchall()
    close()
    return mccard_data


def display_booking():
    con, cursor = conn()
    cursor.execute(
        " SELECT booking_id,booking_date, total_amount, event_name, email_id FROM booking"
        " join eventt on booking.event_id=eventt.event_id"
        " join exhibitor on exhibitor.exhibitor_id=booking.exhibitor_id order by booking_id ;"
    )
    booking_data = cursor.fetchall()
    print(booking_data)
    close()
    return booking_data


def display_exhibitor_1():
    con, cursor = conn()
    cursor.execute(
        "select exhibitor_name, email_id, phone_no, company_name, company_description, company_addr,"
        " company_pin_code,industry_name,state_name,country_name from exhibitor"
        " join industry on exhibitor.industry_id=industry.industry_id"
        " join state on state.state_id=exhibitor.state_id"
        " join country on country.country_id=exhibitor.country_id order by exhibitor_id;"
    )
    exhibitor_data = cursor.fetchall()
    close()
    return exhibitor_data


# -----------------------------------------------------------------------------
def display_visitor():
    con, cursor = conn()
    cursor.execute("Select * from visitor")
    visitor_data = cursor.fetchall()
    close()
    return visitor_data


def display_event():
    con, cursor = conn()
    cursor.execute(
        "select  event_id, event_name, booking_start_date, event_start_date, event_end_date, venue_city from"
        " eventt join venue where eventt.venue_id=venue.venue_id order by event_id"
    )
    event_data = cursor.fetchall()
    close()
    return event_data
