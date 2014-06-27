from flask import render_template
from forms import ContactForm
from app import app

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/submit')
def submit():
    return render_template('submit.html')
