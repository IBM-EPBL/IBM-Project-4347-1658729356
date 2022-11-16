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

def dashboard():
    return render_template("dashboard.html") #rendering our home.html contained within /templates






def createjobseeker_profile():
  if request.method == 'POST':
    name = request.form['name'] 
    email = request.form['email']
    mobileno=request.form['mobileno']
    nationality=request.form['nationality']
    qualification=request.form['qualification']
    passout=request.form['passout']
    experience=request.form['experience"];
    degree=request.form['degree'];
    per_sslc=request.form['per_sslc'];
    per_hsc=request.form['per_hsc'];
    per_degree=request.form['per_degree'];
  
    tum = request.files['resume']
    tum.save(os.path.join(app.config['UPLOAD_DIR'],tum.filename))


    
    hash=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

    query = "SELECT EMAIL FROM JOBSEEKER WHERE EMAIL=?"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    isUser = ibm_db.fetch_assoc(stmt)
    
    if not isUser:
      insert_sql = "INSERT INTO JOBSEEKER (name, email, mobileno, nationality, qualification, passout, experience, degree,per_sslc,per_hsc,per_degree) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, mobileno)
      ibm_db.bind_param(prep_stmt, 4, nationality)
      ibm_db.bind_param(prep_stmt, 5, qualification)
      ibm_db.bind_param(prep_stmt, 6, passout)
      ibm_db.bind_param(prep_stmt, 7, experience)
      ibm_db.bind_param(prep_stmt, 8, degree)
      ibm_db.bind_param(prep_stmt, 9, per_sslc)
      ibm_db.bind_param(prep_stmt, 10, per_hsc)
      ibm_db.bind_param(prep_stmt, 11, per_degree)
      ibm_db.execute(prep_stmt)
      return render_template('dashboard.html')
    

  return render_template('dashboard.html',name='Home')





@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

