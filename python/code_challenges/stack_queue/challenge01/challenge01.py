# Write here the code challenge solution
class Node:
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue
        
class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    
    

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if not self.rear: # if the queue empty
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        if self.front == None:
            return("This queue is empty")        
        if self.front == self.rear:
            self.rear = None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.front == None:
            return("This queue is empty")        
        return self.front.value