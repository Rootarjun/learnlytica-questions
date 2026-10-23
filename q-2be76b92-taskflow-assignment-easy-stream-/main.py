def stream_open_tasks(tasks):
    """Yield the 'title' of every task whose status is not 'done'.
    Must be a GENERATOR (use yield) -- do not build and return a list.
    """
    STATUS=["todo","in_progress","review","blocked",""]

    # TODO: loop over tasks and yield the title of each open task
    for i in tasks:
        status=i.get("status","")
        if status in STATUS:
            yield i.get("title")
    