class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def printtree(root):
    if root == None:
        return
    print(root.data, end = " ")
    printtree(root.left)
    printtree(root.right)
    
def issymmetric(l, r):
    if l == None or r == None:
        return l == r
    if l.data != r.data:
        return False
    
    return issymmetric(l.left, r.right) and issymmetric(l.right, r.left)
    
    
    

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')    
    d = Node('d')     
    b1 = Node('b')
    c1 = Node('c')
    d1 = Node('d')      
    
    a.left = b
    a.right = b1
    b.left = c
    b.right = d
    b1.left = d1
    b1.right = c1
    
    printtree(a)
    print(issymmetric(b,b1))
    
    
    