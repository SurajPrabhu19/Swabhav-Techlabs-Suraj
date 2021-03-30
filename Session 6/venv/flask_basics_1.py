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

"""
    return '''
    <h1>
    Welcome to my WebApp
    ''' + str(datetime.now())"""