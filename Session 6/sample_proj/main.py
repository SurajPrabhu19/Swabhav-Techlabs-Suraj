import conn
from flask import  Flask,render_template

app=Flask(__name__)
@app.route("/")

def intro():
    return f'''
    <h1>
    Hello to Contact App
    <h1>
    '''

@app.route("/contacts")
def get_contact():
    ans=conn.return_data()
    return render_template('home.html',data=ans)