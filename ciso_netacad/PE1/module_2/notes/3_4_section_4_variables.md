# Variables in Python

## Overview

A variable is a name that refers to a value (an object) in memory. In Python, variables are _labels_ pointing to objects — values themselves have types, not variable names.

## Naming rules and conventions

- Must start with a letter (A-Z, a-z) or underscore (`_`), followed by letters, digits, or underscores.
- Case-sensitive: `count`, `Count`, and `COUNT` are different names.
- Avoid reserved keywords (e.g., `def`, `class`, `if`).
- Conventions:
  - `snake_case` for variables and functions.
  - Use descriptive names: `total_price` is better than `tp`.
  - Constants: use `UPPER_SNAKE_CASE` by convention (Python does not enforce immutability).

## Assignment

Use the single equals sign `=` to assign a value to a name.

Example:

```python
count = 10            # integer assigned to name 'count'
name = "Alice"       # string assigned to name 'name'
pi = 3.14159          # float assigned to name 'pi'
```

Multiple assignment and unpacking:

```python
x, y, z = 1, 2, 3
a = b = 0             # chain assignment: both a and b refer to 0

# swapping values (no temporary variable needed)
x, y = y, x
```

## Dynamic typing (type flexibility)

Python variables can be rebound to objects of different types at runtime:

```python
var = 5        # var refers to an int
var = "now a string"  # var now refers to a str
```

Types are properties of objects, not of variable names.

## Mutability vs. immutability

- Immutable types: `int`, `float`, `str`, `tuple`, `frozenset` — assignments create new objects when values change.
- Mutable types: `list`, `dict`, `set`, `bytearray` — objects can be changed in place.

Example showing mutability:

```python
lst = [1, 2, 3]
lst.append(4)   # modifies the same list object

name = "Bob"
name = name.upper()  # returns a new string; original string is unchanged
```

## Scope: local, global, and nonlocal

- Local variables: defined inside a function, visible only there.
- Global variables: defined at module level; accessible across functions in that module.
- `global` keyword: declare inside a function to assign to module-level names.
- `nonlocal` keyword: used inside nested functions to assign to a variable in an enclosing (non-global) scope.

Example:

```python
g = 0

def outer():
	x = 1
	def inner():
		nonlocal x
		x += 1
	inner()
	return x

def inc_global():
	global g
	g += 1
```

## Best practices and tips

- Prefer clear, descriptive names.
- Keep variable scopes as small as possible.
- Use constants (`UPPER_SNAKE_CASE`) to signal values that shouldn't change.
- Avoid reusing variable names in nested scopes to prevent confusion.
- When working with mutable defaults in functions, use `None` sentinel to avoid shared-state bugs:

```python
def append_item(item, lst=None):
	if lst is None:
		lst = []
	lst.append(item)
	return lst
```

## Useful examples

- Read input and store in variable:

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old")
```

- Count occurrences using a dictionary:

```python
words = ['apple', 'banana', 'apple']
counts = {}
for w in words:
	counts[w] = counts.get(w, 0) + 1
```

## Important quotes

- "Readability counts." — The Zen of Python (import this)
- "There should be one-- and preferably only one --obvious way to do it." — The Zen of Python
- "In Python, everything is an object." — core Python principle: names reference objects
- "Names in Python are simply labels pointing to objects; the type belongs to the object, not the name." — paraphrase of Python docs

## Quick reference

- Assign: `name = value`
- Multiple assign: `a, b = 1, 2`
- Swap: `a, b = b, a`
- Constant convention: `MAX_SIZE = 100`

---

End of notes: these examples illustrate common variable uses, pitfalls, and conventions in Python.
