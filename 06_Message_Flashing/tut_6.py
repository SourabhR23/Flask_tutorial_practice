from flask import Flask, request, session, redirect, url_for, render_template, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "abc1234"
# how long you want to store the data in session?
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        # store the session data
        session['user'] = user
        flash("Login Successful!")
        return redirect(url_for('user'))
    else:
        # if you are already logged in
        if 'user' in session:
            flash("Already Logged In!")
            return redirect(url_for('user'))

        return render_template('login.html')


@app.route("/user")
def user():
    if 'user' in session:
        # retrieve the session data
        user = session['user']
        return render_template('user.html', user=user)
    else:
        flash("You are not Logged In!")
        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    if 'user' in session:
        user = session['user']
        # this will flash the 'message' on 'login' page
        flash(f"You have been logged out, {user}", "info")
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)