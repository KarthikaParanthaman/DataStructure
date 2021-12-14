class stack:
    def __init__(self):
        self.arr = []
    
    def push(self,data):
        self.arr.append(data)
    
    def isempty(self):
        return len(self.arr) == 0
    
    def pop(self):
        self.arr.pop()

    def top(self):
        if not self.isempty():
            index = len(self.arr) - 1  
            return self.arr[index]  
     
    def reverse_num(self, s):
        if s.isempty():
            return 0
        elt = s.top()
        s.pop()
        return self.reverse_num(s) * 10 + elt

        
        return num

if __name__ == "__main__":
    num = 123
    #output 321
    s = stack()
    while num > 0:
        num, r = divmod(num,10)
        s.push(r)
        
    # while not s.isempty():
    #     print(s.top())
    #     s.pop()
    
    #  1 method    
    #print(s.reverse_num(s))
    
    # 2 method
    power = 0
    num = 0
    while not s.isempty():
        num += s.top() * (10 ** power)
        s.pop()
        power += 1
        
    print(num)
        
        
    
