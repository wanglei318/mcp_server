from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Task
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete_task/<int:id>')
def complete_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))