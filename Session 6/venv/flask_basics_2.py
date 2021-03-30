from flask import Flask,jsonify,abort

from model import db
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def hello():

    return f'''
    <h1>
    Hello from flask app{str(datetime.now())}
    <h1>
    '''

@app.route("/api/v1/employees")

def get_employee():
    return jsonify(db)

@app.route("/api/v1/employees/<int:emp_index>")

def det_emp(emp_index):
    try :
        return jsonify(db[emp_index])
    except :
        abort(404)