from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from sqlalchemy.sql.schema import Index
from session import session
from models import tasksItems

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    tasks = session.query(tasksItems).all()
    return render_template("home.html", tasks = tasks)

@views.route ("/list")
def list():
    return render_template("list.html")

@views.route("/add", methods = ['POST'])

def add():
    if request.method == 'POST':
        if request.form['task'] != '':
            task= tasksItems(name=request.form['task'],compleate=False)
            session.add(task)
            session.commit()
            flash('New item has been added succesfuly')
            return redirect(url_for('views.home'))
            
        else:
            flash('You can`t add an empty task')
            return redirect(url_for('views.home'))

            

