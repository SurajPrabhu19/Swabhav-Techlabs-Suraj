<<<<<<< HEAD
from flask import Flask, redirect, url_for, request, render_template
import connection

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')
@app.route("/options")
def options():
    return render_template('options.html')

## ####################################______VISITOR_____###################################################
@app.route('/put_visitor_id')
def put_visitor_id():
    visitor_table = connection.get_visitor_table()
    return render_template('put_visitor_id.html', visitor_table=visitor_table)

@app.route("/extract_visitorId_from_request", methods=['POST', 'GET'])
def extract_visitorId_from_request():
    if request.method == 'POST':
        visitor_id = int(request.form['visitor_id'])
        return redirect(url_for('extract_visitorData_using_visitorId', visitor_id=visitor_id))
    else:
        visitor_id = int(request.args.get('visitor_id'))
        return redirect(url_for('extract_visitorData_using_visitorId', visitor_id=visitor_id))


@app.route("/extract_visitorData_using_visitorId/<visitor_id>")
def extract_visitorData_using_visitorId(visitor_id):
    key_visitor_id = int(visitor_id)
    visitor_data = connection.get_visitor_data_from_visitor_id(key_visitor_id)
    if visitor_data == []:
        return "No Such data for Visitor Id:{} exists in the database, Try entering a valid Visitor id!".format(key_visitor_id)
    else:
        visitor_data = visitor_data[0]
        fname = visitor_data[1]
        lname = visitor_data[2]
        addr = visitor_data[3]
        pin_code = visitor_data[4]
        mob_no = visitor_data[5]
        email_id = visitor_data[6]
        date_time = visitor_data[7]
        gender = visitor_data[8]
        # [(3, 'Kanan', 'Sudhakaran', 'Mumbai', '400039', '87797982100', 'swabhav@somaiya.edu', datetime.datetime(2020, 1, 1, 0, 0), 'M')]
        return render_template('update_visitor_page.html', fname=fname, lname=lname, addr=addr, pin_code=pin_code, mob_no=mob_no,
                               email_id=email_id, date_time=date_time, gender=gender, key_visitor_id=key_visitor_id)


@app.route("/visitor_updation_process/<key_visitor_id>", methods=['POST', 'GET'])
def visitor_updation_process(key_visitor_id):
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        addr = request.form['addr']
        pin_code = request.form['pin_code']
        mob_no = request.form['mob_no']
        email_id = request.form['email_id']
        date_of_birth = request.form['date_time']
        gender = request.form['gender'].upper()
        return redirect(url_for('updateVisitor_result', fname=fname, lname=lname, addr=addr, pin_code=pin_code,
                                mob_no=mob_no, email_id=email_id, date_of_birth=date_of_birth, gender=gender,
                                key_visitor_id=key_visitor_id ))
    else:

        fname = request.args.get('fname')
        lname = request.args.get('lname')
        addr = request.args.get('addr')
        pin_code = request.args.get('pin_code')
        mob_no = request.args.get('mob_no')
        email_id = request.args.get('email_id')
        date_of_birth = request.args.get('date_time')
        gender = request.args.get('gender').upper()
        message = connection.update_visitor_data(fname, lname, addr, pin_code, mob_no, email_id, date_of_birth, gender
                                                 , key_visitor_id)

        return redirect(url_for('updateVisitor_result', fname=fname, lname=lname, addr=addr, pin_code=pin_code,
                                mob_no=mob_no, email_id=email_id, date_of_birth=date_of_birth, gender=gender,
                                key_visitor_id=key_visitor_id ))

@app.route("/updateVisitor_result/<key_visitor_id>/<fname>/<lname>/<addr>/<pin_code>/<mob_no>/<email_id>/<date_of_birth>/<gender>")
def updateVisitor_result(fname, lname, addr, pin_code, mob_no, email_id, date_of_birth, gender, key_visitor_id):
    key_visitor_id = int(key_visitor_id)

    message = connection.update_visitor_data(fname, lname, addr, pin_code, mob_no, email_id, date_of_birth, gender,
                                             key_visitor_id)

    visitor_table = connection.get_visitor_table()
    return render_template('updateVisitor_result.html', message=message, visitor_table=visitor_table)

# ####################################______VENUE_____###################################################

# put_venue_id() loads the html page which takes VENUE ID as its input
@app.route('/put_venue_id')
def put_venue_id():
    venue_table = connection.get_venue_table()
    return render_template('put_venue_id.html',venue_table=venue_table)

# pass_venue_id() grabs the VENUE ID from the REQUEST received from put_venue_id.html page and passes it to get_venue_id()
@app.route("/pass_venue_id",methods = ['POST', 'GET'])
def pass_venue_id():
    if request.method == 'POST':
        venue_id = int(request.form['venue_id'])
        return redirect(url_for('get_venue_id', venue_id=venue_id))
    else:
        venue_id = int(request.args.get('venue_id'))
        return redirect(url_for('get_venue_id', venue_id=venue_id))

