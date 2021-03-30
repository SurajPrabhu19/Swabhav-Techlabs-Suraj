from flask import Flask, redirect, jsonify, url_for, request, render_template
import connection
from Dashboards import booking
import matplotlib.pyplot as plt
import insert_check
import pandas as pd


from flask import Flask, render_template, request, redirect
import display_functions, insert_functions, delete_functions, update_functions


app = Flask(__name__)


# @app.route("/booking")
# def booking_dashboard():

#     return render_template(
#         "booking_dash.html",
#         name=booking.booking_dash([1, 2, 3], [2, 3, 5]),
#         label=["Mon", "Tue", "Wed", "Thu", "Fri"],
#         serie=[5, 2, 4, 2, 0],
#     )


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/country", methods=["GET", "POST"])
def country():
    if request.method == "POST":
        insert_functions.insert_country(request.form["country_name"])
    country_data = display_functions.display_country()
    return render_template("country.html", country_data=country_data)


@app.route("/delete/<int:country_id>")
def delete(country_id):
    delete_functions.delete_country(country_id)
    return redirect("/country")


@app.route("/update/<int:country_id>/<string:country_name>", methods=["GET", "POST"])
def update(country_id, country_name):
    if request.method == "POST":
        update_functions.update_country(request.form["country_name"], country_id)
        return redirect("/country")
    return render_template(
        "update_country.html", country_id=country_id, country_name=country_name
    )


# -------------------State----------------------
@app.route("/state", methods=["GET", "POST"])
def state():
    if request.method == "POST":
        insert_functions.insert_state(
            request.form["state_name"], request.form["country_name"]
        )
    state_data = display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template(
        "state.html", state_data=state_data, country_data=country_data
    )


@app.route("/delete_state/<int:state_id>")
def delete_state(state_id):
    delete_functions.delete_state(state_id)
    return redirect("/state")


@app.route(
    "/update/<int:state_id>/<string:state_name>/<string:country_name>",
    methods=["GET", "POST"],
)
def update_state(state_id, state_name, country_name):
    if request.method == "POST":
        update_functions.update_state(
            state_id, request.form["state_name"], request.form["country_name"]
        )
        return redirect("/state")
    country_data = display_functions.display_country()
    return render_template(
        "update_state.html",
        state_id=state_id,
        state_name=state_name,
        country_name=country_name,
        country_data=country_data,
    )


# -------------------Venue----------------------
@app.route("/venue", methods=["GET", "POST"])
def venue():
    if request.method == "POST":
        insert_functions.insert_venue(
            request.form["venue_city"],
            request.form["venue_addr"],
            request.form["state_name"],
            request.form["country_name"],
        )
    venue_data = display_functions.display_venue()
    state_data = display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template(
        "venue.html",
        venue_data=venue_data,
        state_data=state_data,
        country_data=country_data,
    )


@app.route("/delete_venue/<int:venue_id>")
def delete_venue(venue_id):
    delete_functions.delete_venue(venue_id)
    return redirect("/venue")


@app.route(
    "/update_venue/<int:venue_id>/<string:venue_city>/<string:venue_addr>/<string:state_name>/<string:country_name>",
    methods=["GET", "POST"],
)
def update_venue(venue_id, venue_city, venue_addr, state_name, country_name):
    if request.method == "POST":
        update_functions.update_venue(
            venue_id,
            request.form["venue_city"],
            request.form["venue_addr"],
            request.form["state_name"],
            request.form["country_name"],
        )
        return redirect("/venue")
    state_data = display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template(
        "update_venue.html",
        state_data=state_data,
        country_data=country_data,
        venue_id=venue_id,
        venue_city=venue_city,
        venue_addr=venue_addr,
        state_name=state_name,
        country_name=country_name,
    )


# -------------------Stall----------------------
@app.route("/stall", methods=["GET", "POST"])
def stall():
    if request.method == "POST":
        insert_functions.insert_stall(
            request.form["stall_no"],
            request.form["stall_price"],
            request.form["stall_size"],
            request.form["is_booked"],
            request.form["event_name"],
        )
    stall_data = display_functions.display_stall()
    event_data = display_functions.display_event()
    return render_template("stall.html", stall_data=stall_data, event_data=event_data)


