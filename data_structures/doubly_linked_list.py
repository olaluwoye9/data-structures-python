class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node_item, item):
        temp = self.head
        while temp and temp.item != prev_node_item:
            temp = temp.next
        if not temp:
            print("Previous node not found.")
            return
        new_node = Node(item)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def insert_at_end(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at(self, index, item):
        if index == 0:
            self.insert_at_beginning(item)
            return
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        if not temp:
            raise IndexError("Index out of range")
        new_node = Node(item)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_item(self, key):
        temp = self.head
        while temp:
            if temp.item == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Item not found.")

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def access(self, index):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.item
            temp = temp.next
            count += 1
        raise IndexError("Index out of range")

    def update(self, index, new_item):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                temp.item = new_item
                return
            temp = temp.next
            count += 1
        raise IndexError("Index out of range")

    def display(self):
        node = self.head
        while node:
            print(node.item, end=" <--> ")
            node = node.next
        print("NULL")
