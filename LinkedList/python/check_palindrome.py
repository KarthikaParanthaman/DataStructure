class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        n = Node(data)
        n.next = self.head
        self.head = n
        
    def print(self):
        current = self.head
        while current != None:
            print(current.data, end= "->")
            current = current.next
    
    def palindrome_notworking(self, l, h):
        
        left = l
        if h == None:
            return True
        
        status = self.palindrome_notworking(left, h.next)
        if status == False:
            return False
        
        eq_status = (left.data == h.data)
        left = left.next 
        
        return eq_status

    def palindrome(self,h, s1 ='', s2 = '')  :
        if h == None:
            return (s1,s2)

        s1 += str(h.data)
        (s1,s2) = self.palindrome(h.next, s1, s2)
        s2 += str(h.data)

        return (s1,s2)
    
        
        

if __name__ == "__main__":
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(2)
    l.add(1)
    l.print()
    # if l.palindrome(l.head, l.head):
    #     print("is palindrome")
    # else:
    #     print("not palindrome")
        
    s1,s2 = l.palindrome(l.head)
    if s1 == s2:
        print(s1, s2, "palindrome")
    else:
        print("not palindrome")
    
        