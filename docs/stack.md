# Stack

## What is a Stack?

A **stack** is a Last-In-First-Out (LIFO) structure.

A **Last-In-First-Out (LIFO)** structure implemented in two ways:
- Using a Python list (`stack.py`)
- Using a linked list (`stack_linked.py`)

### Supported Operations

- `push(item)`
- `pop()`
- `peek()`
- `is_empty()`

### Example

```python
from data_structures.stack import Stack

s = Stack()
s.push(1)
s.push(2)
print(s.pop())  

