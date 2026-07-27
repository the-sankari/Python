# Variables in Python — an advanced, research-grade overview

## Abstract

This note elevates the practical introduction of Python variables into a concise, research‑grade discussion suitable for advanced students and practitioners. It covers the name→object model, identity vs. equality, assignment semantics, mutability and copying, scoping & namespaces, lifetime and memory considerations, and pragmatic conventions for maintainable, high‑performance code.

## Core concept: names, objects, and identity

- Names are labels bound to objects; objects carry type, value, and identity.
- Use `is` to compare identity (`id(obj)`), and `==` to compare value/equality.
- Small integers and short strings may be interned or cached by the interpreter — this is an implementation detail (CPython) and should not be relied upon for program logic.

Example:

```python
a = 256
b = 256
print(a is b)      # often True in CPython for small ints

c = 1000
d = 1000
print(c is d)      # often False; do not rely on identity for semantics
```

## Assignment model (what happens on `=`)

- Assignment binds a name to an object; it does not copy the object.
- Rebinding a name simply changes which object the name refers to; other names pointing to the previous object are unaffected.
- Multiple assignment unpacks tuples/iterables; chained assignment creates multiple names referencing the same object.

```python
x = [1, 2]
y = x         # y references the same list object
x.append(3)
print(y)      # [1, 2, 3]

a = b = []    # a and b reference the same list
a.append(1)
print(b)      # [1]
```

## Mutability, copying, and defensive patterns

- Mutability determines whether operations modify an object in place (mutable) or produce new objects (immutable).
- For complex data, prefer explicit copying when you need independent replicas. Understand shallow vs deep copy semantics:

```python
import copy

orig = [[1], [2]]
sh = copy.copy(orig)       # shallow copy; inner lists are shared
dp = copy.deepcopy(orig)   # deep copy; everything duplicated

orig[0].append(99)
print(sh)  # inner mutation visible
print(dp)  # unaffected
```

- For APIs, avoid mutable default arguments; use `None` sentinel (see below).

## Scope, namespaces, and closures

- Python has multiple namespaces: local (function), enclosing (lexical), global (module), and builtins. The LEGB rule describes lookup order.
- Use `global` only for module-level mutation; prefer returning values or using explicit containers/objects for shared state.
- Use `nonlocal` to modify variables in an enclosing function scope when writing closures.

Example (closure with `nonlocal`):

```python
def counter(start=0):
	count = start
	def inc():
		nonlocal count
		count += 1
		return count
	return inc

c = counter(10)
print(c())  # 11
```

## Lifetime and garbage collection

- Objects are reference-counted (CPython) and supplemented by a cyclic GC for objects involved in reference cycles.
- Long‑lived references create memory pressure; break large cycles or use weak references (`weakref`) for caches.

## Type annotations and static reasoning

- Use type hints (`PEP 484`) to document and enable static analysis with `mypy`, `pyright`, or IDEs. Type hints are optional at runtime but valuable for large codebases and research reproducibility.

```python
from typing import List, Dict

def mean(values: List[float]) -> float:
	return sum(values) / len(values)
```

- Consider `typing.Final` for constants that should not be re-assigned, and `typing.TypedDict` or `dataclasses` for structured records.

## Immutability as a design choice

- Favor immutable data structures for concurrency and reasoning about state. Use `tuple`, `frozenset`, or frozen `dataclasses` where appropriate.
- When mutation is required for performance, encapsulate it and clearly document invariants.

## Performance considerations

- Attribute and global lookups are slower than local variable accesses — cache frequently used globals into locals inside hot loops.
- Avoid unnecessary object allocation in tight loops; prefer in-place operations for large numeric arrays (use NumPy for numerical work).

Example (micro-optimization):

```python
# slower
for _ in range(n):
	value = globals()['X']

# faster
X_local = X
for _ in range(n):
	value = X_local
```

## Common pitfalls and how to avoid them

- Mutable default argument:

```python
def bad_append(x, lst=[]):
	lst.append(x)
	return lst

def good_append(x, lst=None):
	if lst is None:
		lst = []
	lst.append(x)
	return lst
```

- Accidentally sharing state via class attributes vs instance attributes — initialize per-instance state in `__init__`.

## Practical examples (deepened)

- Counting with `collections.Counter`:

```python
from collections import Counter
words = ['apple', 'banana', 'apple']
counts = Counter(words)
```

- Defensive API pattern with immutability and explicit copy:

```python
from copy import deepcopy

def process(data):
	data = deepcopy(data)  # break caller-owned references
	# mutate data safely
	return data
```

## Style and conventions (senior-level)

- Use `snake_case` for variables and functions, `UpperCamelCase` for classes, and `UPPER_SNAKE_CASE` for constants.
- Choose semantic names that express units and invariants (e.g., `price_usd`, `timestamp_utc`).
- In research code, add docstrings and type annotations for reproducibility and provenance.

## References and further reading

- Python Language Reference — Names and binding model
- PEP 8 — Style Guide for Python Code
- PEP 484 — Type Hints
- Articles on CPython object model and memory internals (for implementation details)

---

End of upgraded notes: this version focuses on conceptual clarity, practical defensive patterns, and considerations important for advanced development and research-quality code.
lid
