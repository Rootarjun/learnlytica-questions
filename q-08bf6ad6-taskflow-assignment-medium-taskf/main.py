class Task:
    def __init__(self, title, estimate_hours, logged_hours=0):
        self.title = title
        self.estimate_hours = estimate_hours
        self.logged_hours = logged_hours
        

    @property  #converts function to an instance -> getters
    def remaining_hours(self):
        return max(0,self.estimate_hours-self.logged_hours)
    

    @property
    def is_complete(self):
        return self.logged_hours>=self.estimate_hours
    



    def weight(self):
        # base weight is just the estimate (as float)
        return float(self.estimate_hours)
    

class BugTask(Task):
    SEVERITY_MULT = {'minor': 1.0, 'major': 1.5, 'critical': 2.0, 'blocker': 3.0}
    # TODO: __init__ adds `severity`; weight() = base weight * severity multiplier, rounded to 2
    def __init__(self,title,estimate_hours,severity,logged_hours=0):
        super().__init__(title,estimate_hours,logged_hours)
        self.severity=severity

    def weight(self):
        return round(super().weight()*BugTask.SEVERITY_MULT[self.severity],2)


class FeatureTask(Task):
    # TODO: __init__ adds `story_points`; weight() = base weight + story_points*2, rounded to 2
    def __init__(self,title,estimate_hours,story_points,logged_hours=0):
            super().__init__(title,estimate_hours,logged_hours)
            self.story_points=story_points
    
    def weight(self):
        return round(super().weight()+self.story_points*2,2)
    


def build_task(kind, title, estimate_hours, extra, logged_hours=0):
    """Factory. Return 'error: negative estimate' if estimate_hours < 0,
    'error: unknown kind' for an unknown kind, else the built task object."""
    # TODO
    kind_types={'bug':BugTask,'feature':FeatureTask,'task':Task}
    if estimate_hours<0:
        return ValueError("error: negative estimate")
    if kind not in kind_types:
        return ValueError("error: unknown kind")
    if kind=="task":
        return Task(title,
        estimate_hours,logged_hours)
    y=kind_types[kind]
    return y(title,estimate_hours,extra,logged_hours)
    
print(FeatureTask('Dark mode',10,3).weight()) # → 16.0
print(BugTask('Crash',8,'critical').weight()) #→ 16.0
print(Task('X',8,3).remaining_hours) #→ 5

'''FAIL
Remaining clamps at 0
FAIL
Complete when logged==estimate
FAIL
Not complete
FAIL
Unknown kind
FAIL
Negative estimate
FAIL
Factory base task uses estimate'''