'''
get_venue_id() does the following operations :

* Checks if DATA for VENUE ID entered by the USER exists in the DATABASE or not -> ( True , False )

      (if data EXISTS) : 
              Extract the DATA from VENUE TABLE for corresponding VENUE ID entered by the User and pass it to 
              update_venue_page.html so that the OLD DATA is visible to the User and User can UPDATE DATA in the
              INPUT FIELDS as per their convenience and SUBMIT the data
    
      (if data DOES NOT EXISTS) =>
              print ERROR STATEMENT
'''
@app.route("/get_venue_id/<venue_id>")
def get_venue_id(venue_id):
    key_venue_id = int(venue_id)
    venue_data = connection.get_venue_data_from_venue_id(int(venue_id))
    if venue_data == []:
        return "No Such data for Venue id:{} exists in the database, Try entering a valid Venue id!".format(key_venue_id)
    else:
        venue_data = venue_data[0]
        venue_city = venue_data[1]
        venue_addr = venue_data[2]
        country_id = venue_data[3]
        state_id = venue_data[4]

        state_table = connection.get_state_table()
        country_table = connection.get_country_table()

        return render_template('update_venue_page.html',state_table=state_table, country_table=country_table ,
                               venue_city=venue_city ,venue_addr=venue_addr,country_id=country_id,state_id=state_id,
                               key_venue_id=key_venue_id)

@app.route("/venue_updation_process/<key_venue_id>",methods=['POST', 'GET'])
def venue_updation_process(key_venue_id):
    if request.method == 'POST':
        '''
        # +------------+--------------+------+-----+---------+----------------+
        # | Field      | Type         | Null | Key | Default | Extra          |
        # +------------+--------------+------+-----+---------+----------------+
        # | venue_id   | int          | NO   | PRI | NULL    | auto_increment |
        # | venue_city | varchar(255) | YES  |     | NULL    |                |
        # | venue_addr | varchar(255) | YES  |     | NULL    |                |
        # | country_id | int          | YES  | MUL | NULL    |                |
        # | state_id   | int          | YES  | MUL | NULL    |                |
        # +------------+--------------+------+-----+---------+-------
        '''
        venue_city = request.form['venue_city']
        venue_addr = request.form['venue_addr']
        country_id = request.form['country_id']
        state_id = request.form['state_id']
        return redirect(url_for('updateVenue_result', key_venue_id=key_venue_id, venue_city=venue_city, venue_addr=venue_addr, country_id=country_id, state_id=state_id))
    else:
        venue_city = request.args.get('venue_city')
        venue_addr = request.args.get('venue_addr')
        country_id = request.args.get('country_id')
        state_id = request.args.get('state_id')
        return redirect(url_for('updateVenue_result', key_venue_id=key_venue_id, venue_city=venue_city, venue_addr=venue_addr, country_id=country_id, state_id=state_id))

@app.route("/updateVenue_result/<key_venue_id>/<venue_city>/<venue_addr>/<country_id>/<state_id>")
def updateVenue_result(key_venue_id,venue_city,venue_addr,country_id,state_id):
    key_venue_id = int(key_venue_id)
    state_id = int(state_id)
    country_id = int(country_id)

    # state_id_verified => True or False
    state_id_verified = connection.verify_state_id(state_id)
    country_id_verified = connection.verify_country_id(country_id)


    if (state_id_verified=="Verified") and (country_id_verified == "Verified"):
        message = connection.update_venue_data(venue_city,venue_addr,country_id,state_id,key_venue_id)
        venue_table = connection.get_venue_table()

        return render_template('updateVenue_result.html',message = message,venue_table=venue_table)
    else :
        message = "Table not Updated!! : State ID is {} and Country Id is {}, Please enter valid data (REFER STATE_COUNTRY TABLE ON THE PREVIOUS PAGE)".format(state_id_verified,country_id_verified)
        return '''
        <body>
        {}
        </body>
        '''.format(message)

        # return render_template('updateVenue_result.html', message=message)
# ####################################______EVENT_____###################################################

@app.route('/put_event_id')
def put_event_id():
    event_table = connection.get_event_table()
    return render_template('put_event_id.html',event_table=event_table)

@app.route("/pass_event_id",methods = ['POST', 'GET'])
def pass_event_id():
    if request.method == 'POST':
        event_id = int(request.form['event_id'])
        return redirect(url_for('get_event_id', event_id=event_id))
    else:
        event_id = int(request.args.get('event_id'))
        return redirect(url_for('get_event_id', event_id=event_id))

@app.route("/get_event_id/<event_id>")
def get_event_id(event_id):
    key_event_id = int(event_id)
    event_data = connection.get_event_data_from_event_id(key_event_id)
    if event_data == []:
        return "No Such data for Event Id:{} exists in the database, Try entering a valid Event id!".format(key_event_id)
    else:
        event_data = event_data[0]
        event_id = event_data[0]
        event_name = event_data[1]
        booking_start_date = event_data[2]
        event_start_date = event_data[3]
        event_end_date = event_data[4]
        venue_id = event_data[5]
        # +----------+------------+---------------------+---------------------+---------------------+--
        # | event_id | event_name | booking_start_date | event_start_date | event_end_date | venue_id |
        # +----------+------------+---------------------+---------------------+---------------------+--

        venue_table = connection.get_venue_table()
        return render_template('update_event_page.html',venue_table=venue_table, event_name=event_name ,booking_start_date=booking_start_date,event_start_date=event_start_date, event_end_date=event_end_date , key_event_id=key_event_id, venue_id=venue_id)

