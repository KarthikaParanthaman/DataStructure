class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, end = "->")
            current = current.next      
    
    def alternate_merge(self,  list2):
        l1 = self.head
        l2 = list2.head
        while l1 != None :
            tl2 = l2
            tl1 = l1
            l2 = l2.next
            l1 = l1.next
            tl2.next = tl1.next
            tl1.next = tl2
            if l2 == None:
                break
        return self.head
    
    def merge_two_list(self, l1, l2):
        if l1 == None:
            self.head = l2
            return
        
        if l2 == None:
            return
        
        if l1.data > l2.data:
            tmp = l2
            l2 = l1
            l1 = tmp
            
        head = l1
        while l1 != None and l2 != None:
            if l1.data <= l2.data:
                if l1.next != None :
                    if l1.next.data > l2.data:
                        #insert after l1
                        # move l1 and l2
                        tmp = l2
                        l2 = l2.next
                        tmp.next = l1.next
                        tmpl1 = l1
                        tmpl1.next = tmp
                        l1 = l1.next
                        continue
                    else:
                        # move l1
                        l1 = l1.next
                        continue
                else:
                    l1.next = l2
                    break
                        
            
        # if l2 != None and l1 == None:
        #     prev_l1.next = l2
        
        self.head = head
        return head   
  
    def mergeTwoLists_notworking(self,l1, l2):
        head = self.head
        list1 = head
        list2 = l2.head

        while list1 != None :
          
            if list2 == None:
                break
            tl1 = list1
            tl2 = list2
            if list1.data <= list2.data :
                print(list1.data, list2.data)  
                #insert after
                list1 = list1.next
                list2 = list2.next
                tl2.next = tl1.next
                tl1.next = tl2                
            else:
                if list1.next == None:
                    break
                list1 = list1.next


        if list2 != None:
            # list1 last element present
            if list1 != None :
                list2.next
        
        self.head = head
                
                
        
            
if  __name__ == "__main__":
    list1 = LinkedList()
    # list1.add_end(1)
    list1.add_end(2)
    # list1.add_end(4)
    
    list2 = LinkedList()
    list2.add_end(1)
    # list2.add_end(2)
    # list2.add_end(5) 
    
    #list1.alternate_merge(list2)
    list1.merge_two_list(list1.head, list2.head)
    list1.print_list()
    
      
        
    