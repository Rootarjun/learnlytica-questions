def dag_fixture():
    return [
        {'id': 'a', 'parents': []},
        {'id': 'b', 'parents': ['a']},
        {'id': 'c', 'parents': ['a']},
        {'id': 'm', 'parents': ['b', 'c']},  # merge commit
        {'id': 'd', 'parents': ['m']},
    ]

def build_commits(commits):
    dic={i['id']:i['parents'] for i in commits}
    return dic

def bfs(commit_id,dic,li=None):
    if li is None:
        li=set()
    if not commit_id:
        return li
    li.add(commit_id)
    for i in dic[commit_id]:
        if i not in li:
            li=bfs(i,dic,li)
    return li     
    

def ancestors(commits, commit_id):
    # sorted list of all transitive ancestor ids (excluding commit_id)
    dic=build_commits(commits)
    if commit_id not in dic:
        return []
    sorted_ancestors=bfs(commit_id,dic,set())
    sorted_ancestors.remove(commit_id)
    return sorted(sorted_ancestors)
    

def is_ancestor(commits, a, b):
    # True if a is an ancestor of b
    return a in ancestors(commits,b)

