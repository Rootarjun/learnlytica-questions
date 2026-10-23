"""TaskFlow S9 - Medium. Complete the hierarchy and the reporting function."""

class TaskFlowError(Exception):
    pass

class ValidationError(TaskFlowError):
    pass

# TODO: MissingFieldError and InvalidValueError, both subclasses of ValidationError
class MissingFieldError(ValidationError):
    pass

class InvalidValueError(ValidationError):
    pass


VALID_STATUSES = {"todo", "in_progress", "done", "blocked"}
REQUIRED_FIELDS = ("title", "status", "priority")

def validate_task(task):
    # TODO: raise MissingFieldError("missing field: <name>") for any absent required field.
    # TODO: raise InvalidValueError for: empty/whitespace title, bad status,
    #       priority not an int in 1..5 (reject booleans too). Return True if ok.
    for field in REQUIRED_FIELDS:
        if field not in task:
            raise MissingFieldError(f"missing field: {field}")
        title=task["title"]
        status=task["status"]
        priority=task["priority"]

        if not isinstance(title,str) or not title.strip():
            raise InvalidValueError("invalid title")

        if not isinstance(status,str) or status not in VALID_STATUSES:
            raise InvalidValueError(f"invalid status: {status}")

        if isinstance(priority,bool) or not isinstance(priority,int) or not 1<=priority<=5:
            raise InvalidValueError(f"invalid priority: {priority}")
    return True


def validate_task_report(task):
    # TODO: call validate_task inside try/except/else/finally and build a report dict:
    #   ok      -> {"valid": True,  "error_type": None,               "message": "ok"}
    #   missing -> {"valid": False, "error_type": "MissingFieldError","message": <str(exc)>}
    #   invalid -> {"valid": False, "error_type": "InvalidValueError","message": <str(exc)>}
    # In finally, add result["checked"] = True. Return the report.
    result={}
    try:
        validate_task(task)
    except MissingFieldError as exc:
        result["valid"]=False
        result["error_type"]=type(exc).__name__
        result["message"]=str(exc)
    except InvalidValueError as exc:
        result["valid"]=False
        result["error_type"]=type(exc).__name__
        result["message"]=str(exc)
    else:
        result["valid"]=True
        result["error_type"]=None
        result["message"]="ok"
    finally:
        result["checked"]=True
    
    return result