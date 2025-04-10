
---

## 📄 `graph.md`

```markdown
# Graph

The `Graph` class uses an **adjacency list** to represent connections.

## Features
- Add node
- Add edge
- Display neighbors

## Example

```python
from data_structures.graph import Graph

g = Graph()
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B")
print(g.graph)
