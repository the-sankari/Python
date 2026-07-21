# Section 2: Python Literals

## What Are Literals?

**Literals** are fixed values written directly in your code. They represent specific data that doesn't change. Python supports various types of literals:

- **Numeric literals**: e.g., `123`, `3.14`
- **String literals**: e.g., `"Hello"`, `'World'`
- **Boolean literals**: e.g., `True`, `False`

---

## Number Systems

### Binary System

- Base: 2
- Uses: 0s and 1s only
- Example: `1010` (binary) = `10` (decimal)

### Octal System

- Base: 8
- Uses: digits 0-7

### Hexadecimal System

- Base: 16
- Uses: digits 0-9 and letters A-F

---

## Numeric Types in Python

### Integers (int)

- Numbers **without** a fractional component
- Can be positive or negative
- Examples: `256`, `-1`, `0`

### Floating-Point Numbers (float)

- Numbers **with** a fractional component
- Examples: `1.27`, `3.14`, `-0.5`

---

## String Escape Characters

To include special characters inside strings, use the **escape character** `\` or choose appropriate quote types:

### Using Escape Characters

```python
'I\'m happy.'           # Escaping apostrophe
"He said \"Python\""    # Escaping double quotes
```

### Using Opposite Quote Types

```python
"I'm happy."                          # Double quotes for apostrophe
'He said "Python", not "typhoon"'     # Single quotes for double quotes
```

---

## Boolean Values

Boolean values represent truth values:

- `True` - represents 1 in numeric context
- `False` - represents 0 in numeric context

Used for logical operations and conditions.

---

## Special Literal: None

- **None** is a special literal in Python
- Type: `NoneType`
- Represents the **absence of a value**
- Commonly used as a default or placeholder value