@app.route("/event_updation_process/<key_event_id>",methods=['POST', 'GET'])
def event_updation_process(key_event_id):
    if request.method == 'POST':
        event_name = request.form['event_name']
        booking_start_date = request.form['booking_start_date']
        event_start_date = request.form['event_start_date']
        event_end_date = request.form['event_end_date']
        venue_id = request.form['venue_id']
        return redirect(url_for('updateEvent_result', key_event_id=key_event_id,venue_id=venue_id,event_start_date=event_start_date, event_name=event_name, booking_start_date=booking_start_date,event_end_date=event_end_date))
    else:
        event_name = request.args.get('event_name')
        booking_start_date = request.args.get('booking_start_date')
        event_start_date = request.args.get('event_start_date')
        event_end_date = request.args.get('event_end_date')
        venue_id = request.args.get('venue_id')
        return redirect(url_for('updateEvent_result', key_event_id=key_event_id,venue_id=venue_id,event_start_date=event_start_date, event_name=event_name, booking_start_date=booking_start_date,event_end_date=event_end_date))

#    event_name | booking_start_date | event_start_date | event_end_date | venue_id |

@app.route("/updateEvent_result/<key_event_id>/<event_name>/<booking_start_date>/<event_start_date>/<event_end_date>/<venue_id>")
def updateEvent_result(key_event_id,event_name,booking_start_date,event_start_date,event_end_date,venue_id):
    key_event_id = int(key_event_id)
    venue_id = int(venue_id)

    # venue_id_verified => "Verified" or "Not Verified"
    venue_id_verified = connection.verify_venue_id(venue_id)


    if (venue_id_verified=="Verified"):
        message = connection.update_event_data(key_event_id, event_name, booking_start_date,
                                               event_start_date, event_end_date, venue_id)
        event_table = connection.get_event_table()

        return render_template('updateEvent_result.html',message = message,event_table=event_table)
    else :
        message = "Table not Updated!! : Venue ID is {}, Please enter valid data (REFER VENUE TABLE ON THE PREVIOUS PAGE)".format(venue_id_verified)
        return '''
        <body>
        {}
        </body>
        '''.format(message)

        # return render_template('updateVenue_result.html', message=message)


# ####################################______STALL_____###################################################


@app.route('/put_stall_id')
def put_stall_id():
    stall_table = connection.get_stall_table()
    return render_template('put_stall_id.html', stall_table=stall_table)


@app.route("/extract_stallId_from_request", methods=['POST', 'GET'])
def extract_stallId_from_request():
    if request.method == 'POST':
        stall_id = int(request.form['stall_id'])
        return redirect(url_for('extract_stallData_using_stallId', stall_id=stall_id))
    else:
        stall_id = int(request.args.get('stall_id'))
        return redirect(url_for('extract_stallData_using_stallId', stall_id=stall_id))


@app.route("/extract_stallData_using_stallId/<stall_id>")
def extract_stallData_using_stallId(stall_id):
    key_stall_id = int(stall_id)
    stall_data = connection.get_stall_data_from_stall_id(key_stall_id)
    if stall_data == []:
        return "No Such data for Stall Id:{} exists in the database, Try entering a valid Stall id!".format(key_stall_id)
    else:
        stall_data = stall_data[0]
        stall_id = stall_data[0]
        stall_no = stall_data[1]
        stall_price = stall_data[2]
        stall_size = stall_data[3]
        is_booked = stall_data[4]
        event_id = stall_data[5]

        event_table = connection.get_event_table()
        return render_template('update_stall_page.html', event_table=event_table, stall_no=stall_no, stall_price=stall_price, stall_size=stall_size,
                               is_booked=is_booked, event_id=event_id, key_stall_id=key_stall_id)


@app.route("/stall_updation_process/<key_stall_id>", methods=['POST', 'GET'])
def stall_updation_process(key_stall_id):

    if request.method == 'POST':
        stall_no = request.form['stall_no']
        stall_price = request.form['stall_price']
        stall_size = request.form['stall_size']
        is_booked = request.form['is_booked']
        event_id = request.form['event_id']
        return redirect(url_for('updateStall_result', key_stall_id=key_stall_id, stall_no=stall_no,
                                stall_price=stall_price, stall_size=stall_size,
                                is_booked=is_booked, event_id=event_id))
    else:
        stall_no = request.args.get('stall_no')
        stall_price = request.args.get('stall_price')
        stall_size = request.args.get('stall_size')
        is_booked = request.args.get('is_booked')
        event_id = request.args.get('event_id')
        return redirect(url_for('updateStall_result', key_stall_id=key_stall_id, stall_no=stall_no,
                                stall_price=stall_price, stall_size=stall_size,
                                is_booked=is_booked, event_id=event_id))
    # +----------+------------+---------------------+---------------------+--------
    # | | stall_id | stall_no | stall_price | stall_size | is_booked | event_id  |
    # +----------+------------+---------------------+---------------------+--------
