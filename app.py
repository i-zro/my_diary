from flask import Flask, render_template, redirect, url_for, flash, session, request, g
import pymongo
from pymongo import MongoClient
from pymongo import CursorType
from flask_login import LoginManager
# from werkzeug import secure_filename
from werkzeug.security import generate_password_hash,check_password_hash
import bcrypt
from flask_login import login_user,current_user
import os
from db_maker import *

host = "localhost"
port = "27017"
client=MongoClient(host, int(port))
db=client['Users']

det=[1,3]

app=Flask(__name__)
        
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():    
    return render_template('login.html')
    


@app.route('/login',methods=['POST'])
def login_post():
    session.pop('user',None)
    email=request.form.get('email')
    password=request.form.get('pass')
    data=db.credentials
    flag=False    
    # session.pop('User',None)
    
    if email is None or password is None:
        flash("Please fill both the fields and Try Again")
        return redirect(url_for('login'))
    
    
    for i in data.find():
        if i['email']==email:
            name=i['username']            
            if check_password_hash(i['password'], password):    
                flag=True
                session['user']=name 
                print(session['user'])  
                det[0]=name
                det[1]=email                                  
                return redirect(url_for('profile'))
            
    if flag==False:
        flash("Invalid Credentials")
        return redirect(url_for('login'))
    
    return redirect(url_for('login'))

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def reg_post():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('pass')
    password=generate_password_hash(password, method='sha256')
    
    
    data=db.credentials
    for i in data.find():
        if i['email']==email:  
            flash("Your Email Address is already registered with us")
            return redirect(url_for('login')) 
    else:   
        user_info={'username': name,
                'email': email,
                'password': password} 
        data.insert_one(user_info)
        
    return redirect(url_for('login'))

@app.route('/logout')
def logoute():
    session.pop('user', None)  
    det=[]  
    return redirect(url_for('login'))

@app.route('/moabogi')
def moabogi():
    if g.user:
        return render_template('moabogi_select.html', username=det[0], email=det[1])

@app.route('/my_diary')
def my_diary():
    return render_template('my_diary.html', username=det[0], email=det[1])
    
@app.route('/profile')
def profile():   
    if g.user:
         return render_template('profile.html',username=det[0],email=det[1])        
    elif det==[]:
        flash("You are kindly requested to Login first")        
        return redirect(url_for('login')) 
   
    flash("You are kindly requested to Login first") 
    return redirect(url_for('login'))

@app.route('/fileUpload/<email>', methods = ['GET', 'POST'])
def upload_file(email):
   if request.method == 'POST':
      f = request.files['file']
      title = request.json['title']
      content = request.json['content']
      
      
      #저장할 경로 + 파일명
      if not ('../static/image_db/{0}'.format(email)):
          os.system(mkdir('../static/image_db/{0}'.format(email)))
      f.save('../static/image_db/{0}/{1}'.format(email, )+'.jpg')
      insert_item_one(mongo, "izero3127@gmail.com", "오늘 힘드네", "diary", "diarylist")
      return render_template('return.html')

@app.before_request
def before_request():
    g.user=None
    det=[]
    if 'user' in session:
        g.user=session['user']

if __name__=='__main__':
    app.secret_key = 'izero'
    app.run(debug=True)
    
