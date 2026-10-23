def merge_pages(pages, status=None):
    # Merge paginated response pages into one de-duplicated, sorted list.
    # If status is given, keep only tasks with that status.
    if not pages:
        return []
    pages=sorted(pages,key=lambda x:x.get("page"))
    id_set=set()
    result_set=[]
    for i in pages:
        result=i.get("results")
        if not result:
            continue
        for j in result:
            id=j.get('id')
            stat=j.get('status')
            if id not in id_set:
                if status is None or status==stat:
                     id_set.add(id)
                     result_set.append(j)
    return sorted(result_set,key=lambda x:x.get("id"))
            
        

def pages_fixture():
    return [
        {"page": 2, "next": False, "results": [
            {"id": 4, "status": "done"},
            {"id": 5, "status": "todo"},
        ]},
        {"page": 1, "next": True, "results": [
            {"id": 1, "status": "todo"},
            {"id": 2, "status": "done"},
            {"id": 3, "status": "todo"},
            {"id": 4, "status": "done"},
        ]},
    ]
#print(merge_pages(pages_fixture()))