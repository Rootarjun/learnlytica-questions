# TaskFlow sprint board — each task is a tuple: (id, title, status, assignee, hours)
tasks = [
    (1, "Design login page", "done", "Ava", 4.0),
    (2, "Write API tests", "todo", "Ben", 3.0),
    (3, "Fix payment bug", "in_progress", "Ava", 5.5),
    (4, "Deploy release", "todo", "Cara", 2.0),
    (5, "Review PR", "done", "Ben", 1.5),
]

# Start with empty containers, then fill them in ONE for loop over tasks:
task_titles = []       # TODO: append each title (t[1])
status_counts = {}     # TODO: count each status (t[2]) with if/else
unique_assignees = set()  # TODO: add each assignee (t[3])
total_hours = 0.0      # TODO: add each hours value (t[4])

for i in tasks:
    task_titles.append(i[1])

    s_c=i[2]
    if s_c in status_counts:
        status_counts[s_c]+=1
    else:
        s_c=1
    
    unique_assignees.add(i[3])
    total_hours+=i[4]



# After the loop:
# TODO: sorted_titles  = task_titles sorted alphabetically (use sorted)
sorted_titles = sorted(task_titles)

# TODO: assignee_count = number of distinct assignees (len of the set)
assignee_count = len(unique_assignees)

# TODO: has_ava        = is "Ava" one of the assignees? (membership with in)
has_ava = "Ava" in unique_assignees