from typing import List

class Stack:
    def __init__(self):
        self.stack = []
    
    def __repr__(self) -> str:
        return f'Stack -> {self.stack}'

    def size(self):
        '''Returns the size of the stack'''
        return len(self.stack)
    
    def peek(self, position: int = 1):
        '''Allows to see the element for a position in the stack'''
        return self.stack[-position] if position <= self.size() else None
    
    def insert(self, val:int) -> List:
        '''Inserts a value into the stack

        Args:
            val: Integer value
        '''
        return self.stack.append(val)
        
    def remove(self) -> int:
        '''Removes the top value from the stack'''
        if not self.isEmpty():
            return self.stack.pop(-1)
        else:
            print('Stack is empty')
            return None

    def isEmpty(self) -> bool:
        '''Checks whether the stack is empty'''
        return len(self.stack) == 0

s1 = Stack()
print(s1)

s1.insert(1)
print(s1)
s1.insert(2)
s1.insert(4)
s1.insert(10)
s1.insert(12)
print(s1)

print(s1.remove())
print(s1)

print(s1.isEmpty())

print(s1.peek())
print(s1.peek(3))
print(s1.peek(5))
print(s1)

print(s1.size())

s2 = Stack()
print(s2)
print(s2.remove())