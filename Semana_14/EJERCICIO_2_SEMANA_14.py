class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Double_ended_queue:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    
    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def pop_left(self):
        if self.head is None:  
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:  
            self.tail = None
        return data

    
    def pop_right(self):
        if self.tail is None:  
            return None
        if self.head == self.tail:  
            data = self.tail.data
            self.head = self.tail = None
            return data
        
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        data = self.tail.data
        self.tail = current
        self.tail.next = None  
        return data

    def print_queue(self):
        if self.head is None:
            print("Queue is empty.")
            return
        print("Queue contains:", end=" ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  
