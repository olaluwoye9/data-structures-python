
---

## 📄 `tree.md`

```markdown
# Binary Search Tree (BST)

The `BinarySearchTree` class organizes nodes such that:
- Left < Root < Right
- Efficient insert and search (O(log n) average)

## Operations
- `insert(item)`
- `search(item)`
- `inorder_traversal()`

## Example

```python
from data_structures.tree import BinarySearchTree

bst = BinarySearchTree()

- bst.insert(50)

- bst.insert(30)

- bst.insert(70)

- print(bst.search(30))  

- print(bst.inorder_traversal())  
