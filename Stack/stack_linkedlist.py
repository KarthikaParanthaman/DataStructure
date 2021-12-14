class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def pop(self):
        if not self.isempty():
            temp = self.head
            self.head = self.head.next
            temp = None
    
    def isempty(self):
        return self.head == None
    
    def top(self):
        if not self.isempty():
            return self.head.data

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    while not s.isempty():
        print(s.top())
        s.pop()
    