@app.route("/delete_stall/<int:stall_id>")
def delete_stall(stall_id):
    delete_functions.delete_stall(stall_id)
    return redirect("/stall")


@app.route(
    "/update_stall/<int:stall_id>/<int:stall_no>/<float:stall_price>/<float:stall_size>/<string:is_booked>/<string:event_name>",
    methods=["GET", "POST"],
)
def update_stall(stall_id, stall_no, stall_price, stall_size, is_booked, event_name):
    if request.method == "POST":
        update_functions.update_stall(
            stall_id,
            request.form["stall_no"],
            request.form["stall_price"],
            request.form["stall_size"],
            request.form["is_booked"],
            request.form["event_name"],
        )
        return redirect("/stall")
    event_data = display_functions.display_event()
    return render_template(
        "update_stall.html",
        event_data=event_data,
        stall_id=stall_id,
        stall_no=stall_no,
        stall_price=stall_price,
        stall_size=stall_size,
        is_booked=is_booked,
        event_name=event_name,
    )


# ----------------------------Industry--------------------------------
@app.route("/industry", methods=["GET", "POST"])
def industry():
    if request.method == "POST":
        insert_functions.insert_industry(request.form["industry_name"])
    industry_data = display_functions.display_industry()
    return render_template("industry.html", industry_data=industry_data)


@app.route("/delete_industry/<int:industry_id>")
def delete_industry(industry_id):
    delete_functions.delete_industry(industry_id)
    return redirect("/industry")


@app.route(
    "/update_industry/<int:industry_id>/<string:industry_name>", methods=["GET", "POST"]
)
def update_industry(industry_id, industry_name):
    if request.method == "POST":
        update_functions.update_industry(request.form["industry_name"], industry_id)
        return redirect("/industry")
    return render_template(
        "update_industry.html", industry_id=industry_id, industry_name=industry_name
    )


# -------------------Exhibitor----------------------
@app.route("/exhibitor", methods=["GET", "POST"])
def exhibitor():
    if request.method == "POST":
        insert_functions.insert_exhibitor(
            request.form["exhibitor_name"],
            request.form["email_id"],
            request.form["phone_no"],
            request.form["company_name"],
            request.form["company_description"],
            request.form["company_addr"],
            request.form["company_pin_code"],
            request.form["industry_name"],
            request.form["state_name"],
            request.form["country_name"],
        )
    exhibitor_data = display_functions.display_exhibitor()
    industry_data = display_functions.display_industry()
    state_data = display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template(
        "exhibitor.html",
        exhibitor_data=exhibitor_data,
        industry_data=industry_data,
        state_data=state_data,
        country_data=country_data,
    )


@app.route("/delete_exhibitor/<int:exhibitor_id>")
def delete_exhibitor(exhibitor_id):
    delete_functions.delete_exhibitor(exhibitor_id)
    return redirect("/exhibitor")


@app.route(
    "/update_exhibitor/<int:exhibitor_id>/<string:exhibitor_name>/<string:email_id>/<string:phone_no>/<string:company_name>/<string:company_description>/<string:company_addr>/<int:company_pin_code>/<string:industry_name>/<string:state_name>/<string:country_name>",
    methods=["GET", "POST"],
)
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
    if request.method == "POST":
        update_functions.update_exhibitor(
            exhibitor_id,
            request.form["exhibitor_name"],
            request.form["email_id"],
            request.form["phone_no"],
            request.form["company_name"],
            request.form["company_description"],
            request.form["company_addr"],
            request.form["company_pin_code"],
            request.form["industry_name"],
            request.form["state_name"],
            request.form["country_name"],
        )
        return redirect("/exhibitor")
    industry_data = display_functions.display_industry()
    state_data = display_functions.display_state()
    country_data = display_functions.display_country()
    return render_template(
        "update_exhibitor.html",
        industry_data=industry_data,
        state_data=state_data,
        country_data=country_data,
        exhibitor_id=exhibitor_id,
        exhibitor_name=exhibitor_name,
        email_id=email_id,
        phone_no=phone_no,
        company_name=company_name,
        company_description=company_description,
        company_addr=company_addr,
        company_pin_code=company_pin_code,
        industry_name=industry_name,
        state_name=state_name,
        country_name=country_name,
    )


