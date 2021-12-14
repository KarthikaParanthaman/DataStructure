import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def build_tree(elts):
    q = queue.Queue()
    root = n = Node(elts[0])    
    q.put(root)
    i = 1
    while not q.empty() :
        n = q.get()
        left = elts[i]    
        right = elts[i+1]
        if left != -1:
            l = Node(left)
            q.put(l)
            n.left = l
        if right != -1:
            r = Node(right)
            q.put(r)
            n.right = r
        i += 2

    return root

def printtree(root):
    if root == None:
        return
    print(root.data, end = " ")
    printtree(root.left)
    printtree(root.right)
        

if __name__ == "__main__":
    a = [1, 2, 3, 4, -1, 5, 6, -1, -1, -1, -1, -1, -1]
    root = build_tree(a)
    printtree(root)