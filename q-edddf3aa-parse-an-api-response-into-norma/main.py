def extract_tasks(response):
    # Return a sorted list of normalised task dicts from an API response.
    if not isinstance(response,dict) or response.get("status")!="ok":
        return []
    
    
    data=response.get('data',[])

    if not data:
        return data
    li=[]
    for i in data:
        if not i.get("id"):
            continue
        i['id']=int(i['id'])
        i["title"]=i.get("title",'').strip()
        i["status"]=str(i.get("status")).lower().strip()
        
        if i["status"] not in ["todo","in_progress","review","done"]:
            i["status"]="todo"
        try:
            i["priority"]=int(i.get("priority","3"))
        except Exception as e:
            i["priority"]=3
        
        i["priority"]=min(max(1,i["priority"]),5)
        new_dic={"id":i['id'],"title":i["title"],"status":i["status"],"priority":i["priority"]}
        li.append(new_dic)
    return sorted(li,key=lambda x:x["id"])

def api_fixture():
    return {
        "status": "ok",
        "data": [
            {"id": 3, "title": "  Ship release  ", "status": "In_Progress", "priority": "2"},
            {"id": 1, "title": "Fix login bug", "status": "TODO", "priority": 9},
            {"id": 2, "title": "Write docs", "priority": None},
            {"id": None, "title": "orphan", "status": "done"},
        ],
    }
    
print(extract_tasks(api_fixture()))