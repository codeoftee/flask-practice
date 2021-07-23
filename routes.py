from flask import render_template, request, session, redirect, url_for

from app import app


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # dummy login
        # if user['email'] == email and user['password'] == password:
        #     session['user'] = user
        #
        #     resp = redirect(url_for('home_page'))
        #     resp.set_cookie('email', user['email'], max_age=timedelta(hours=24))
        #     resp.set_cookie('password', user['password'], max_age=timedelta(hours=24))
        #     return resp
        # else:
        #     flash('Invalid email or password')
        #     return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def log_out():
    session.pop('user', None)
    resp = redirect(url_for('login'))
    resp.set_cookie('email', expires=0)
    resp.set_cookie('password', expires=0)
    return resp
