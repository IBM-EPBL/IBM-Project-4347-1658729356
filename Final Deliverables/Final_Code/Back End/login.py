from flask import *#importing flask (Install it using python -m pip install flask)
import os
import ibm_db
import bcrypt
#import send_from_directory
app = Flask(__name__) #initialising flask
app.secret_key = ''
PEOPLE_FOLDER = os.path.join('static', 'people_photo')

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=phb43134;PWD=mTTnIE45Raj9A0rr",'','')


@app.route("/") #defining the routes for the home() funtion (Multiple routes can be used as seen here)
@app.route("/home")

def home():
    return render_template("home.html") #rendering our home.html contained within /templates

@app.route("/login")
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            return render_template('login.html',error='Please fill all fields')
        
        query = "SELECT * FROM USER WHERE email=?"
        stmt = ibm_db.prepare(conn, query)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        isUser = ibm_db.fetch_assoc(stmt)
        print(isUser,password)

        if not isUser:
            return render_template('login.html',error='Invalid Credentials')
      
        isPasswordMatch = bcrypt.checkpw(password.encode('utf-8'),isUser['PASSWORD'].encode('utf-8'))

        if not isPasswordMatch:
            return render_template('login.html',error='Invalid Credentials')

        session['email'] = isUser['EMAIL']
        return redirect(url_for('user_dashboard'))

    return render_template('login.html',name='Home')




app.config["UPLOAD_DIR"] = "uploads"
@app.route("/register",methods=['GET','POST'])
def register():
  if request.method == 'POST':
    email = request.form['email'] 
    password = request.form['password']
    firstname=request.form['firstname']
    middlename=request.form['middlename']
    lastname=request.form['lastname']
    dob=request.form['dob']
    age=request.form['age']
    drno=request.form['drno']
    landmark1=request.form['lnmk1']
    landmark2=request.form['lnmk2']
    village =request.form['village']
    district=request.form['district']
    pincode=request.form['pincode']
    country=request.form['country']
    country_code=request.form['countryCode']
    phone=request.form['phone']
    schlname10=request.form['schlname10']
    maxmark10=request.form['maxmark10']
    actmark10=request.form['actmark10']
    schlname212=request.form['schlname212']
    maxmark212=request.form['maxmark212']
    actmark212=request.form['actmark212']
    clgname=request.form['clgname']
    clgmaxmark=request.form['clgmaxmark']
    clgactmark=request.form['clgactmark']
    stream=request.form['stream']
    graduation=request.form['graduation']
    grayear=request.form['grayear']
    branch=request.form['branch']
    skills=request.form['form[]']
    q1=request.form['Q1']
    q2=request.form['Q2']
    q3=request.form['Q3']
    q4=request.form['Q4']
    q5=request.form['Q5']
    position=request.form['position']
    experience=request.form['expyears']
    designation=request.form['designation']
    tum = request.files['resume']
    tum.save(os.path.join(app.config['UPLOAD_DIR'],tum.filename))


    
    hash=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

    query = "SELECT EMAIL FROM JOBSEEKER WHERE EMAIL=?"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    isUser = ibm_db.fetch_assoc(stmt)
    
    if not isUser:
      insert_sql = "INSERT INTO JOBSEEKER (EMAIL, PASSWORD, FIRSTNAME, MIDDLENAME, LASTNAME, DOB, AGE, DOOR_NO, LANDMARK1, LANDMARK2,VILLAGE, DISTRICT, PINCODE, COUNTRY, COUNTRY_CODE, PHONE, SCHOOL_NAME, SC_MAX_MARK, SC_ACT_MARK,HSC_SCHOOL_NAME,HSC_MAX_MARK, HSC_ACT_MARK,COLLEGE_NAME,COLLEGE_MAX,COLLEGE_ACT, STREAM, GRADUATION, GRADUATION_YEAR, BRANCH, SKILLS, PRESENTATION, HACKATHON, CODING, WON, PRIZE_WON, POSITION, EXPYEARS,DESIGNATION, RESUME) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, email)
      ibm_db.bind_param(prep_stmt, 2, password)
      ibm_db.bind_param(prep_stmt, 3, firstname)
      ibm_db.bind_param(prep_stmt, 4, middlename)
      ibm_db.bind_param(prep_stmt, 5, lastname)
      ibm_db.bind_param(prep_stmt, 6, dob)
      ibm_db.bind_param(prep_stmt, 7, age)
      ibm_db.bind_param(prep_stmt, 8, drno)
      ibm_db.bind_param(prep_stmt, 9, landmark1)
      ibm_db.bind_param(prep_stmt, 10, landmark2)
      ibm_db.bind_param(prep_stmt, 11, village)
      ibm_db.bind_param(prep_stmt, 12, district)
      ibm_db.bind_param(prep_stmt, 13, pincode)
      ibm_db.bind_param(prep_stmt, 14, country)
      ibm_db.bind_param(prep_stmt, 15, country_code)
      ibm_db.bind_param(prep_stmt, 16, phone)
      ibm_db.bind_param(prep_stmt, 17, schlname10)
      ibm_db.bind_param(prep_stmt, 18, maxmark10)
      ibm_db.bind_param(prep_stmt, 19, actmark10)
      ibm_db.bind_param(prep_stmt, 20, schlname212)
      ibm_db.bind_param(prep_stmt, 21, maxmark212)
      ibm_db.bind_param(prep_stmt, 22, actmark212)
      ibm_db.bind_param(prep_stmt, 23, clgname)
      ibm_db.bind_param(prep_stmt, 24, clgmaxmark)
      ibm_db.bind_param(prep_stmt, 25, clgactmark)
      ibm_db.bind_param(prep_stmt, 26, stream)
      ibm_db.bind_param(prep_stmt, 27, graduation)
      ibm_db.bind_param(prep_stmt, 28, grayear)
      ibm_db.bind_param(prep_stmt, 29, branch)
      ibm_db.bind_param(prep_stmt, 30, skills)
      ibm_db.bind_param(prep_stmt, 31, q1)
      ibm_db.bind_param(prep_stmt, 32, q2)
      ibm_db.bind_param(prep_stmt, 33, q3)
      ibm_db.bind_param(prep_stmt, 34, q4)
      ibm_db.bind_param(prep_stmt, 35, q5)
      ibm_db.bind_param(prep_stmt, 36, position)
      ibm_db.bind_param(prep_stmt, 37, experience)
      ibm_db.bind_param(prep_stmt, 38, designation)
      ibm_db.bind_param(prep_stmt, 39, tum)
      ibm_db.execute(prep_stmt)
      return render_template('register.html')
    else:
      return render_template('register.html',error='Invalid Credentials')

  return render_template('register.html',name='Home')


@app.route("/orgregister")
def orgregister():
    return render_template("orgregister.html") #rendering our register.html contained within /templates


@app.route("/user_dashboard")
def user_dashboard():

    return render_template("user_dashboard.html")

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == "__main__": #checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    app.run(debug=True,port=8080) #running flask (Initalised on line 4)