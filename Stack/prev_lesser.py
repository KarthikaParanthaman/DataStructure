class stack:
    def __init__(self):
        self.a = []
    
    def push(self,data):
        self.a.append(data)
        
    def pop(self):
        self.a.pop()
        
    def top(self):
        index = len(self.a)-1
        if index >= 0:
            return self.a[index]
    
    def isempty(self):
        return len(self.a) == 0
    
if __name__ == "__main__":
    s = stack()

    v = [5,3,2,9,6,8,4]
    n = len(v)
    i = n-1
    d = {}
    while i >= 0:
        if s.isempty():
            s.push(v[i])
        else:
            top = s.top()
            while v[i] < top:
                d[top] = v[i]
                s.pop()
                if s.isempty():
                    break
                top = s.top()
            s.push(v[i])
        i -= 1
    
    while not s.isempty():
        top = s.top()
        d[top] = -1
        s.pop()

    print(d)
                    
            
        
    