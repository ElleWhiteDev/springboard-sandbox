from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Todo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'mr_pickles'

connect_db(app)
app.app_context().push()

@app.route("/")
def index_page():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/api/todos")
def list_todos():
    all_todos = [todo.serialize() for todo in Todo.query.all()]
    return jsonify(todos = all_todos)

@app.route("/api/todos/<int:id>")
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo=todo.serialize())

@app.route("/api/todos", methods=["POST"])
def create_todo():
    new_todo = Todo(title=request.json["title"])
    db.session.add(new_todo)
    db.session.commit()
    # response_json = jsonify(todo=new_todo.serialize()) can be done seperately
    return (jsonify(todo=new_todo.serialize()), 201)  #standards dictate 201 response code when making new thing

@app.route("/api/todos/<int:id>", methods=["PATCH"])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    # db.session.query(Todo).filter_by(id=id).update(request.json)
    todo.title = request.json.get("title", todo.title)  #look for title; if none default to existing 
    todo.done = request.json.get("done", todo.done)
    db.session.commit()
    return jsonify(todo=todo.serialize())

@app.route("/api/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify(message="Deleted")