@app.route("/updateStall_result/<key_stall_id>/<stall_no>/<stall_price>/<stall_size>/<is_booked>/<event_id>")
def updateStall_result(key_stall_id, stall_no, stall_price, stall_size, is_booked, event_id):
    key_stall_id = int(key_stall_id)
    event_id = int(event_id)
    stall_no = int(stall_no)
    stall_price = float(stall_price)
    stall_size = float(stall_size)
    # event_id_verified => "Verified" or "Not Verified"
    event_id_verified = connection.verify_stall_id(event_id)

    if (event_id_verified == "Verified"):
        message = connection.update_stall_data(key_stall_id, stall_no, stall_price, stall_size, is_booked, event_id)
        stall_table = connection.get_stall_table()

        return render_template('updateStall_result.html', message=message, stall_table=stall_table)
    else:
        message = "Table not Updated!! : Event ID is {}, Please enter valid data (REFER EVENT TABLE ON THE PREVIOUS PAGE)".format(
            event_id_verified)
        return '''
        <body>
        {}
        </body>
        '''.format(message)


# ####################################______EXHIBITOR_____###################################################

@app.route('/put_exhibitor_id')
def put_exhibitor_id():
    exhibitor_table = connection.get_exhibitor_table()
    return render_template('put_exhibitor_id.html', exhibitor_table=exhibitor_table)


@app.route("/extract_exhibitorId_from_request", methods=['POST', 'GET'])
def extract_exhibitorId_from_request():
    if request.method == 'POST':
        exhibitor_id = int(request.form['exhibitor_id'])
        return redirect(url_for('extract_exhibitorData_using_exhibitorId', exhibitor_id=exhibitor_id))
    else:
        exhibitor_id = int(request.args.get('exhibitor_id'))
        return redirect(url_for('extract_exhibitorData_using_exhibitorId', exhibitor_id=exhibitor_id))


@app.route("/extract_exhibitorData_using_exhibitorId/<exhibitor_id>")
def extract_exhibitorData_using_exhibitorId(exhibitor_id):
    key_exhibitor_id = int(exhibitor_id)
    exhibitor_data = connection.get_exhibitor_data_from_exhibitor_id(key_exhibitor_id)
    if exhibitor_data == []:
        return "No Such data for Stall Id:{} exists in the database, Try entering a valid Stall id!".format(key_exhibitor_id)
    else:
        exhibitor_data = exhibitor_data[0]
        exhibitor_id = exhibitor_data[0]
        exhibitor_name = exhibitor_data[1]
        email_id = exhibitor_data[2]
        phone_no = exhibitor_data[3]
        company_name = exhibitor_data[4]
        company_description = exhibitor_data[5]
        company_addr = exhibitor_data[6]
        company_pin_code = exhibitor_data[7]
        industry_id = exhibitor_data[8]
        country_id = exhibitor_data[9]
        state_id = exhibitor_data[10]

        exhibitor_state_country_table = connection.join_exhibitor_state_country_table()
        return render_template('update_exhibitor_page.html',exhibitor_state_country_table=exhibitor_state_country_table,
                               exhibitor_name=exhibitor_name, email_id=email_id,company_name=company_name, phone_no=phone_no,
                               company_description=company_description, company_addr=company_addr,company_pin_code=company_pin_code,
                               industry_id=industry_id, country_id=country_id, state_id=state_id, key_exhibitor_id=key_exhibitor_id)


@app.route("/exhibitor_updation_process/<key_exhibitor_id>", methods=['POST', 'GET'])
def exhibitor_updation_process(key_exhibitor_id):

    if request.method == 'POST':
        exhibitor_name = request.form['exhibitor_name']
        email_id = request.form['email_id']
        phone_no = request.form['phone_no']
        company_name = request.form['company_name']
        company_description = request.form['company_description']
        company_addr = request.form['company_addr']
        company_pin_code = request.form['company_pin_code']
        industry_id = request.form['industry_id']
        country_id = request.form['country_id']
        state_id = request.form['state_id']

        return redirect(url_for('updateExhibitor_result', key_exhibitor_id=key_exhibitor_id, exhibitor_name=exhibitor_name,
                                email_id=email_id, phone_no=phone_no, company_name=company_name,
                                company_description=company_description,company_addr=company_addr,
                                company_pin_code=company_pin_code, industry_id=industry_id,
                                country_id=country_id, state_id=state_id))
    else:
        # exhibitor_id | exhibitor_name | email_id | phone_no | company_name | company_description | company_addr |
        # company_pin_code | industry_id | country_id | state_id
        exhibitor_name = request.args.get('exhibitor_name')
        email_id = request.args.get('email_id')
        phone_no = request.args.get('phone_no')
        company_name = request.args.get('company_name')
        company_description = request.args.get('company_description')
        company_address = request.args.get('company_address')
        company_pin_code = request.args.get('company_pin_code')
        industry_id = request.args.get('industry_id')
        country_id = request.args.get('country_id')
        state_id = request.args.get('state_id')

        return redirect(url_for('updateExhibitor_result', key_exhibitor_id=key_exhibitor_id, exhibitor_name=exhibitor_name,
                                email_id=email_id, phone_no=phone_no, company_name=company_name,
                                company_description=company_description, company_address=company_address,
                                company_pin_code=company_pin_code, industry_id=industry_id,
                                country_id=country_id, state_id=state_id))

@app.route("/updateExhibitor_result/<key_exhibitor_id>/<exhibitor_name>/<email_id>/<phone_no>/<company_name>/"
           "<company_description>/<company_addr>/<company_pin_code>/<industry_id>/<country_id>/<state_id>")
