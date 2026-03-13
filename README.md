# Task Tracker Enhanced - With Priorities & Search

Enhanced version of the task tracker with priority levels and search functionality!

## 🆕 New Features

### 1. ✅ Task Priorities
- **High Priority** (🔴 Red) - Urgent tasks
- **Medium Priority** (🟡 Yellow) - Normal tasks
- **Low Priority** (🟢 Green) - Can wait

**Features:**
- Color-coded priority badges on each task
- Color-coded left border on task cards
- Automatic sorting by priority (High → Medium → Low)
- Select priority when creating task

### 2. ✅ Search Functionality
- Search by task title or description
- Real-time search across all columns
- "Clear" button to reset search
- Shows "No matching tasks" if nothing found
- Press Enter to search

## 📸 Visual Changes

### **Top Bar:**
```
📋 Task Tracker Pro | [Search Box] [Search] [Clear]
```

### **Task Cards Now Show:**
```
┌─────────────────────────────┐
│ 🔴 HIGH            [Delete] │ ← Priority badge
│ Complete Project            │ ← Title
│ Finish by Friday            │ ← Description
└─────────────────────────────┘
 ▲ Red left border for high priority
```

### **Add Task Form:**
```
Task Title: [_______________]
Description: [____________]
Priority: [🟢 Low ▼]  ← New dropdown
```

## 🗄️ Database Changes

New column added to tasks table:

```sql
ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'medium';
```

**Priority values:**
- `'high'` - Red, sorted first
- `'medium'` - Yellow, sorted second (default)
- `'low'` - Green, sorted last

## 🚀 How to Use

### Installation

```bash
pip install Flask
```

### Running

```bash
python app.py
```

Open: http://localhost:5000

### Using Priorities

1. Click "+ Add Task"
2. Fill in title and description
3. Select priority from dropdown:
   - 🔴 High - Critical tasks
   - 🟡 Medium - Regular tasks
   - 🟢 Low - Nice to have
4. Click "Save"

Tasks automatically sort by priority!

### Using Search

1. Type in the search box at the top
2. Click "Search" or press Enter
3. See filtered results across all columns
4. Click "Clear" to show all tasks again

**Search works on:**
- Task titles
- Task descriptions

**Example searches:**
- "urgent" - finds all tasks with "urgent" in title/description
- "meeting" - finds all meeting-related tasks
- "python" - finds all Python-related tasks

## 📊 Priority Sorting

Tasks are automatically sorted within each column
High priority tasks always appear at the top!


### Prioritization Best Practices:
- **High**: Urgent AND important
- **Medium**: Important but not urgent
- **Low**: Nice to have, not urgent

### Search Tips:
- Search is case-insensitive
- Partial matches work ("meet" finds "meeting")
- Clear search to see all tasks again
- Search across all columns simultaneously

## 📁 File Structure

```
task-tracker-enhanced/
├── app.py              # Flask with priorities & search
├── templates/
│   └── index.html     # Enhanced UI
├── tasks.db           # SQLite database
└── README.md          # This file
```

## 🔄 Migration from Old Version

If you have an existing `tasks.db`, add the priority column:

```bash
sqlite3 tasks.db
```

```sql
ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'medium';
```

Existing tasks will default to 'medium' priority.

## 🆚 Comparison

| Feature | Old Version | Enhanced Version |
|---------|-------------|------------------|
| Add tasks | ✅ | ✅ |
| Delete tasks | ✅ | ✅ |
| Drag & drop | ✅ | ✅ |
| Priorities | ❌ | ✅ Color-coded |
| Search | ❌ | ✅ Full-text |
| Sorting | None | ✅ By priority |
| Top bar | None | ✅ With search |

## 🎯 Future Enhancements

Easy to add:
- Due dates
- Task tags
- Filter by priority only
- Export tasks
- Task statistics by priority

## ⌨️ Keyboard Shortcuts

- **Enter** in search box → Search
- **Drag** task → Move to column

---

**Enjoy your enhanced task tracker!** 🎉