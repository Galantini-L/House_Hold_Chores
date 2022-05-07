from flask import Flask
from session import session
from flask import render_template, request, redirect, url_for
from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask.helpers import flash
import secrets
from sqlalchemy.orm.session import sessionmaker
from db import engine


app = Flask(__name__)

#SECRET_KEY
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

#app.register_blueprint(app, url_prefix="/")


class tasksItems(declarative_base()):
    __tablename__ = 'tasks'
    id = Column(Integer,primary_key=True)
    name = Column(String(60), nullable=False)
    compleate = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())



@app.route("/")
def home():
    try:
        Session = sessionmaker(engine)
        session = Session()
        tasks = session.query(tasksItems).all()
        return render_template("home.html", tasks = tasks)

    except:
        print('-------------Error whit the Server-------------')
        flash('Error Conectiong whit the server', "danger")
        return render_template("home.html")

@app.route("/add", methods = ['POST'])
def add():
    if request.method == 'POST':
        if request.form['task'] != '':
            task= tasksItems(name=request.form['task'])
            session.add(task)
            session.commit()
            flash('New item has been added succesfuly', "success")
            return redirect(url_for('home'))
            
        else:
            flash('You can`t add an empty task', "warning")
            return redirect(url_for('home'))

@app.get("/update/<int:tasks_id>")
def update(tasks_id):
    query1 = session.query(tasksItems).filter(tasksItems.id == tasks_id)
    for q in query1:
        q.compleate = not q.compleate
    session.commit()


    return redirect(url_for('home'))
            
@app.get("/delete/<int:tasks_id>")
def delete(tasks_id):
    session.query(tasksItems).filter(
        tasksItems.id == tasks_id).delete()
    session.commit()
        
    return redirect(url_for('home'))


    #task_list = request.form.getlist('task')



if __name__ == '__main__':
    app.run(debug=True, port=8020)