def updateExhibitor_result(key_exhibitor_id, exhibitor_name, email_id, phone_no, company_name,company_description,
                           company_addr, company_pin_code, industry_id, country_id, state_id):

    key_exhibitor_id = int(key_exhibitor_id)
    industry_id = int(industry_id)
    company_pin_code = int(company_pin_code)
    country_id = int(country_id)
    state_id = int(state_id)

    # state_id_verified => "Verified" or "Not Verified"
    state_id_verified = connection.verify_state_id(state_id)
    country_id_verified = connection.verify_country_id(country_id)
    industry_id_verified = connection.verify_industry_id(industry_id)

    if state_id_verified == "Verified" and country_id_verified == "Verified" and industry_id_verified == "Verified":
        message = connection.update_exhibitor_data(key_exhibitor_id, exhibitor_name, email_id, phone_no,
                                                   company_name, company_description, company_addr, company_pin_code,
                                                   industry_id, country_id, state_id)
        exhibitor_table = connection.get_exhibitor_table()

        return render_template('updateExhibitor_result.html', message=message, exhibitor_table=exhibitor_table)
    else:
        message = "Table not Updated!! : Country ID is {} , State ID is {} and Industry ID is {}," \
                  " Please enter valid data (REFER INDUSTRY_STATE_COUNTRY TABLE ON THE PREVIOUS PAGE AND RE-INPUT )".format(country_id_verified,
                                                                                                                             state_id_verified,
                                                                                                                             industry_id_verified)
        return '''
        <body>
        {}
        </body>
        '''.format(message)


# ####################################______BOOKING_____###################################################

 # booking_id | booking_date | total_amount | event_id | exhibitor_id

@app.route('/put_booking_id')
def put_booking_id():
    booking_table = connection.get_booking_table()
    return render_template('put_booking_id.html', booking_table=booking_table)


@app.route("/extract_bookingId_from_request", methods=['POST', 'GET'])
def extract_bookingId_from_request():
    if request.method == 'POST':
        booking_id = int(request.form['booking_id'])
        return redirect(url_for('extract_bookingData_using_bookingId', booking_id=booking_id))
    else:
        booking_id = int(request.args.get('booking_id'))
        return redirect(url_for('extract_bookingData_using_bookingId', booking_id=booking_id))


@app.route("/extract_bookingData_using_bookingId/<booking_id>")
def extract_bookingData_using_bookingId(booking_id):
    key_booking_id = int(booking_id)
    booking_data = connection.get_booking_data_from_booking_id(key_booking_id)
    if booking_data == []:
        return "No Such data for Booking Id:{} exists in the database, Try entering a valid Booking id!".format(key_booking_id)
    else:
        # | booking_id | booking_date | total_amount | event_id | exhibitor_id |
        booking_data = booking_data[0]
        booking_id = booking_data[0]
        booking_date = booking_data[1]
        total_amount = booking_data[2]
        event_id = booking_data[3]
        exhibitor_id = booking_data[4]

        event_table = connection.get_event_table()
        exhibitor_table = connection.get_exhibitor_table()
        return render_template('update_booking_page.html',event_table=event_table, exhibitor_table=exhibitor_table,
                               booking_date=booking_date, total_amount=total_amount, exhibitor_id=exhibitor_id,
                               event_id=event_id, key_booking_id=key_booking_id)


@app.route("/booking_updation_process/<key_booking_id>", methods=['POST', 'GET'])
def booking_updation_process(key_booking_id):
    # | booking_id | booking_date | total_amount | event_id | exhibitor_id |
    if request.method == 'POST':
        booking_date = request.form['booking_date']
        total_amount = request.form['total_amount']
        event_id = request.form['event_id']
        exhibitor_id = request.form['exhibitor_id']
        return redirect(url_for('updateBooking_result', key_booking_id=key_booking_id, booking_date=booking_date,
                                total_amount=total_amount, exhibitor_id=exhibitor_id, event_id=event_id))
    else:
        booking_date = request.args.get('booking_date')
        total_amount = request.args.get('total_amount')
        exhibitor_id = request.args.get('exhibitor_id')
        event_id = request.args.get('event_id')
        return redirect(url_for('updateBooking_result', key_booking_id=key_booking_id, booking_date=booking_date,
                                total_amount=total_amount, exhibitor_id=exhibitor_id, event_id=event_id))

@app.route("/updateBooking_result/<key_booking_id>/<booking_date>/<total_amount>/<exhibitor_id>/<event_id>")
def updateBooking_result(key_booking_id, booking_date, total_amount, exhibitor_id, event_id):

    key_booking_id = int(key_booking_id)
    total_amount = float(total_amount)
    event_id = int(event_id)
    exhibitor_id = int(exhibitor_id)

    # event_id_verified => "Verified" or "Not Verified"
    event_id_verified = connection.verify_event_id(event_id)
    exhibitor_id_verified = connection.verify_exhibitor_id(exhibitor_id)

    if event_id_verified == "Verified" and exhibitor_id_verified == "Verified" :
        message = connection.update_booking_data(key_booking_id, total_amount, booking_date, exhibitor_id, event_id)
        booking_table = connection.get_booking_table()

        return render_template('updateBooking_result.html', message=message, booking_table=booking_table)
    else:
        message = "Table not Updated!! : Event ID is {} and Exhibitor ID is {}, Please enter valid data (REFER EVENT AND EXHIBITOR TABLE ON THE PREVIOUS PAGE)".format(
            event_id_verified, exhibitor_id_verified)
        return '''
        <body>
        {}
        </body>
        '''.format(message)

