from flask import render_template, request, flash, redirect, url_for
from forms import JobForm
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = JobForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Please fill out the missing forms')
            return render_template('submit.html', form = form)
        else:
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('submit.html', form = form)



