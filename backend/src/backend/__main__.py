from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return { 'id': self.id, 'task': self.task, 'done': self.done }

def setup_db():
    with app.app_context():
        db.create_all()

@app.route('/todos', methods=['GET'])
def todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

if __name__ == '__main__':
    setup_db()
    app.run(host='0.0.0.0', port=3000, debug=True)
