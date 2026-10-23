statuses = "tttdirdt"

# TODO: count each status with a single for loop and if/elif/elif/else
todo_count = 0
in_progress_count = 0
review_count = 0
done_count = 0

for ch in statuses:
    if ch=='t':
        todo_count+=1
    elif ch=='i':
        in_progress_count+=1
    elif ch=='r':
        review_count+=1
    else:
        done_count+=1

# TODO: board_state via conditionals
total = len(statuses)
active_count = todo_count + in_progress_count + review_count
board_state="complete" if done_count==total else "not started" if done_count==0 else "mostly done" if done_count>=active_count else "in progress"
print(board_state)