# ####################################______MEGA_CONSUMER_CARD_____###################################################


@app.route('/put_mccard_id')
def put_mccard_id():
    mccard_table = connection.get_mega_consumner_card_table()
    return render_template('put_mccard_id.html', mccard_table=mccard_table)

@app.route("/extract_mccardId_from_request", methods=['POST', 'GET'])
def extract_mccardId_from_request():
    if request.method == 'POST':
        mccard_id = int(request.form['mccard_id'])
        return redirect(url_for('extract_mccardData_using_mccardId', mccard_id=mccard_id))
    else:
        mccard_id = int(request.args.get('mccard_id'))
        return redirect(url_for('extract_mccardData_using_mccardId', mccard_id=mccard_id))


@app.route("/extract_mccardData_using_mccardId/<mccard_id>")
def extract_mccardData_using_mccardId(mccard_id):
    key_mccard_id = int(mccard_id)
    mccard_data = connection.get_mccard_data_from_mccard_id(key_mccard_id)
    if mccard_data == []:
        return "No Such data for Card Id:{} exists in the database, Try entering a valid Card id!".format(key_mccard_id)
    else:
        # card_id | spend_amt | spend_date | payment_mode | event_id | booking_id | visitor_id |
        mccard_data = mccard_data[0]
        card_id = mccard_data[0]
        spend_amt = mccard_data[1]
        spend_date = mccard_data[2]
        payment_mode = mccard_data[3]
        event_id = mccard_data[4]
        booking_id = mccard_data[5]
        visitor_id = mccard_data[6]

        event_table = connection.get_event_table()
        booking_table = connection.get_booking_table()
        visitor_table = connection.get_visitor_table()

        return render_template('update_mccard_page.html', event_table=event_table, booking_table=booking_table,
                               visitor_table=visitor_table, spend_amt=spend_amt, spend_date=spend_date,
                               payment_mode=payment_mode, booking_id=booking_id, visitor_id=visitor_id,
                               event_id=event_id, key_mccard_id=key_mccard_id)


@app.route("/mccard_updation_process/<key_mccard_id>", methods=['POST', 'GET'])
def mccard_updation_process(key_mccard_id):
    # card_id | spend_amt | spend_date | payment_mode | event_id | booking_id | visitor_id |
    if request.method == 'POST':
        spend_amt = request.form['spend_amt']
        spend_date = request.form['spend_date']
        payment_mode = request.form['payment_mode']
        event_id = request.form['event_id']
        booking_id = request.form['booking_id']
        visitor_id = request.form['visitor_id']


        return redirect(url_for('updateMccard_result', key_mccard_id=key_mccard_id, spend_amt=spend_amt,
                                spend_date=spend_date, payment_mode=payment_mode, event_id=event_id,
                                booking_id=booking_id, visitor_id=visitor_id))
    else:
        spend_amt = request.args.get('spend_amt')
        spend_date = request.args.get('spend_date')
        payment_mode = request.args.get('payment_mode')
        booking_id = request.args.get('booking_id')
        visitor_id = request.args.get('visitor_id')
        event_id = request.args.get('event_id')

        return redirect(url_for('updateMccard_result', key_mccard_id=key_mccard_id, spend_amt=spend_amt,
                                spend_date=spend_date, payment_mode=payment_mode, event_id=event_id,
                                booking_id=booking_id, visitor_id=visitor_id))

@app.route("/updateMccard_result/<key_mccard_id>/<spend_amt>/<spend_date>/<payment_mode>/<event_id>/<booking_id>/<visitor_id>")
def updateMccard_result(key_mccard_id, spend_amt, spend_date, payment_mode, event_id, booking_id, visitor_id):

    key_mccard_id = int(key_mccard_id)
    spend_amt = float(spend_amt)
    event_id = int(event_id)
    booking_id = int(booking_id)
    visitor_id = int(visitor_id)

    # event_id_verified => "Verified" or "Not Verified"
    event_id_verified = connection.verify_event_id(event_id)
    booking_id_verified = connection.verify_booking_id(booking_id)
    visitor_id_verified = connection.verify_visitor_id(visitor_id)

    # key_mccard_id, spend_amt, spend_date, payment_mode, event_id, booking_id, visitor_id

    if event_id_verified == "Verified" and booking_id_verified == "Verified" and visitor_id_verified == "Verified" :
        message = connection.update_mccard_data(key_mccard_id, spend_amt, spend_date, payment_mode, event_id, booking_id, visitor_id)
        mccard_table = connection.get_mega_consumner_card_table()

        return render_template('updateMccard_result.html', message=message, mccard_table=mccard_table)
    else:
        message = "Table not Updated!! Please enter valid data (REFER EVENT, BOOKING AND VISITOR TABLE ON THE PREVIOUS PAGE)<br>" \
                  "Event ID is {} <br> Booking ID is {} <br>  Visitor ID is {} <br> ".format(
            event_id_verified, booking_id_verified,visitor_id_verified)
        return '''
        <body>
        {}
        </body>
        '''.format(message)

# ####################################______INDUSTRY_____###################################################
@app.route('/put_industry_id')
def put_industry_id():
    industry_table = connection.get_industry_table()
    return render_template('put_industry_id.html', industry_table=industry_table)

