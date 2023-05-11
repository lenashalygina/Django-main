from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@app.route('/')
def todo_list():
    todos = Todo.query.all()
    return render_template('todo_list.html', todos=todos)


@app.route('/create', methods=['GET', 'POST'])
def todo_create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('todo_form.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def todo_update(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        db.session.commit()
        return redirect('/')
    return render_template('todo_form.html', todo=todo)


@app.route('/delete/<int:id>', methods=['POST'])
def todo_delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
