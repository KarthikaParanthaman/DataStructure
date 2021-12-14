import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def height(root):
    if root == None:
        return 0
    return max(height(root.left)+1, height(root.right)+1)
        
def preorder(root):
    if root == None:
        return
    print(root.data, end = " ")
    preorder(root.left)
    preorder(root.right)
    
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end = " ")    
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)   
    print(root.data, end = " ")       

# print each level in single line
def levelorder(root):
    # create queue and insert root and none(newline)
    q = queue.Queue()
    q.put(root)
    q.put(None)
    
 # 1 none 2 3 none 4 5 6 none  
 # remove elt
 # if none , add newline to stdout and insert none in queue  
 # else print data add its left and right none if exist in queue
    while not q.empty():
        temp = q.get()
        if temp == None:
            print()
            if not q.empty():                
                q.put(None)
                
        else:
            print(temp.data, end = " ")
            if temp.left != None:
                q.put(temp.left)
            if temp.right != None:
                q.put(temp.right)  
                
def mindepth(root)  :
    if root == None:
        return 0
    return min(mindepth(root.left)+1, mindepth(root.right)+1)
    
if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)

    
    a.left = b
    a.right = c
    # # b.left = g
    # # g.left = h
    # c.left = d
    # d.left = e
    # c.right = f
    
    print("preorder")
    preorder(a)
    print("\ninorder")    
    inorder(a)
    print("\npostorder")    
    postorder(a)
    print("\nlevelorder")
    levelorder(a)
    print("\n height", height(a))
    print("\n mindepth: ",mindepth(a))
    
    