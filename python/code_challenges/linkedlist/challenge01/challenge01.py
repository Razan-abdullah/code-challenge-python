# Write here the code challenge solution
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    
    
    
    def __init__(self):
        self.head = None

    def add_new_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            
            
            
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
            
            
            
    def print(self):

        list=[]
        if self.head is None :
            print("The linked list is empty")
        else :
            current = self.head
            while current is not None:
                list.add_new_node(current.value)
                print(current.value)

                current = current.next
        print(list)
        return list