class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster
    
    def roster(self):
        return self._roster
    
    def add_student(self, name, grade):
        if grade in self.roster_:
            self._roster[grade].append(name)
        else:
            self._roster[grade] = [name]
    
    def grade(self, grade):
        return self._roster[grade]
