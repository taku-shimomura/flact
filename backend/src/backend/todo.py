from flask import Blueprint, Flask, jsonify
from flask_cors import CORS

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
def todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])
