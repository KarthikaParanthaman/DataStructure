class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root, data):
    if root == None:
        return Node(data)
    if data <= root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
        
    return root

def printinorder(root):
    if root == None:
        return None
    printinorder(root.left)
    print(root.data, end = " ,")
    printinorder(root.right)
 
# O(H) log n < O(H)< n    
def search(root, data):
    if root == None:
        return False
    if root.data == data:
        return True
    if data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)
    
def findmin(root):
    while root.left != None:
        root = root.left
    return root
    
def remove(root, data):
    if root == None:
        return None
    if data < root.data:
        root.left = remove(root.left, data)
    elif data > root.data:
        root.right = remove(root.right, data)
    else:
        #node to delete
        # no child
        if root.left == None and root.right == None:
            root = None
        elif root.left == None:
            # right child
            temp = root.right
            root = temp
            temp = None
        elif root.right == None:
            #left child
            temp = root.left
            root = temp
            temp = None
        else:
            # both child exists
            #get inorder successor of root
            temp = findmin(root.right)
            print(f"-{temp.data}-")
            root.data = temp.data
            root.right = remove(root.right, temp.data)            
        return root
            
  
def printrange(root, a, b):
    if root == None:
        return
    
    if a <= root.data <= b:
        printrange(root.left, a, b)
        print(root.data, end = " ")
        printrange(root.right, a, b)
    if root.data < a:
        printrange(root.right, a, b)
    if root.data > b:
        printrange(root.left, a, b)
      
if __name__ == "__main__":
    elts = [5, 3, 6, 1, 2, 7, 8]
    elts = [10,9,8,7,6,4]
    root = None
    for i in elts:
        root = insert(root, i)
    printinorder(root)
    # remove(root,5)
    # print()
    # printinorder(root)
    print()
    printrange(root, 5, 7)
    #print(search(root, 1))