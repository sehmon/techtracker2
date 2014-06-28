from flask import render_template, request, flash, redirect, url_for, session
from forms import JobForm
from app import app, db
from models import Job

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
            job = Job(name=form.name.data, desc=form.desc.data)
            db.session.add(job)
            db.session.commit()
            return render_template('submit.html', success = True, name = " " + job.name)

    elif request.method == 'GET':
        return render_template('submit.html', form = form)

@app.route('/view')
def view():
    jobs = Job.query.all()
    return render_template('view.html',jobs = jobs) 
