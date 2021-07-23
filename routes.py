import hashlib
from datetime import timedelta

from flask import render_template, request, session, redirect, url_for, flash

from app import app, db
from models import User


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # query user with email
        user = User.query.filter_by(email=email).first()
        if user is None:
            # user not found
            flash('Invalid email or password')
            return render_template('login.html')
        else:
            password_hash = hashlib.sha256(password.encode())
            hashed = password_hash.hexdigest()
            if hashed == user.password:
                # login is correct
                session['username'] = user.username
                session['phone'] = user.phone
                session['email'] = user.email
                resp = redirect(url_for('home_page'))
                resp.set_cookie('id', str(user.id), max_age=timedelta(hours=24))
                resp.set_cookie('password', hashed, max_age=timedelta(hours=24))
                return resp
            else:
                flash('Invalid email or password')
                return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def log_out():
    session.pop('user', None)
    resp = redirect(url_for('login'))
    resp.set_cookie('email', expires=0)
    resp.set_cookie('password', expires=0)
    return resp


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('create-account.html')
    else:
        username = request.form['username']
        email = request.form['email']
        gender = request.form['gender']
        phone = request.form['phone']
        password = request.form['password']
        if username == '':
            flash('Username is required')
        # register user
        password_hash = hashlib.sha256(password.encode())
        hashed = password_hash.hexdigest()
        user = User(username=username, email=email, gender=gender, phone=phone,
                    password=hashed)
        db.session.add(user)
        db.session.commit()
        session['username'] = user.username
        session['phone'] = user.phone
        session['email'] = user.email
        resp = redirect(url_for('home_page'))
        resp.set_cookie('id', str(user.id), max_age=timedelta(hours=24))
        resp.set_cookie('password', hashed, max_age=timedelta(hours=24))
        flash('Registration successful!')
        return resp
