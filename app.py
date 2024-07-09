from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import random
import datetime

app = Flask(__name__)

quotes = [
    "Life is what happens when you're busy making other plans.",
    "Get busy living or get busy dying.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
    "Your time is limited, don't waste it living someone else's life."
]

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS submissions
                      (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT, contact TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    quote = random.choice(quotes)
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('form.html', quote=quote, current_date_time=current_date_time)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    contact = request.form['contact']

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submissions (first_name, last_name, email, contact) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, email, contact))
    conn.commit()
    conn.close()

    return redirect(url_for('show_submissions'))

@app.route('/submissions')
def show_submissions():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM submissions")
    data = cursor.fetchall()
    conn.close()
    return render_template('submission.html', submissions=data)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, port=8001)
