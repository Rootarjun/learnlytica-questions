def to_task_response(task):
    """Shape a raw TaskFlow task dict into an API response dict.

    Return a dict with exactly these keys:
      - "task_id"      -> task["id"] (or None if absent)
      - "title"        -> task["title"] (empty string "" if missing/None)
      - "status"       -> task["status"] (default "todo" if missing/None)
      - "is_completed" -> True only when the (defaulted) status == "done"
    """
    # TODO: read fields safely and build the response dict
    title = ...
    status = ...
    return {
        "task_id": ...,
        "title": ...,
        "status": ...,
        "is_completed": ...,
    }