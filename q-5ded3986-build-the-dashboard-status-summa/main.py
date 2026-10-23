STATUSES = ["todo", "in_progress", "review", "done"]


def tasks_fixture():
    return [
        {"id": 1, "title": "Design schema", "status": "done", "priority": 3, "estimate_hours": 4.0},
        {"id": 2, "title": "Build API", "status": "in_progress", "priority": 5, "estimate_hours": 8.0},
        {"id": 3, "title": "Write unit tests", "status": "todo", "priority": 2, "estimate_hours": 3.0},
        {"id": 4, "title": "Deploy to staging", "status": "todo", "priority": 4, "estimate_hours": 2.0},
        {"id": 5, "title": "Review PR", "status": "done", "priority": 1, "estimate_hours": 1.5},
    ]


def build_status_summary(tasks):
    # Return total, by_status (all 4 keys), done, completion_rate,
    # total_estimate_hours, done_estimate_hours.
    summary=dict.fromkeys(["total","by_status","done","completion_rate","total_estimate_hours","done_estimate_hours"],0.0)
    summary["total"]=len(tasks)
    summary["by_status"]=dict.fromkeys(["todo","in_progress","review","done"],0)
    summary["done"]=0
    for i in tasks:
        status=i.get("status")
        estimate_hours=i.get("estimate_hours",0.0)
        count=summary["by_status"].get(status,-1)
        if count!=-1:
            summary["by_status"][status]+=1
        if status=="done":
            summary["done"]+=1
            summary["done_estimate_hours"]+=estimate_hours
        summary["total_estimate_hours"]+=estimate_hours
    
    if summary["total"]==0:
        summary["completion_rate"]=0.0
    else:
        summary["completion_rate"]=summary["done"]/summary["total"]
    
    summary["completion_rate"] = round(summary["completion_rate"],4)
    summary["total_estimate_hours"]=round(summary["total_estimate_hours"],4)
    summary["done_estimate_hours"]=round(summary["done_estimate_hours"],4)
    return summary
    
#print(build_status_summary(tasks_fixture()))