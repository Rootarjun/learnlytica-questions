def commits_fixture():
    return [
        {'id': 'a1', 'parent': None, 'message': 'init TaskFlow repo'},
        {'id': 'b2', 'parent': 'a1', 'message': 'add Task model'},
        {'id': 'c3', 'parent': 'b2', 'message': 'add status field'},
        {'id': 'd4', 'parent': 'c3', 'message': 'add priority field'},
    ]

def history_messages(commits, head_id):
    # walk parent pointers from head_id, collecting messages newest-first
    pass
