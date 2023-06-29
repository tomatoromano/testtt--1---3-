import sqlite3
from flask import Flask, render_template, request, session, redirect, flash, url_for

app = Flask(__name__, static_url_path='/static', static_folder="static")


def get_db_connection():
    conn = sqlite3.connect('databse.db')
    conn.row_factory = sqlite3.Row
    return conn

# get all users


@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# add a new user


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        if not firstname:
            flash('firstname is required!')
        elif not lastname:
            flash('lastname is required!')
        elif not lastname:
            flash('email is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO users (firstname, lastname, email) VALUES (?, ?, ?)',
                         (firstname, lastname, email))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('yup2.html')


@app.route('/home')
def home():
    return render_template('yup.html')


@app.route('/about')
def about():
    return render_template('yup3.html')


if __name__ == '__main__':
    app.run(debug=True)
