class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty. Cannot pop.")
            return None
        popped_item = self.top.item
        self.top = self.top.next
        return popped_item

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        return self.top.item

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        if current is None:
            print("Stack is empty.")
            return
        while current:
            print(current.item, end=" -> ")
            current = current.next
        print("None")
