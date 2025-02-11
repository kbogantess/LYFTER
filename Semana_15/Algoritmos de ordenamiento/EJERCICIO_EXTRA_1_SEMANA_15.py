class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def bubble_sort(self):
        end = None

        while end != self.head:
            current = self.head
            while current.next != end:
                next_node = current.next

                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data

                current = next_node

            end = current

third_node = Node("I am the third node")
second_node = Node("I am the second node", third_node)
first_node = Node("I am the first node", second_node)

linked_list = LinkedList(first_node)

print("before sorting: ")
linked_list.print_structure()

linked_list.bubble_sort()

print("\nAfter sorting: ")
linked_list.print_structure()
