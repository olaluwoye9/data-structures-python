
---

## 📄 `array.md`

```markdown
# Array

The `Array` class mimics a dynamic list with operations for insertion, deletion, access, and search.

## Features
- `insert(item)`
- `insert_at(index, item)`
- `delete(item)`
- `delete_at(index)`
- `update(index, item)`
- `access(index)`
- `search(item)`
- `get_length()`
- `display()`

## Example

```python
from data_structures.array import Array

arr = Array()
arr.insert(5)
arr.insert(10)
arr.insert_at(1, 7)
arr.update(2, 20)
arr.display()
