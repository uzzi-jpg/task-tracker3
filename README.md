# Simple Task Tracker

A basic task tracking app like Trello.

## Features

- 3 columns: To Do, In Progress, Done
- Add, delete, and drag tasks between columns
- Saves to localStorage (or backend if available)

## Quick Start

### Option 1: Just HTML

1. Open `index.html` in your browser
2. Tasks save automatically to your browser

### Option 2: With Python Backend

1. Install Flask:

   ```bash
   pip install Flask flask-cors
   ```

2. Run the server:

   ```bash
   python app.py
   ```

3. Open `index.html` in your browser

## Files

- `index.html` - The webpage
- `app.py` - Python Flask backend
- `requirements.txt` - Python packages needed

## How to Use

1. Click "+ Add Task" to create a task
2. Drag tasks between columns to change status
3. Click "Delete" to remove a task

## API Endpoints (if using backend)

- `GET /tasks` - Get all tasks
- `POST /tasks` - Save all tasks
- `POST /tasks/<column>` - Add task to column
- `DELETE /tasks/<column>/<id>` - Delete task
