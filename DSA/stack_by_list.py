class Stack():
    def __init__(self):
        self.stack_list = []
    def push(self, value):
        self.stack_list.append(value)
    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else: 
            return False
    def pop(self):
        if self.is_empty() == True:
            return None
        else:
            self.stack_list.pop()

