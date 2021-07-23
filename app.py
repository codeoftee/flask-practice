from datetime import timedelta

from flask import Flask, render_template, request, flash, session, redirect, url_for

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


user = {
    "username": "Okocha",
    "password": "test",
    "shirt": 10,
    "email": 'test@test.com',
    "id": 1
}


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # dummy login
        if user['email'] == email and user['password'] == password:
            session['user'] = user

            resp = redirect(url_for('home_page'))
            resp.set_cookie('email', user['email'], max_age=timedelta(hours=24))
            resp.set_cookie('password', user['password'], max_age=timedelta(hours=24))
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


if __name__ == '__main__':
    app.run()
