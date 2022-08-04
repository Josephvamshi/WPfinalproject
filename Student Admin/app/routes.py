from flask import render_template, flash, redirect, url_for
from app import app
from flask import request
from app.models import Credentials, Studentdetails
from app import db

@app.route('/',methods=['GET'])
@app.route('/index',methods=['GET'])

def login():
    return render_template('index.html')

@app.route('/',methods=['POST'])
@app.route('/index',methods=['POST'])
def post_login():
        if request.form['action']=='signup':
            return render_template('register.html')
        else:
            username1=request.form.get("username","<missing username>")
            password1=request.form.get("password","<missing password>")
            print(username1)
            u1=0
            u=Credentials.query.filter(Credentials.username==username1)
            
            for u in u:
                print(u.username)
            try:
                if u.username==username1 :
                    if u.password==password1:
                        return redirect('/login_1')
                    else:
                        return '<html><h1>login failed</h1></html>'
                else:
                        return '<html><h1>login failed</h1></html>'
            except :
                return '<html<p>user not exists</p></html>'
            
            

                
@app.route("/register",methods=['GET'])
def register():
    return render_template('register.html')

@app.route("/register",methods=['POST'])
def post_register():
    username1=request.form.get("username","<missing username")
    password1=request.form.get("password","<missing password>")
    confirm_password1=request.form.get("confirm_password","<missing confirm_password>")
    print(password1)
    print(confirm_password1)
    if password1 == confirm_password1:
        u=Credentials(username=username1,password=password1)
        db.session.add(u)
        try:
            db.session.commit()
            submitted=1
        except :
            db.session.rollback()
            submitted=0
        return render_template('reg_status.html',submitted=submitted)
    else:
        return '<html><h1>password and confirm password does not match</h1> <br><br><a href="/index"> HOME</a> </html>'
@app.route('/login_1')
def login_1():    
    return render_template('login.html')


@app.route('/login/student',methods=['GET'])
def add_details():
    return render_template('add_student.html')

@app.route('/login/student',methods=['POST'])
def post_details():
    student1=request.form.get("student","<missing student>")
    course1=request.form.get("Course","<missing course>")
    fee1=request.form.get("fee","<missing fee>")
    grades1=request.form.get("grades","<missing grades>")
    city1=request.form.get("city","<missing city>")
    contact1=request.form.get("contact","<missing contact>")
    u=Studentdetails(student=student1,course=course1,fee=fee1,grades=grades1,city=city1,contact=contact1)
    db.session.add(u)
    try:
        db.session.commit()
        submitted=1
    except :
        db.session.rollback()
        submitted=0
    return render_template('login_1.html',submitted=submitted)

@app.route('/login/view',methods=['GET'])
def view_details():
    return render_template('view.html',submitted=0)

@app.route('/login/view',methods=['POST'])
def post_view_details():
    student1=request.form.get("name","<missing name>")
    print(student1)
    details=Studentdetails.query.filter(Studentdetails.student==student1)
    return render_template('view.html',submitted=1,detail=details)














