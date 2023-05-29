class NestedList():
    def __init__(self,val):
        self.val  =  val
    def is_integer(self):
        return isinstance(self.val, int)
    def get_interger(self):
        return self.val if self.is_integer() else None
    def get_list(self):
        return None if self.is_integer() else self.val

class NestedInteger():  
    def __init__(self,val):
        self.val = val
    def next(self):
        pass
    def has_next(self):
        
        pass