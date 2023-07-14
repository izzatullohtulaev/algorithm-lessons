class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack)==0
    def push(self, data):
        self.stack.append(data)
        return True
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty!")
            return
        else:
            return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            print("The stack is empty")
            return 
        else:
            return self.stack[-1]
    