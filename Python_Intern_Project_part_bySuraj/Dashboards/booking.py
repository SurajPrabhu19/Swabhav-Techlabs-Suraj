import matplotlib.pyplot as plt


def booking_dash(X, Y):
    plt.plot(X, Y)
    plt.xlabel("Booking Date")
    plt.ylabel("No. of Booking")
    plt.savefig("static/images/img_booking_dash.png")
    return "static/images/img_booking_dash.png"

