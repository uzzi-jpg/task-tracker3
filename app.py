from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'tasks_data.json'

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'todo': [], 'progress': [], 'done': []}

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    column = data.get('column')
    title = data.get('title')
    description = data.get('description')
    
    tasks = load_tasks()
    
    new_task = {
        'id': datetime.now().timestamp(),
        'title': title,
        'description': description
    }
    
    tasks[column].append(new_task)
    save_tasks(tasks)
    
    return jsonify(tasks)

@app.route('/api/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    column = data.get('column')
    task_id = float(data.get('task_id'))
    
    tasks = load_tasks()
    tasks[column] = [t for t in tasks[column] if t['id'] != task_id]
    save_tasks(tasks)
    
    return jsonify(tasks)

@app.route('/api/move_task', methods=['POST'])
def move_task():
    data = request.get_json()
    from_column = data.get('from_column')
    to_column = data.get('to_column')
    task_id = float(data.get('task_id'))
    
    tasks = load_tasks()
    
    task = None
    for t in tasks[from_column]:
        if t['id'] == task_id:
            task = t
            break
    
    if task:
        tasks[from_column] = [t for t in tasks[from_column] if t['id'] != task_id]
        tasks[to_column].append(task)
        save_tasks(tasks)
    
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
