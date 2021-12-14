
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

if __name__ == "__main__":
    s = stack()
    str ="(]"
    open_bracket = ['(','[','{']
    close_bracket = [')',']','}']
    for i in range(len(str)):
        if str[i] in open_bracket :
            s.push(str[i])
        if str[i] in close_bracket:
            if s.isempty():
                print("False")
                break
            else:
                s_top = s.top()
                s.pop()
    
    if not s.isempty():
        print("False")
    else:
        print("True")
            