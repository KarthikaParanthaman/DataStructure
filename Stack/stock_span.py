# stock span - no of days from current day going backwards first max
# stocks 4 3 2
# span  (1)(1-0)(2-1)

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
        else:
            return -1

    def find_maxstock_index(self, stocks, price):
        while True:
            top = self.top()
            if stocks[top] < price:
                self.pop()
            else:
                return top
            
        

stocks = [100,80,60,70,60,75,85]
span = []
st = stack()
# create span
for i in range(len(stocks)):
    # first elt span is 1
    if i == 0:
        span.append(1)
    else:
        # current index -  prev max stock index
        maxtop = st.find_maxstock_index(stocks, stocks[i])
        span.append(i - maxtop)
    st.push(i)
    
print(span)
    
        
    
