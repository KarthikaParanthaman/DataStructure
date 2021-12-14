class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            
    def add_pos(self, data, pos):
        new_node = Node(data)
        #handle no element
        if self.head == None:
            self.head = new_node
        else:
            if pos == 0:
                self.add_beginning(data)
                return
            
            current = prev = self.head
            count = 0
            # inset after pos 
            while count < pos :
                prev = current
                current = current.next
                count += 1
            
            new_node.next = current
            prev.next = new_node

    def search(self, data):
        current = self.head
        index = 0
        while current != None:
            if current.data == data:
                return index
            else:
                current = current.next
                index += 1
        return -1
    
    def recursive_search(self,node,data):

        if node == None:
            return -1
        if node.data == data:
            return 0
        else:
            subindex = self.recursive_search(node.next, data)
            if subindex == -1:
                return -1
            else:
                return subindex+1
    
    def delete_all(self):
        current = self.head
        while current.next != None:
            del_node = current
            current = current.next
            print("deleting node ", del_node.data)
            del_node = None
        current = None
        self.head = None
        
    def delete(self, data):
        current = prev = self.head
        while current != None:
            if current.data == data:
                prev.next = current.next
                current = None
                return
            
            prev = current
            current = current.next
            
    def delete_beginning(self):
        current = self.head
        if current == None:
            return
        else:
            self.head = current.next
            current = None
      
    def delete_end(self):
        current = prev = self.head
        if current == None:
            return
        else:
            while current.next != None:
                prev = current
                current = current.next
            prev.next = None
            current = None
            
    def reverse_list(self):
        current = self.head
        rhead = None
        while current != None:
            new_node = current
            current = current.next
            new_node.next = rhead
            rhead = new_node
        self.head = rhead

    def kth_last_element(self, k):
        second = first = self.head
        # move second pointer to kth element from head
        while k > 1 :
            if second == None:
                return
            else:
                second = second.next
                k -= 1

        # move both first and second pointer 1 step at a time
        while second.next != None:
            first = first.next
            second = second.next
        
        return first.data
        
        
            
        
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, end = "->")
            current = current.next
            
    def rprint_list(self, node):
        if node == None:
            return node
        data = self.rprint_list(node.next)
        print( data, node.data,end = " - ")
    

if __name__ == "__main__":
    list = LinkedList()
    list.add_beginning(5)
    list.add_beginning(4)
    list.add_beginning(3)
    list.add_end(6)
    list.add_pos(1,0)
    list.print_list()
    print()
    list.rprint_list(list.head)
    # print(list.search(15))
    # print(list.recursive_search(list.head, 15))
    # #list.delete_beginning()
    # #list.delete_end()
    # list.reverse_list()
    
    # #list.delete(3)
    # #list.delete_all()
    # list.print_list()
    # print()
    # print(list.kth_last_element(2))
        