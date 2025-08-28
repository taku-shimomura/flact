from flask import Flask
from . import extensions
from . import todo

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = extensions.db
db.init_app(app)

app.register_blueprint(todo.bp)


def setup_db():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    setup_db()
    app.run(host="0.0.0.0", port=3000, debug=True)