# -------------------MegaConsumerCard----------------------
"""    # +--------------+--------------+------+-----+---------+----------------+
    # | Field | Type | Null | Key | Default | Extra |
    # +--------------+--------------+------+-----+---------+----------------+
    # | spend_amt | int | NO | | NULL | |
    # | spend_date | datetime | NO | | NULL | |
    # | payment_mode | varchar(255) | YES | | NULL | |
    # | event_id | int | YES | MUL | NULL | |
    # | booking_id | int | YES | MUL | NULL | |
    # | visitor_id | int | YES | MUL | NULL | |
    # +--------------+--------------+------+-----+---------+----------------+

"""


@app.route("/mccard", methods=["GET", "POST"])
def mccard():
    if request.method == "POST":
        insert_functions.insert_mccard(
            int(request.form["spend_amt"]),
            request.form["spend_date"],
            request.form["payment_mode"],
            request.form["event_name"],
            request.form["email_id"],
        )
    mccard_data = display_functions.display_mccard()
    event_data = display_functions.display_event()
    visitor_data = display_functions.display_visitor()
    return render_template(
        "mccard.html",
        mccard_data=mccard_data,
        event_data=event_data,
        visitor_data=visitor_data,
    )


@app.route("/delete_mccard/<int:card_id>")
def delete_mccard(card_id):
    delete_functions.delete_mccard(card_id)
    return redirect("/mccard")


@app.route(
    "/update_mccard/<int:card_id>/<int:spend_amt>/<string:spend_date>/<string:payment_mode>/<string:event_name>"
    "/<string:email_id>",
    methods=["GET", "POST"],
)
def update_mccard(card_id, spend_amt, spend_date, payment_mode, event_name, email_id):
    if request.method == "POST":
        update_functions.update_mccard(
            card_id,
            request.form["spend_amt"],
            request.form["spend_date"],
            request.form["payment_mode"],
            request.form["event_name"],
            request.form["email_id"],
        )
        return redirect("/mccard")
    mccard_data = display_functions.display_mccard()
    event_data = display_functions.display_event()
    visitor_data = display_functions.display_visitor()
    return render_template(
        "update_mccard.html",
        mccard_data=mccard_data,
        event_data=event_data,
        visitor_data=visitor_data,
        card_id=card_id,
        spend_amt=spend_amt,
        spend_date=spend_date,
        payment_mode=payment_mode,
        event_name=event_name,
        email_id=email_id,
    )


# -------------------Booking----------------------
"""   	[Id] [uniqueidentifier] NOT NULL,
	[BookingDate] [datetime] NOT NULL,
	[TotalAmount] [float] NOT NULL,

	[Event_Id] [uniqueidentifier] NULL,
	[Exhibitor_Id] [uniqueidentifier] NULL
"""


@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        insert_functions.insert_booking(
            request.form["booking_date"],
            request.form["total_amount"],
            request.form["event_name"],
            request.form["email_id"],
        )
    booking_data = display_functions.display_booking()
    event_data = display_functions.display_event()
    exhibitor_data = display_functions.display_exhibitor_1()
    return render_template(
        "booking.html",
        booking_data=booking_data,
        event_data=event_data,
        exhibitor_data=exhibitor_data,
    )


@app.route("/delete_booking/<int:booking_id>")
def delete_booking(booking_id):
    delete_functions.delete_booking(booking_id)
    return redirect("/booking")


@app.route(
    "/update_booking/<int:booking_id>/<string:booking_date>/<string:total_amount>"
    "/<string:event_name>/<string:email_id>",
    methods=["GET", "POST"],
)
def update_booking(booking_id, booking_date, total_amount, event_name, email_id):
    if request.method == "POST":
        total_amount = float(request.form["total_amount"])
        update_functions.update_booking(
            booking_id,
            request.form["booking_date"],
            total_amount,
            request.form["event_name"],
            request.form["email_id"],
        )
        return redirect("/booking")
    booking_data = display_functions.display_booking()
    event_data = display_functions.display_event()
    exhibitor_data = display_functions.display_exhibitor_1()
    return render_template(
        "update_booking.html",
        booking_data=booking_data,
        event_data=event_data,
        exhibitor_data=exhibitor_data,
        booking_id=booking_id,
        booking_date=booking_date,
        total_amount=total_amount,
        event_name=event_name,
        email_id=email_id,
    )