@app.route("/extract_industryId_from_request", methods=['POST', 'GET'])
def extract_industryId_from_request():
    if request.method == 'POST':
        industry_id = int(request.form['industry_id'])
        return redirect(url_for('extract_industryData_using_industryId', industry_id=industry_id))
    else:
        industry_id = int(request.args.get('industry_id'))
        return redirect(url_for('extract_industryData_using_industryId', industry_id=industry_id))


@app.route("/extract_industryData_using_industryId/<industry_id>")
def extract_industryData_using_industryId(industry_id):
    key_industry_id = int(industry_id)
    industry_data = connection.get_industry_data_from_industry_id(key_industry_id)
    if industry_data == []:
        return "No Such data for Industry Id:{} exists in the database, Try entering a valid Industry id!".format(key_industry_id)
    else:
        industry_data = industry_data[0]
        industry_name = industry_data[1]

        return render_template('update_industry_page.html', industry_name=industry_name, key_industry_id=key_industry_id)


@app.route("/industry_updation_process/<key_industry_id>", methods=['POST', 'GET'])
def industry_updation_process(key_industry_id):
    if request.method == 'POST':
        industry_name = request.form['industry_name']
        return redirect(url_for('updateIndustry_result', key_industry_id=key_industry_id, industry_name=industry_name))
    else:
        industry_name = request.args.get('industry_name')
        return redirect(url_for('updateIndustry_result', key_industry_id=key_industry_id, industry_name=industry_name))

@app.route("/updateIndustry_result/<key_industry_id>/<industry_name>")
def updateIndustry_result(key_industry_id, industry_name):
    key_industry_id = int(key_industry_id)
    message = connection.update_industry_data(key_industry_id, industry_name)
    industry_table = connection.get_industry_table()
    return render_template('updateIndustry_result.html', message=message, industry_table=industry_table)

# ####################################______COUNTRY_____###################################################

@app.route('/put_country_id')
def put_country_id():
    country_table = connection.get_country_table()
    return render_template('put_country_id.html', country_table=country_table)

@app.route("/extract_countryId_from_request", methods=['POST', 'GET'])
def extract_countryId_from_request():
    if request.method == 'POST':
        country_id = int(request.form['country_id'])
        return redirect(url_for('extract_countryData_using_countryId', country_id=country_id))
    else:
        country_id = int(request.args.get('country_id'))
        return redirect(url_for('extract_countryData_using_countryId', country_id=country_id))


@app.route("/extract_countryData_using_countryId/<country_id>")
def extract_countryData_using_countryId(country_id):
    key_country_id = int(country_id)
    country_data = connection.get_country_data_from_country_id(key_country_id)
    if country_data == []:
        return "No Such data for Country Id:{} exists in the database, Try entering a valid Country id!".format(key_country_id)
    else:
        country_data = country_data[0]
        country_name = country_data[1][:]

        return render_template('update_country_page.html', country_name=country_name, key_country_id=key_country_id)


@app.route("/country_updation_process/<key_country_id>", methods=['POST', 'GET'])
def country_updation_process(key_country_id):
    if request.method == 'POST':
        country_name = request.form['country_name']
        return redirect(url_for('updateCountry_result', key_country_id=key_country_id, country_name=country_name))
    else:
        country_name = request.args.get('country_name')
        return redirect(url_for('updateCountry_result', key_country_id=key_country_id, country_name=country_name))

@app.route("/updateCountry_result/<key_country_id>/<country_name>")
def updateCountry_result(key_country_id, country_name):
    key_country_id = int(key_country_id)
    message = connection.update_country_data(key_country_id, country_name)
    country_table = connection.get_country_table()
    return render_template('updateCountry_result.html', message=message, country_table=country_table)

# ####################################______STATE_____###################################################

@app.route('/put_state_id')
def put_state_id():
    state_table = connection.get_state_table()
    return render_template('put_state_id.html', state_table=state_table)

@app.route("/extract_stateId_from_request", methods=['POST', 'GET'])
def extract_stateId_from_request():
    if request.method == 'POST':
        state_id = int(request.form['state_id'])
        return redirect(url_for('extract_stateData_using_stateId', state_id=state_id))
    else:
        state_id = int(request.args.get('state_id'))
        return redirect(url_for('extract_stateData_using_stateId', state_id=state_id))


@app.route("/extract_stateData_using_stateId/<state_id>")
def extract_stateData_using_stateId(state_id):
    key_state_id = int(state_id)
    state_data = connection.get_state_data_from_state_id(key_state_id)
    if state_data == []:
        return "No Such data for State Id:{} exists in the database, Try entering a valid State id!".format(key_state_id)
    else:
        state_data = state_data[0]
        state_name = state_data[1]

        return render_template('update_state_page.html', state_name=state_name, key_state_id=key_state_id)


@app.route("/state_updation_process/<key_state_id>", methods=['POST', 'GET'])
def state_updation_process(key_state_id):
    if request.method == 'POST':
        state_name = request.form['state_name']
        return redirect(url_for('updateState_result', key_state_id=key_state_id, state_name=state_name))
    else:
        state_name = request.args.get('state_name')
        return redirect(url_for('updateState_result', key_state_id=key_state_id, state_name=state_name))

