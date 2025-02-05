class Node:
    def __init__(self, head, next=None):
        self.head = head  
        self.next = next  


class Stack:
    def __init__(self):
        self.head = None  

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.head)  
            current_node = current_node.next

    def push(self, new_node):

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:  # If it is empty
            print("Stack is empty!")
            return None
        
        popped_node = self.head
        self.head = self.head.next  
        return popped_node  


first_node = Node("first")
my_stack = Stack()

my_stack.push(first_node)

second_node = Node("second")
my_stack.push(second_node)

third_node = Node("third")
my_stack.push(third_node)


print("STACK:")
my_stack.print_structure()


print("\nPOP")
popped = my_stack.pop()
print(f"Deleted element: {popped.head}")
my_stack.print_structure()

print("\nPOP")
popped = my_stack.pop()
print(f"Deleted element: {popped.head}")
my_stack.print_structure()

print("\nPOP")
popped = my_stack.pop()
print(f"Deleted element: {popped.head}")
my_stack.print_structure()

print("\nPOP")
popped = my_stack.pop()
if popped:
    print(f"Deleted element: {popped.head}")
my_stack.print_structure()

print("\nPOP")
popped = my_stack.pop()
if popped:
    print(f"Deleted element: {popped.head}")
my_stack.print_structure()



