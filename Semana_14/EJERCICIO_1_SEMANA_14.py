print("Semana 14. Ejercicio 1 - CAMBIOS SOLICITADOS")

class Node:
    def __init__(self, data, next=None):
        self.data = data  
        self.next = next  

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None  

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)  
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:  # Empty
            print("Stack is empty!")
            return None
        
        popped_node = self.head
        self.head = self.head.next  
        return popped_node  

my_stack = Stack()
my_stack.push(Node("first"))
my_stack.push(Node("second"))
my_stack.push(Node("third"))

print("STACK:")
my_stack.print_structure()

print("\nPOP")
popped = my_stack.pop()
if popped:
    print(f"Deleted element: {popped}")

my_stack.print_structure()