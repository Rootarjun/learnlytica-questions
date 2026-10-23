import sqlite3

def sample_users():
    return [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Ben"},
        {"id": 3, "name": "Cara"},
        {"id": 4, "name": "Dan"},
    ]

def sample_tasks():
    return [
        {"id": 100, "title": "Design schema", "status": "done",        "assignee_id": 1},
        {"id": 101, "title": "Build API",     "status": "in_progress", "assignee_id": 2},
        {"id": 102, "title": "Write tests",   "status": "todo",        "assignee_id": 1},
        {"id": 103, "title": "Setup CI",      "status": "todo",        "assignee_id": None},
        {"id": 104, "title": "Deploy",        "status": "review",      "assignee_id": 3},
        {"id": 105, "title": "Docs",          "status": "done",        "assignee_id": 2},
    ]

def no_tasks():
    return []

def all_done_tasks():
    out = []
    for t in sample_tasks():
        t = dict(t); t["status"] = "done"; out.append(t)
    return out

def alt_tasks():
    return [
        {"id": 201, "title": "A1", "status": "todo",        "assignee_id": 1},
        {"id": 202, "title": "A2", "status": "in_progress", "assignee_id": 2},
        {"id": 203, "title": "A3", "status": "review",      "assignee_id": None},
        {"id": 204, "title": "A4", "status": "done",        "assignee_id": 1},
        {"id": 205, "title": "B1", "status": "todo",        "assignee_id": 3},
        {"id": 206, "title": "B2", "status": "done",        "assignee_id": 2},
    ]

def open_tasks_with_assignee(users, tasks):
    # Load users and tasks into an in-memory sqlite3 DB, INNER JOIN them on
    # assignee_id, keep only tasks whose status != 'done', and return a list of
    # (task_title, assignee_name) tuples ordered by task title.
    conn=sqlite3.connect(":memory:")
    cursor=conn.cursor()
    cursor.execute("""Create table users(id Integer primary key, name Text)""")
    cursor.execute(""" Create table tasks(id integer primary key, title text, status text,
                   assignee_id integer)""")
    for user in users:
        cursor.execute("Insert into users(id,name) values (?,?)",(user["id"],user["name"]))
    
    for task in tasks:
        cursor.execute("""Insert into tasks (id,title,status,assignee_id)
                       values (?,?,?,?)""",(task["id"],task["title"],task["status"],task["assignee_id"]))
    cursor.execute("""Select tasks.title, users.name from tasks inner join users on tasks.assignee_id=users.id where
                   tasks.status!='done' order by tasks.title asc""")
    result=cursor.fetchall()
    conn.close()
    return result
        