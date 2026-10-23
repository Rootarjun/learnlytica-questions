import json


def status_counts_json(tasks):
    if tasks is None:
        return "{}"
    counts = {}
    # TODO: tally each task's status into counts (missing/empty status -> 'unknown')
    for i in tasks:
        
        status=i.get("status","")
        if not status:
            status="unknown"
        
        counts[status]=counts.get(status,0)+1

    
    return json.dumps(counts,sort_keys=True) if counts else {}


    # TODO: return the tally as a sorted-key JSON string
    pass

#print(status_counts_json([{'status':'todo'}]))