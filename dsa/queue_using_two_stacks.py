class QueueStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add_to_queue(self, val):
        self.stack1.append(val)
        self.stack2.insert(0, val)
    
    def remove_from_queue(self):
        return self.stack2.pop()

q = QueueStack()
q.add_to_queue(18)
q.add_to_queue(24)
q.add_to_queue(2)

print(q.remove_from_queue()) #18
print(q.stack1, q.stack2)

q.add_to_queue(11)

print(q.remove_from_queue()) #24
print(q.stack1, q.stack2)

print(q.remove_from_queue()) # 2
print(q.stack1, q.stack2)