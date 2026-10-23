# TaskFlow — the status of each task in the sprint (with repeats):
statuses = ["todo", "done", "in_progress", "done", "todo", "done"]

# TODO: build status_counts, a dict mapping each status -> how many times it appears.
#       Use an empty dict, then a for loop over statuses with an if/else.
#       (NO comprehension, NO functions.)
status_counts = {}
for i in statuses:
    if i in status_counts:
        status_counts[i]+=1
    else:
        status_counts[i]=1

# TODO: done_count = number of "done" tasks (read it from status_counts)
done_count = status_counts["done"]

# TODO: total      = total number of tasks (len of statuses)
total = len(statuses)

# TODO: has_todo    = is "todo" one of the keys in status_counts? (membership with in)
has_todo = "todo" in status_counts
