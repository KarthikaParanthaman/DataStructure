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

#i deal solution
# use stack to get next greater elt in array
if __name__ == "__main__":
    v =[4, 5, 3, 25, 27, 1, 2, 6]
    d = {}
    i=0
    n = len(v)
    s = stack()
    while i < n:
        if s.isempty():
            s.push(v[i])
        
        top = s.top()
        if v[i] <= top :
            s.push(v[i])
        else:
            max = v[i]
            
            while max > top:
                d[top] = max
                s.pop()
                if s.isempty():
                    break
                top = s.top()
            
            s.push(max)
        i+=1
            
    while not s.isempty():
        d[s.top()] = -1
        s.pop()

    print(d)
    
    
#push outpu to stack

# if __name__ == "__main__":
#     v =[4,5,3,25,27,1,2,6]
#     s = stack()
#     i, j = (0, 0)
#     while i < len(v):
#         max = v[i]
#         j = i+1
#         push = False
#         while j < len(v):
#             if v[j] > max:
#                 s.push(v[j])
#                 push = True
#                 break
#             j += 1
#         if not push:
#             s.push(-1)
#         i += 1
#         #s.push(-1)


   
#     while not s.isempty():
#         print(s.top())
#         s.pop()
    
            
        
        