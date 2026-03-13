from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id REAL PRIMARY KEY,
                  title TEXT NOT NULL,
                  description TEXT,
                  column_name TEXT NOT NULL,
                  priority TEXT DEFAULT 'medium')''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE column_name = 'todo' ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END")
    todo = [dict(row) for row in cursor.fetchall()]
    
    cursor.execute("SELECT * FROM tasks WHERE column_name = 'progress' ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END")
    progress = [dict(row) for row in cursor.fetchall()]
    
    cursor.execute("SELECT * FROM tasks WHERE column_name = 'done' ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END")
    done = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({'todo': todo, 'progress': progress, 'done': done})

@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    column = data.get('column')
    title = data.get('title')
    description = data.get('description', '')
    priority = data.get('priority', 'medium')
    
    task_id = datetime.now().timestamp()
    
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (id, title, description, column_name, priority) VALUES (?, ?, ?, ?, ?)',
                 (task_id, title, description, column, priority))
    conn.commit()
    conn.close()
    
    return get_tasks()

@app.route('/api/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_id = float(data.get('task_id'))
    
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    return get_tasks()

@app.route('/api/move_task', methods=['POST'])
def move_task():
    data = request.get_json()
    task_id = float(data.get('task_id'))
    to_column = data.get('to_column')
    
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET column_name = ? WHERE id = ?', (to_column, task_id))
    conn.commit()
    conn.close()
    
    return get_tasks()

@app.route('/api/search', methods=['POST'])
def search_tasks():
    data = request.get_json()
    query = data.get('query', '').lower()
    
    if not query:
        return get_tasks()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    search_pattern = f'%{query}%'
    
    cursor.execute("SELECT * FROM tasks WHERE column_name = 'todo' AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ?) ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END", 
                   (search_pattern, search_pattern))
    todo = [dict(row) for row in cursor.fetchall()]
    
    cursor.execute("SELECT * FROM tasks WHERE column_name = 'progress' AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ?) ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END", 
                   (search_pattern, search_pattern))
    progress = [dict(row) for row in cursor.fetchall()]
    
    cursor.execute("SELECT * FROM tasks WHERE column_name = 'done' AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ?) ORDER BY CASE priority WHEN 'high' THEN 1 WHEN 'medium' THEN 2 WHEN 'low' THEN 3 END", 
                   (search_pattern, search_pattern))
    done = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({'todo': todo, 'progress': progress, 'done': done})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)