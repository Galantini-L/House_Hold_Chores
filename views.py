from functools import update_wrapper
from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from session import session
from models import tasksItems
from sqlalchemy import update


views = Blueprint(__name__,"views")

@views.route("/")
def home():
    tasks = session.query(tasksItems).all()
    return render_template("home.html", tasks = tasks)

@views.route("/add", methods = ['POST'])
def add():
    if request.method == 'POST':
        if request.form['task'] != '':
            task= tasksItems(name=request.form['task'])
            session.add(task)
            session.commit()
            flash('New item has been added succesfuly', "success")
            return redirect(url_for('views.home'))
            
        else:
            flash('You can`t add an empty task', "warning")
            return redirect(url_for('views.home'))

@views.get("/update/<int:tasks_id>")
def update(tasks_id):
    query1 = session.query(tasksItems).filter(tasksItems.id == tasks_id)
    for q in query1:
        q.compleate = not q.compleate
    session.commit()


    return redirect(url_for('views.home'))
            
@views.get("/delete/<int:tasks_id>")
def delete(tasks_id):
    session.query(tasksItems).filter(
        tasksItems.id == tasks_id).delete()
    session.commit()
        
    return redirect(url_for('views.home'))


    #task_list = request.form.getlist('task')