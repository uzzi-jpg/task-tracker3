import sqlite3
import os

def migrate_database():
    """
    Migrate existing tasks.db to include priority column
    """
    if not os.path.exists('tasks.db'):
        print("No existing tasks.db found. A new one will be created when you run app.py")
        return
    
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # Check if priority column exists
    cursor.execute("PRAGMA table_info(tasks)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'priority' in columns:
        print("✅ Database already has priority column. No migration needed!")
    else:
        print("📊 Adding priority column to existing database...")
        cursor.execute("ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'medium'")
        conn.commit()
        print("✅ Migration complete! All existing tasks now have 'medium' priority.")
        print("   You can change priorities when editing tasks.")
    
    conn.close()

if __name__ == '__main__':
    print("=" * 50)
    print("Task Tracker Database Migration")
    print("=" * 50)
    migrate_database()
    print("\nYou can now run: python app.py")