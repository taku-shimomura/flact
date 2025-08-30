from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS, cross_origin

from . import extensions

bp = Blueprint("todo", __name__, url_prefix="/todo")

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = extensions.db
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {"id": self.id, "task": self.task, "done": self.done}


@bp.route("/", methods=["GET"])
@cross_origin()
def get_todos():
    todos = db.session.execute(db.select(Todo)).scalars()
    return jsonify([todo.to_dict() for todo in todos])


@bp.route("/<int:id>", methods=["GET"])
@cross_origin()
def get_todo(id):
    todo = db.get_or_404(Todo, id)
    return jsonify(todo.to_dict())


@bp.route("/", methods=["POST"])
@cross_origin()
def create_todo():
    data = request.get_json()
    todo = Todo(task=data["task"], done=data.get("done", False))  # type: ignore
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201


@bp.route("/<int:id>", methods=["PUT"])
@cross_origin()
def update_todo(id):
    todo = db.get_or_404(Todo, id)
    data = request.get_json()
    todo.task = data.get("task", todo.task)
    todo.done = data.get("done", todo.done)
    db.session.commit()
    return jsonify(todo.to_dict())


@bp.route("/<int:id>", methods=["DELETE"])
@cross_origin()
def delete_todo(id):
    todo = db.get_or_404(Todo, id)
    db.session.delete(todo)
    db.session.commit()
    return "", 204
