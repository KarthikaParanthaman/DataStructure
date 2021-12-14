class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,data):
        self.arr.append(data)
    
    def isempty(self):
        return len(self.arr) == 0
    
    def pop(self):
        self.arr.pop()
        # if not self.isempty():
        #     index = len(self.arr) - 1
        #     self.arr.pop(index)
            
    def top(self):
        if not self.isempty():
            index = len(self.arr) - 1  
            return self.arr[index]          

if __name__ == "__main__":
    s = stack()
    s.push('a')
    s.push('n')
    s.push('d')
    while not s.isempty():
        print(s.top())
        s.pop()
            