@app.route("/updateState_result/<key_state_id>/<state_name>")
def updateState_result(key_state_id, state_name):
    key_state_id = int(key_state_id)
    message = connection.update_state_data(key_state_id, state_name)
    state_table = connection.get_state_table()
    return render_template('updateState_result.html', message=message, state_table=state_table)
=======
from flask import Flask, redirect, jsonify, url_for, request, render_template
import connection
from Dashboards import booking
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/")
def home():
    visitor = connection.new_disp_visitor()
    return render_template("new_home.html", data=visitor)


@app.route("/choose_id_or_num")
def choose_id_or_num():
    return render_template("new_choose_id_or_num.html")


@app.route("/get_id", methods=["POST", "GET"])
def get_id():
    if request.method == "POST":
        email = request.form["email"]
        return redirect(url_for("update_data", email=email))
    else:
        email = request.args.get("email")
        return redirect(url_for("update_data", email=email))


@app.route("/update_data/<email>")
def update_data(email):
    return render_template("new_update.html", email=email)


@app.route("/get_name" + "/<email>")
def get_name(email):
    return render_template("new_update_name.html", email=email)


@app.route("/update_name/<email>")
def update_name(email):
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        return redirect(url_for("disp_message", fname=fname, lname=lname, email=email))
    else:
        fname = request.args.get("fname")
        lname = request.args.get("lname")
        return redirect(url_for("disp_message", fname=fname, lname=lname, email=email))
>>>>>>> 1bd8e154d9ce5e8e68956cf2690f086d973f5af8

#
# from Dashboards import booking
# import matplotlib.pyplot as plt
#
# app = Flask(__name__)

<<<<<<< HEAD
#
# @app.route("/")
# def home():
#     visitor = connection.new_disp_visitor()
#     return render_template("new_home.html", data=visitor)
#
#
# @app.route("/choose_id_or_num")
# def choose_id_or_num():
#     return render_template("new_choose_id_or_num.html")
#
#
# @app.route("/get_id", methods=["POST", "GET"])
# def get_id():
#     if request.method == "POST":
#         email = request.form["email"]
#         return redirect(url_for("update_data", email=email))
#     else:
#         email = request.args.get("email")
#         return redirect(url_for("update_data", email=email))
#
#
# @app.route("/update_data/<email>")
# def update_data(email):
#     return render_template("new_update.html", email=email)
#
#
# @app.route("/get_name" + "/<email>")
# def get_name(email):
#     return render_template("new_update_name.html", email=email)
#
#
# @app.route("/update_name/<email>")
# def update_name(email):
#     if request.method == "POST":
#         fname = request.form["fname"]
#         lname = request.form["lname"]
#         return redirect(url_for("disp_message", fname=fname, lname=lname, email=email))
#     else:
#         fname = request.args.get("fname")
#         lname = request.args.get("lname")
#         return redirect(url_for("disp_message", fname=fname, lname=lname, email=email))
#
#
# @app.route("/disp_message/<fname>/<lname>/<email>")
# def disp_message(fname, lname, email):
#     data = connection.update_name(fname, lname, email)
#     return render_template("new_disp_message.html", data=data)
#
#
# @app.route("/booking")
# def booking_dashboard():
#
#     return render_template(
#         "booking_dash.html",
#         name=booking.booking_dash([1, 2, 3], [2, 3, 5]),
#         label=["Mon", "Tue", "Wed", "Thu", "Fri"],
#         serie=[5, 2, 4, 2, 0],
#     )
#
=======
@app.route("/disp_message/<fname>/<lname>/<email>")
def disp_message(fname, lname, email):
# <<<<<<< HEAD
    data = connection.update_name(fname,lname,email)
    return render_template('new_disp_message.html',data=data)

@app.route("/new_visitor",methods=['GET'])
def new_visitor():
        return render_template('new_visitor.html')
        fname = request.form['fname']
        lname = request.form['lname']
        addr = request.form['addr']
        pin = request.form['pin']
        mob = request.form['mob']
        email = request.form['email']
        dob = request.form['dob']
        gender = request.form['gender']
        connection.insert_visitor(fname,lname,addr,pin,mob,email,dob,gender)


@app.route("/new_visitor", methods=['POST'])
def get_new_contact():
     fname = request.form['fname']
     lname = request.form['lname']
     contact = request.form['contact']
     connect.add_contact(fname, lname, contact)
     ans = connection.new_disp_visitor()
     return render_template('new_home.html', data=ans)
# # =======
#     data = connection.update_name(fname, lname, email)
#     return render_template("new_disp_message.html", data=data)


@app.route("/booking")
def booking_dashboard():

    return render_template(
        "booking_dash.html",
        name=booking.booking_dash([1, 2, 3], [2, 3, 5]),
        label=["Mon", "Tue", "Wed", "Thu", "Fri"],
        serie=[5, 2, 4, 2, 0],
    )


@app.route("/test", methods=["GET"])
def ret_book():
    # data = {"label": , }
    message = {"label": ["A", "B", "C"], "value": [1, 2, 3]}
    return jsonify(message)


@app.route("/dashboard")
def dashboard():
    print("hey")
    return render_template("charts.html", s="Sahil")

# >>>>>>> 64600e9c6b7604a39fee76453b9e4d17aa5f15f2
>>>>>>> 1bd8e154d9ce5e8e68956cf2690f086d973f5af8
