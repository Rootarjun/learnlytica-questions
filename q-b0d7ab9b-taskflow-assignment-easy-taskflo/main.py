class Task:
    """Base task in the TaskFlow board.
    Store title and priority; every new task starts with status 'todo'.
    """
    def __init__(self, title, priority='medium'):
        # TODO: set self.title, self.priority, self.status
        pass

    def label(self):
        # TODO: return f"[TASK] <title> (<priority>)"
        pass


class BugTask(Task):
    """A bug. Adds a `severity` (default 'minor'). Reuse Task via super()."""
    def __init__(self, title, priority='medium', severity='minor'):
        # TODO: call super().__init__(...) then set self.severity
        pass

    def label(self):
        # TODO: return f"[BUG] <title> (<priority>/<severity>)"
        pass


class FeatureTask(Task):
    """A feature. Adds `story_points` (default 1). Reuse Task via super()."""
    def __init__(self, title, priority='medium', story_points=1):
        # TODO
        pass

    def label(self):
        # TODO: return f"[FEATURE] <title> (<priority>) sp=<story_points>"
        pass