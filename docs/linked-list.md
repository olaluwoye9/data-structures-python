
---

## 📄 `linked-list.md`

```markdown
# Linked List

The `LinkedList` class supports basic operations using singly or doubly linked nodes.

## Singly Linked List
- `insertAtBeginning(item)`
- `insertAtEnd(item)`
- `insertAfter(index, item)`
- `deleteItem(item)`
- `update(index, item)`
- `access(index)`
- `search(item)`
- `display()`

## Example

```python
ll = LinkedList()
ll.insertAtBeginning(1)
ll.insertAtEnd(3)
ll.insertAfter(0, 2)
ll.display()
