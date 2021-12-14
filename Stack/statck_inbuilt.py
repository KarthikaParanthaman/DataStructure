from queue import LifoQueue

def insert_bottom(s, data):
    if s.empty():
        s.put(data)
        return
    
    temp = s.get()
    insert_bottom(s, data)
    s.put(temp)
    
def reverse(s):
    if s.empty():
        return

    temp = s.get()
    reverse(s)
    insert_bottom(s,temp)

s = LifoQueue(maxsize=5)

s.put(1)
s.put(2)
s.put(3)
#insert_bottom(s, 4)
reverse(s)
print(f"size: {s.qsize()}")
print(f"is full: {s.full()}")
while not s.empty():
    print(s.get())