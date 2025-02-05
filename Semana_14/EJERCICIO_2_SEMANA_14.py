class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev  

class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data, next=self.head)
        if self.head is None:  
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node  
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data, prev=self.tail)
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
        else:
            self.head.prev = None  
        return data

    def pop_right(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev  
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None  
        return data

    def print_queue(self):
        if self.head is None:
            print("Queue is empty.")
            return
        print("Queue (left to right):", end=" ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

        print("Queue (right to left):", end=" ")
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


deque = DoubleEndedQueue()
deque.push_left(1)
deque.push_right(2)
deque.push_left(0)
deque.push_right(3)

deque.print_queue()

print("\nPOP LEFT:", deque.pop_left())
deque.print_queue()

print("\nPOP RIGHT:", deque.pop_right())
deque.print_queue()

