# TaskFlow — this sprint has four tasks, in order:
#   "Design login page", "Write API tests", "Fix payment bug", "Deploy release"

# TODO: build a list called task_titles with the four titles above, in order
task_titles = ["Design login page", "Write API tests", "Fix payment bug", "Deploy release"]

# TODO: first_task  = the first title in the list (indexing)
first_task = task_titles[0]

# TODO: last_task   = the last title in the list (indexing, e.g. [-1])
last_task = task_titles[-1]

# TODO: task_count  = how many titles are in the list (len)
task_count= len(task_titles)

# TODO: has_deploy  = is "Deploy release" in the list? (membership with in)
has_deploy = "Deploy release" in task_titles