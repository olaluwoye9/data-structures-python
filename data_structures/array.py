class Array:
    def __init__(self):
        self.items = []

    def insert(self, item):
        """Insert an item at the end"""
        self.items.append(item)

    def insert_at(self, index, item):
        """Insert an item at a specific index"""
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of range")
        self.items.insert(index, item)

    def delete(self, item):
        """Delete the first occurrence of item"""
        try:
            self.items.remove(item)
        except ValueError:
            print("Item not found.")

    def delete_at(self, index):
        """Delete item at a specific index"""
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")
        self.items.pop(index)

    def update(self, index, new_item):
        """Update item at a specific index"""
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")
        self.items[index] = new_item

    def access(self, index):
        """Access item by index"""
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of range")
        return self.items[index]

    def search(self, item):
        """Check if item is in array"""
        return item in self.items

    def get_length(self):
        return len(self.items)

    def display(self):
        print(self.items)
