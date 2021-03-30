import connection
import datetime

def insert_booking(booking_date,total_amount,event_id,exhibitor_id):
    con,cursor=connection.conn()
    query=f"INSERT INTO `booking` (`booking_date`,`total_amount`,`event_id`,`exhibitor_id`) VALUES ('{datetime.datetime()}',{total_amount},{event_id},{exhibitor_id});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_bookstall_map(booking_id,event_id,stall_id):
    con, cursor = connection.conn()
    query = f"INSERT INTO `bookstall_map` (`booking_id`,`event_id`,`stall_id`) VALUES ('{booking_id}',{event_id},{stall_id});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_country(country_name):
    con, cursor = connection.conn()
    query = f"INSERT INTO `country` (`country_name`) VALUES ('{country_name}');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_eventt(event_name,booking_start_date,event_start_date,event_end_date,venue_id):
    con, cursor = connection.conn()
    query = f"INSERT INTO `eventt` (`event_name`,`booking_start_date`,`event_start_date`,`event_end_date`,`venue_id`) VALUES ('{event_name}',{booking_start_date},{event_start_date},{event_end_date},{venue_id});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_exhibitor(exhibitor_name,email_id,phone_no,company_name,company_description,company_addr,company_pin_code,industry_id,country_id,state_id):
    con, cursor = connection.conn()
    query = f"INSERT INTO `exhibitor` (`exhibitor_name`,`email_id`,`phone_no`,`company_name`,`company_description`,`company_addr`,`company_pin_code`,`industry_id`,`country_id`,`state_id`) VALUES ('{exhibitor_name}','{email_id}',{phone_no},'{company_name}',{company_description},{company_addr},{company_pin_code},{industry_id},{country_id},{state_id});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_industry(industry_name):
    con, cursor = connection.conn()
    query = f"INSERT INTO `industry` (`industry_name`) VALUES ('{industry_name}');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def megaconsumercard(spend_amt,spend_date,payment_mode,event_id,booking_id,visitor_id):
    con, cursor = connection.conn()
    query = f"INSERT INTO `megaconsumercard` (`spend_amt`,`spend_date`,`payment_mode`,`event_id`,`booking_id`,`visitor_id`) VALUES ({spend_amt},'{spend_date}','{payment_mode}',{event_id},{booking_id},{visitor_id});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def insert_stall(stall_no,stall_price,stall_size,is_booked,event_id):
    con, cursor = connection.conn()
    query = f"INSERT INTO `stall` (`stall_no`,`stall_price`,`stall_size`,`is_booked`,`event_id`) VALUES ({stall_no},{stall_price},{stall_size},'{is_booked}',{event_id});"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

insert_booking('2020-04-10 00:00:00',14000,2,4)

