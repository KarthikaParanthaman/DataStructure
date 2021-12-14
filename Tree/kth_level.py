import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def build_tree():

    elt = int(input("enter elt: "))
    if elt == -1:
        return None
    n = Node(elt)

    n.left = build_tree()
    n.right = build_tree()
        
    return n

def print_kthlevel(root, k):
    q = queue.Queue()
    q.put(root)
    q.put(None)
    i = 0

    while i < k:
        temp = q.get()
        if temp == None:
            #print("push ",None)
            q.put(None)
            i += 1
            if i == k:
                break                
        else:
            print(temp.data, end="-")
            if temp.left != None:
                #print("push ",temp.left.data)
                q.put(temp.left)
            if temp.right != None:
                #print("push ",temp.right.data)                
                q.put(temp.right)
    l = []
    while not q.empty():  
        temp = q.get() 
        if temp == None:
            break
        l.append(temp.data)      
    
    return l

def preorder( root):
    if root == None:
        return
    print(root.data, end = " ")
    preorder(root.left)
    preorder(root.right)
    
def sum(root):
    if root == None:
        return 0
    return sum(root.left) + sum(root.right) + root.data
  
def evaluate_expression(root):
    if root == None:
        return ''
    return evaluate_expression(root.left) + root.data + evaluate_expression(root.right)
        

if __name__ == "__main__":
    # root = build_tree()
    # preorder(root)
    # #l = print_kthlevel(root, 2)
    # #print(l)
    a = Node(6)
    b = Node(5)
    c = Node(3)
    d = Node(8)
    e = Node(1)
    f = Node(4)
    
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    
    # l = print_kthlevel(a, 0)
    # print(l)
    
    e1 = Node('+')
    e2 = Node('1')
    e3 = Node('*')
    e4 = Node('2')
    e5 = Node('3')
    e1.left = e2
    e1.right = e3
    e3.left = e4
    e3.right = e5
    
    
    #print(sum(a))
    exp = evaluate_expression(e1)
    print(eval(exp))