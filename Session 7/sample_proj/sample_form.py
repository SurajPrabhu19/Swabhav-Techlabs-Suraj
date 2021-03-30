from flask import Flask, redirect, url_for, request,render_template
import connection
import time
app = Flask(__name__)
#------------------------------------login_page-------------------------------------------------------------------------
@app.route("/")
def login_page():
   return render_template('login.html')

#-----------------------------------home_page---------------------------------------------------------------------------
@app.route("/home")
def home_page():
    return render_template('home.html')

#-----------------------------------display_contacts--------------------------------------------------------------------
@app.route("/contacts")
def return_contact():
    contact_data = connection.get_contact_data()
    return render_template('contact.html',data = contact_data)

#-----------------------------------open_add_contacts_page------------------------------------------------------------------------
@app.route("/addcontact")
def addcontact():
    return render_template('addcontact.html')

@app.route("/add_address")
def add_address():
    return render_template('add_address.html')
# ------------------------------------------------------------------------------------------------------------------------

@app.route("/disp_message/<message>")
def disp_message(message):
   contact_data = connection.get_contact_data()
   return render_template('disp_message.html',data = contact_data,message = message)

@app.route("/disp_addr_message/<message>")
def disp_addr_message(message):
   address_data = connection.get_address_data()
   return render_template('disp_addr_message.html',data = address_data,message = message)

# @app.route("/disp_addr_message/<message>")
# def disp_message(message):
#    contact_data = connection.get_contact_data()
#    return render_template('disp_message.html',data = contact_data,message = message)


@app.route("/register/<fname>/<lname>/<number>")
def register(fname,lname,number):
   message = connection.register_contact(fname, lname, number)
   return redirect(url_for('disp_message',message = message))
   # return fname+"_"+lname+"_"+number

@app.route("/register_addr/<id>/<number>/<addr>/<city>/<state>/<p_code>")
def register_addr(id,number,city,addr,state,p_code):
   message = connection.register_address(number,addr,city,state,p_code,id)
   return redirect(url_for('disp_addr_message',message = message))

@app.route("/pass_addcontact_data",methods = ['POST', 'GET'])
def pass_addcontact_data():
   if request.method == 'POST':
      fname = request.form['fname']
      lname = request.form['lname']
      number = request.form['number']
      return redirect(url_for('register',fname=fname,lname=lname,number=number))
   else:
      fname = request.args.get('fname')
      lname = request.args.get('lname')
      number = request.args.get('number')
      return redirect(url_for('register', fname=fname, lname=lname, number=number))

@app.route("/pass_add_address_data",methods = ['POST', 'GET'])
def pass_add_address_data():
   if request.method == 'POST':
      id = request.form['id']
      number = request.form['number']
      addr = request.form['addr']
      city = request.form['city']
      state = request.form['state']
      p_code = request.form['p_code']
      return redirect(url_for('register_addr',id=id,addr=addr,city=city,state=state,p_code=p_code,number=number))
   else:
      id = request.args.get['id']
      number = request.args.get['number']
      addr = request.args.get['addr']
      city = request.args.get['city']
      state = request.args.get['state']
      p_code = request.args.get['p_code']
      return redirect(url_for('register_addr', id=id,addr=addr,city=city,state=state,p_code=p_code,number=number))

#-----------------------------------proceed_to_homepage-----------------------------------------------------------------
@app.route("/proceed/<successful>")
def proceed(successful):
   if successful == "True" :
      return redirect(url_for('home_page'))
   else :
      return redirect(url_for('login_page'))
      # return f'<head>Welcome Page else</head>'

#----------------------------------veryfing_password--------------------------------------------------------------------
@app.route('/success/<name><password>')
# def success(name, password):
#    password_data = connection.get_passwords()
#    for data in password_data:
#       pwd = (data[2])
#       if str(password) == str(pwd):
#          # return redirect(url_for('final',successful = True))
#          return "Password Correct for %s"%data
#    return "Password Incorrect for %s"%data
#    # return redirect(url_for('final',successful = False))
def success(name, password):
   password = (name + str(password))[-5:]
   password_data = connection.get_passwords()
   for data in password_data:
      pwd = str(data[2])
      if str(password) == str(pwd):
         return redirect(url_for('proceed',successful = "True"))
         # return "Password Correct %s %s"%(password,pwd)
   # return "Password InCorrect %s %s"%(password,pwd)
   return redirect(url_for('proceed',successful = "False"))

#-----------------------------------get/post data-----------------------------------------------------------------------
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      password = request.form['pwd']
      return redirect(url_for('success',name = user,password = password))
   else:
      user = request.args.get('nm')
      password= request.args.get('pwd')
      return redirect(url_for('success',name = user, password = password))

#-----------------------------------display_passwords-------------------------------------------------------------------
# @app.route('/pass')
# def display_passwords():
#    passwords = connection.get_passwords()
#    return render_template('password.html',data = passwords)
#-----------------------------------display_contact_address_table-------------------------------------------------------
# @app.route('/contact_address')
# def display_contact_address():
#    contact_address_data = connection.get_contact_address_data()
#    return render_template('contact_address.html',data = contact_address_data)


@app.route('/address_details/<num>')
def display_address_details(num):
   detail_dict = connection.address_detail_dict()
   return detail_dict[num]

@app.route('/address')
def address_table():
   address_data = connection.get_contact_address_data()
   return render_template('address.html',data = address_data)


if __name__ == '__main__':
   app.run(debug = True)
