from .loader import Loader

class Tasks:
    def __init__(self): self.tasks=[]
    def add(self,name,func=None): self.tasks.append([str(name),func,"pending"]); return self
    def run(self):
        results=[]
        for task in self.tasks:
            task[2]="running"
            try:
                with Loader(task[0],effect="dots"):
                    result=task[1]() if task[1] else None
                task[2]="done"; results.append(result)
            except Exception:
                task[2]="failed"; raise
        return results
    def status(self): return [(x[0],x[2]) for x in self.tasks]
