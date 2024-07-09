from flask import Flask, render_template
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

@app.route('/')
def contact_form():
    quote = random.choice(quotes)
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('contact_form.html', quote=quote, current_date_time=current_date_time)

if __name__ == '__main__':
    app.run(debug=True)
