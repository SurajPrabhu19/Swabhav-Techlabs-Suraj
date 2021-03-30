from flask import Flask , render_template
import connection

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

'''  <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <form>
            <input type="radio" name="gender" value="male" id="male">
            <label for="male">Male</label><br>
            <input type="radio" name="gender" value="female" id="female">
            <label for="female">Female</label><br>
            <input type="radio" name="gender" value="other" id="other">
            <label for="other">Other</label>
        </form>
    </body>
    </html>'''

@app.route("/contacts")
def return_contact():
    contact_data = connection.get_contact_data()
    return render_template('contact.html',data = contact_data)

@app.route("/addcontact")
def open_addContact():
    return render_template('addcontact.html')