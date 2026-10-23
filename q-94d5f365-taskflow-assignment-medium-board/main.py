def summarize_tasks(tasks, include_rate=True):
    by_status = {}
    for t in tasks:
        # TODO: count tasks per status; use 'unknown' when 'status' is missing
        pass
    total = len(tasks)
    result = {'total': total, 'by_status': by_status}
    if include_rate:
        # TODO: add 'rate' = percent of 'done' tasks (1 decimal). 0.0 when empty.
        pass
    return result