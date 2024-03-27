from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for

from .models import db, Todobase

@app.route('/')
@app.route('/tasks')
def tasks():
    todobase = Todobase.query.order_by(Todobase.date.desc()).all()
    return render_template("tasks.html", todobase=todobase)

@app.route('/create-task', methods=['POST', 'GET'])
def create_task():
    if request.method == "POST":
        task = request.form['task']
        task_stat = request.form['task_stat']
        task_cat = request.form['task_cat']
        task_project = request.form['task_project']
        descript = request.form.get('ckeditor')

        todobase = Todobase(task=task, task_stat=task_stat, task_cat=task_cat, task_project=task_project, descript=descript)

        try:
            db.session.add(todobase)
            db.session.commit()
            return redirect('/tasks')
        except:
            return "При добавлении задания произошла ошибка"
    else:
        return render_template("create-task.html")

@app.route('/task/<int:id>')
def task_detail(id):
    todobase = Todobase.query.get(id)
    return render_template("task-detail.html", todobase=todobase)

@app.route('/task/<int:id>/delete')
def task_delete(id):
    todobase = Todobase.query.get_or_404(id)

    try:
        db.session.delete(todobase)
        db.session.commit()
        return redirect('/tasks')
    except:
        return "При удалении задачи произошла ошибка"

@app.route('/task/<int:id>/update', methods=['POST', 'GET'])
def task_update(id):
    todobase = Todobase.query.get(id)
    if request.method == "POST":
        todobase.task = request.form['task']
        todobase.task_stat = request.form['task_stat']
        todobase.task_cat = request.form['task_cat']
        todobase.task_project = request.form['task_project']
        todobase.descript = request.form.get('ckeditor')

        try:
            db.session.commit()
            return redirect('/tasks')
        except:
            return "При редактировании задачи произошла ошибка"
    else:
        return render_template("task-update.html", todobase=todobase)