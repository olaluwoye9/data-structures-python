## Data-Structures-Python

A beginner-friendly Python package that implements classic data structures from scratch using object-oriented Python. Designed to help learners understand how data structures work under the hood without relying on Python’s built-in abstractions.

Whether you're a coding bootcamp student, computer science learner, or self-taught developer — this package is for you.

## Why This Project?

Most learners rely on built-in Python data types (lists, sets, dicts) without truly understanding how they work under the hood. While these data types provide convenient abstractions, knowing how to implement core data structures from scratch helps solidify your understanding of programming concepts.

This project aims to bridge that gap by providing clear and simple implementations of fundamental data structures. It’s an ideal resource for:

- Beginners: Anyone learning to code and wants to understand data structures.

- Bootcamp students: Those preparing for technical interviews.

- Software engineers: Developers transitioning into fields that require data structure knowledge.


## 🧠 What’s Inside?

This package provides detailed implementations and clean interfaces for the following data structures:

| Data Structure       | Description |
|----------------------|-------------|
| ✅ **Array**          | Dynamic array with index-based operations |
| ✅ **Stack**          | LIFO stack implemented using both a Python list and a linked list |
| ✅ **Queue**          | FIFO queue implemented using a list |
| ✅ **Linked List**    | Singly linked list with insert, delete, search, and update operations |
| ✅ **Doubly Linked List** | Bi-directional traversal with flexible insert/delete |
| ✅ **Binary Search Tree (BST)** | Recursive insert, search, and in-order traversal for efficient searching |
| ✅ **Graph**          | Undirected graph using an adjacency list to represent connections between node |

All implementations are **self-contained**, easy to understand, and extensible for future improvements (e.g., weighted graphs, AVL trees, etc.).

---

## 🚀 Project Structure

The data-structures-python package is organized into several modules and folders:

data-structures-python/

| **Data Structure**      | **Description** |
|----------------------|-------------|
| ✅ *data_structures*          | Core package code |
| ✅ *array.py*         |Stack using Python list |
| ✅ *stack_linked.py*         | Stack using Linked List |
| ✅ *queue.py*    | Queue implementation |
| ✅ *linked_list.py* | Singly Linked List implementation |
| ✅ *doubly_linked_list.py* | Doubly Linked List implementation|
| ✅ *Graph.py*          | Graph implementation |
| **examples**/       |              |
|----------------------|-------------|
| ✅ *stack_example.ipynb* | Example showing stack usage |
| ✅ *queue_example.ipynb* | Example showing queue usage |
| ...                        | Other examples for different data structures | 
| **README.md**/                 | Project overview and documentation|
|----------------------|-------------|
| **LICENSE**/             | License file for the project |
|----------------------|-------------|
| **setup.py** /           | Setup script for installing the package |
|----------------------|-------------|
| **pyproject.toml** /     | Project metadata and configuration |

---
## 🚀 Installation

Once the package is published on PyPI (Python Package Index), you can install it using the following command:

Once published on PyPI, install using:

```bash
pip install Olaluwoye-data-structures

## Manual Installation
You can also install the package directly from GitHub for development or testing purposes:

pip install git+https://github.com/olaluwoye9/data-structures-python.git

```
---
## Example Usage
Here’s a simple example of how to use the Array class from the package:

**1. Array**

from data_structures.array import Array

- arr = Array() # Create a new array

- arr.insert(10)

- arr.insert(20)

- arr.insert(30)

- print(arr.access(1))  # Access and print an item by index

**2. Stack**

from data_structures.stack import Stack

- stack = Stack() # Create a new stack

- stack.push(10) # Push some items to the stack

- stack.push(20)

- stack.push(30)

- print(stack.pop())  # Pop an item from the stack

- print(stack.peek())  # Peek the top item

- print(stack.is_empty())  # Check if the stack is empty

**3. Queue**

from data_structures.queue import Queue

- queue = Queue() # Create a new queue

- queue.enqueue(10) # Enqueue some items

- queue.enqueue(20)

- queue.enqueue(30)

- print(queue.dequeue())  # Dequeue an item from the queue

- print(queue.peek())  # Peek the front item 

- print(queue.is_empty())  # Check if the queue is empty

**4. Linked List**

from data_structures.linked_list import LinkedList

- linked_list = LinkedList() # Create a new linked list

- linked_list.insert_at_beginning(10) # Insert items at the beginning

- linked_list.insert_at_beginning(20)

- linked_list.insert_at_beginning(30)

- linked_list.display()  # Display the linked list

- linked_list.delete_item(20) # Delete an item

- linked_list.display()  # Display the linked list after deletion

- print(linked_list.search(10))  # Search for an item

**5. Doubly Linked List**

from data_structures.doubly_linked_list import DoublyLinkedList

- dll = DoublyLinkedList() # Create a new doubly linked list

- dll.insert_at_beginning(10) # Insert at the beginning

- dll.insert_at_beginning(20)

- dll.display()  # Display the doubly linked list

- dll.insert_at_end(30) # Insert at the end

- dll.display()  # Display after insertion

- dll.delete_item(10) # Delete an item

- dll.display()  

**6. Binary Search Tree (BST)**

from data_structures.tree import BinarySearchTree

- bst = BinarySearchTree() # Create a new binary search tree

- bst.insert(20)  # Insert some values

- bst.insert(10)

- bst.insert(30)

- print(bst.search(10)) # Search for a value

- print(bst.search(25))  

- bst.inorder_traversal() # In-order traversal

**7. Graph**

from data_structures.graph import Graph

- graph = Graph() # Create a new graph

- graph.add_edge('A', 'B') # Add nodes and edges

- graph.add_edge('A', 'C')

- graph.add_edge('B', 'D')

- graph.display()  # Display the graph

**For Other Data Structures:**

For additional details on Stacks, Queues, Linked Lists, Binary Search Trees, Graphs, and other data structures, please refer to the documentation. The implementation is fully self-contained, and you can easily modify or extend it as needed. Whether you want to create a priority queue, implement an AVL tree, or work with weighted graphs, the package can be extended to meet your requirements.

---

## Author

Created by: Olalekan T. OLALUWOYE — MSc; Statistics & Big Data.

📧 Email: oolaluwoye@aimsammi.org, olaluwoye9@gmail.com  
🔗 LinkedIn: [linkedin.com/in/olaluwoye-olalekan](linkedin.com/in/olaluwoye-olalekan-612a92147)

---

## Live Documentation

Access the live documentation here:  
👉 [Live Docs - data-structures-python](https://yourusername.github.io/data-structures-python/)