# -------------------Visitor----------------------
"""
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| visitor_id    | int          | NO   | PRI | NULL    | auto_increment |
| first_name    | varchar(255) | YES  |     | NULL    |                |
| last_name     | varchar(255) | YES  |     | NULL    |                |
| addr          | varchar(255) | YES  |     | NULL    |                |
| pin_code      | varchar(255) | YES  |     | NULL    |                |
| mob_no        | varchar(255) | NO   |     | NULL    |                |
| email_id      | varchar(255) | NO   |     | NULL    |                |
| date_of_birth | datetime     | YES  |     | NULL    |                |
| gender        | varchar(1)   | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
"""


@app.route("/visitor", methods=["GET", "POST"])
def visitor():

    if request.method == "POST":
        insert_functions.insert_visitor(
            request.form["first_name"],
            request.form["last_name"],
            request.form["addr"],
            request.form["pin_code"],
            request.form["mob_no"],
            request.form["email_id"],
            request.form["date_of_birth"],
            request.form["gender"],
        )

    visitor_data = display_functions.display_visitor()
    return render_template("visitor.html", visitor_data=visitor_data)


@app.route("/delete_visitor/<int:visitor_id>")
def delete_visitor(visitor_id):
    delete_functions.delete_visitor(visitor_id)
    return redirect("/visitor")


@app.route(
    "/update_visitor/<int:visitor_id>/<string:first_name>/<string:last_name>/<string:addr>"
    "/<string:pin_code>/<string:mob_no>/<string:email_id>/<string:date_of_birth>/<string:gender>",
    methods=["GET", "POST"],
)
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
    if request.method == "POST":
        # visitor_id, first_name, last_name, addr, pin_code, mob_no, email_id, date_of_birth, gender
        update_functions.update_visitor(
            visitor_id,
            request.form["first_name"],
            request.form["last_name"],
            request.form["addr"],
            request.form["pin_code"],
            request.form["mob_no"],
            request.form["email_id"],
            request.form["date_of_birth"],
            request.form["gender"],
        )
        return redirect("/visitor")
    # visitor_data = display_functions.display_visitor()
    return render_template(
        "update_visitor.html",
        visitor_id=visitor_id,
        first_name=first_name,
        last_name=last_name,
        addr=addr,
        pin_code=pin_code,
        mob_no=mob_no,
        email_id=email_id,
        date_of_birth=date_of_birth,
        gender=gender,
    )


# -------------------event----------------------
"""
| Field              | Type         | Null | Key | Default | Extra          |
+--------------------+--------------+------+-----+---------+----------------+
| event_id           | int          | NO   | PRI | NULL    | auto_increment |
| event_name         | varchar(255) | YES  |     | NULL    |                |
| booking_start_date | datetime     | NO   |     | NULL    |                |
| event_start_date   | datetime     | NO   |     | NULL    |                |
| event_end_date     | datetime     | NO   |     | NULL    |                |
| venue_id           | int          | YES  | MUL | NULL    |
"""


@app.route("/event", methods=["GET", "POST"])
def event():

    if request.method == "POST":
        insert_functions.insert_event(
            request.form["event_name"],
            request.form["booking_start_date"],
            request.form["event_start_date"],
            request.form["event_end_date"],
            request.form["venue_city"],
        )
    event_data = display_functions.display_event()
    venue_data = display_functions.display_venue()
    return render_template("event.html", venue_data=venue_data, event_data=event_data)


@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    delete_functions.delete_event(event_id)
    return redirect("/event")


