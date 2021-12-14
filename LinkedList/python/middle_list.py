class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_end(self, data):
        n = Node(data)
        if self.head == None:
            print("adding data", data)            
            self.head = n
        else:
            current = self.head
            while current.next != None:
                current = current.next
            print("adding data", data)
            current.next = n
            
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, end ="->")
            current = current.next
    
    def middle(self):
        first = second = self.head
        while second.next != None:
            print(first.data, second.data)
            first = first.next
            pos = 2
            while second.next != None and pos > 0 :
                second = second.next
                pos -= 1            

        print(first.data)
        
        
            
if __name__ == "__main__":
    l = LinkedList()
    l.add_end(1)
    l.add_end(2)
    l.add_end(3)
    l.add_end(4)
    #l.add_end(5)    
    l.print_list()
    print("middle element")
    l.middle()
    