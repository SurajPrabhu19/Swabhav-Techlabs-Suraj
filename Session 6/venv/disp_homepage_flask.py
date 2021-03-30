from flask import Flask, render_template
app = Flask(__name__)

@app.route("/contact")

def disp_html():
    return render_template('home.html')