@app.route(
    "/update_event/<int:event_id>/<string:event_name>/<string:booking_start_date>/<string:event_start_date>"
    "/<string:event_end_date>/<string:venue_city>",
    methods=["GET", "POST"],
)
def update_event(
    event_id,
    event_name,
    booking_start_date,
    event_start_date,
    event_end_date,
    venue_city,
):
    if request.method == "POST":
        # {{event_id}} / {{event_name}} / {{booking_start_date}} / {{event_name}} / {{event_end_date}} / {{venue_city}}
        update_functions.update_event(
            event_id,
            request.form["event_name"],
            request.form["booking_start_date"],
            request.form["event_start_date"],
            request.form["event_end_date"],
            request.form["venue_city"],
        )
        return redirect("/event")
    venue_data = display_functions.display_venue()
    return render_template(
        "update_event.html",
        event_id=event_id,
        event_name=event_name,
        booking_start_date=booking_start_date,
        event_start_date=event_start_date,
        event_end_date=event_end_date,
        venue_city=venue_city,
        venue_data=venue_data,
    )


@app.route("/test", methods=["GET"])
def ret_book():
    # data = {"label": , }
    # view
    event_map = {}

    booking_data = insert_check.display_booking()
    event_data = insert_check.display_eventt()
    for event_id, event_name, _, _, _, _ in event_data:
        event_map[event_id] = event_name
    print(event_map)

    event_booking = {}

    for data in booking_data:
        event_name = event_map[data[-2]]
        if event_name in event_booking:
            event_booking[event_name] += 1
        else:
            event_booking[event_name] = 1

    print(event_booking)
    message = {
        "label": list(event_booking.keys()),
        "value": list(event_booking.values()),
    }
    return jsonify(message)


@app.route("/industry_data", methods=["GET"])
def industry_data():
    industry_map = {}
    industry_data = insert_check.display_industry()
    for industry_id, industry_name in industry_data:
        industry_map[industry_id] = industry_name

    industry_exhibitor = {}
    exhibitor_booking = insert_check.display_exhibitor()
    for data in exhibitor_booking:
        industry_name = industry_map[data[-3]]
        if industry_name in industry_exhibitor:
            industry_exhibitor[industry_name] += 1
        else:
            industry_exhibitor[industry_name] = 1
    final_data = {
        "label": list(industry_exhibitor.keys()),
        "value": list(industry_exhibitor.values()),
    }
    return jsonify(final_data)


@app.route("/sales_company", methods=["GET"])
def company_sales_data():
    megacons_booking = {}
    megaconsumers = insert_check.display_megaconsumercard()
    megaconsumerdata = pd.DataFrame(
        megaconsumers,
        columns=[
            "card_id",
            "spend_amt",
            "spend_date",
            "payment_mode",
            "event_id",
            "booking_id",
            "visitor_id",
        ],
    )
    for data in megaconsumers:
        megacons_booking[data[-2]] = data[1]
    booking_exhibitor = {}
    booking_data = insert_check.display_booking()
    print(megaconsumerdata)
    bookingdata = pd.DataFrame(
        booking_data,
        columns=[
            "booking_id",
            "booking_date",
            "total_amount",
            "event_id",
            "exhibitor_id",
        ],
    )
    print(bookingdata)
    exhibitor_data = insert_check.display_exhibitor()
    exhibitor_df = pd.DataFrame(
        exhibitor_data,
        columns=[
            "exhibitor_id",
            "exhibitor_name",
            "email_id",
            "phone_no",
            "company_name",
            "company_descr",
            "company_add",
            "company_pin_code",
            "industry_id",
            "country_id",
            "state_id",
        ],
    )

    megacons_booking = pd.merge(megaconsumerdata, bookingdata, on="booking_id")
    final_df = pd.merge(megacons_booking, exhibitor_df, on="exhibitor_id")
    print(final_df)
    company_sales = {}
    for data in range(len(final_df)):
        if final_df.iloc[data, -7] in company_sales:
            company_sales[final_df.iloc[data, -7]] += int(final_df.iloc[data, 1])
        else:
            company_sales[final_df.iloc[data, -7]] = int(final_df.iloc[data, 1])
        # print(data)
        # print(data[1])
    final_data = {
        "label": list(company_sales.keys()),
        "value": list(company_sales.values()),
    }
    # print(final_data)
    # print(list(company_sum[0]))
    return jsonify(final_data)


@app.route("/dashboard/booking")
def bookingdashboard():
    print("hey")
    return render_template("charts.html")


@app.route("/dashboard/industry")
def industrydashboard():
    print("hey")
    return render_template("industry_chart.html")


@app.route("/dashboard/company")
def companydashboard():
    print("hey")
    return render_template("company_sales.html")

