# Section 3: Python Operators & Data Manipulation Tools

## What Are Operators?

**Operators** are special symbols that perform operations on values (operands). They allow you to manipulate data, perform calculations, and create logical conditions.

---

## 1. Arithmetic Operators

Perform mathematical calculations on numeric values.

| Operator | Name                | Example   | Result |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `5 + 3`   | `8`    |
| `-`      | Subtraction         | `5 - 3`   | `2`    |
| `*`      | Multiplication      | `5 * 3`   | `15`   |
| `/`      | Division            | `10 / 2`  | `5.0`  |
| `//`     | Floor Division      | `10 // 3` | `3`    |
| `%`      | Modulus (Remainder) | `10 % 3`  | `1`    |
| `**`     | Exponentiation      | `2 ** 3`  | `8`    |

### Examples

```python
# Basic arithmetic
x = 10
y = 3

print(x + y)    # 13
print(x - y)    # 7
print(x * y)    # 30
print(x / y)    # 3.333...
print(x // y)   # 3 (floor division)
print(x % y)    # 1 (remainder)
print(x ** y)   # 1000 (10 to the power of 3)
```

---

## 2. Assignment Operators

Assign values to variables, with optional operations.

| Operator | Example   | Equivalent   |
| -------- | --------- | ------------ |
| `=`      | `x = 5`   | `x = 5`      |
| `+=`     | `x += 3`  | `x = x + 3`  |
| `-=`     | `x -= 3`  | `x = x - 3`  |
| `*=`     | `x *= 3`  | `x = x * 3`  |
| `/=`     | `x /= 3`  | `x = x / 3`  |
| `//=`    | `x //= 3` | `x = x // 3` |
| `%=`     | `x %= 3`  | `x = x % 3`  |
| `**=`    | `x **= 3` | `x = x ** 3` |

### Examples

```python
x = 10
x += 5      # x = 15
x -= 3      # x = 12
x *= 2      # x = 24
x /= 4      # x = 6.0
x //= 2     # x = 3.0
x %= 2      # x = 1.0
```

---

## 3. Comparison (Relational) Operators

Compare two values and return `True` or `False`.

| Operator | Name                  | Example  | Result  |
| -------- | --------------------- | -------- | ------- |
| `==`     | Equal                 | `5 == 5` | `True`  |
| `!=`     | Not Equal             | `5 != 3` | `True`  |
| `>`      | Greater Than          | `5 > 3`  | `True`  |
| `<`      | Less Than             | `5 < 3`  | `False` |
| `>=`     | Greater Than or Equal | `5 >= 5` | `True`  |
| `<=`     | Less Than or Equal    | `5 <= 3` | `False` |

### Examples

```python
a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False
```

---

## 4. Logical Operators

Combine boolean values and return boolean results.

| Operator | Meaning                   | Example          | Result  |
| -------- | ------------------------- | ---------------- | ------- |
| `and`    | Both must be True         | `True and False` | `False` |
| `or`     | At least one must be True | `True or False`  | `True`  |
| `not`    | Negates the value         | `not True`       | `False` |

### Examples

```python
x = 10
y = 5

# and operator
print(x > y and x > 0)      # True (both conditions true)
print(x > y and x < 0)      # False (second condition false)

# or operator
print(x > y or x < 0)       # True (first condition true)
print(x < y or x < 0)       # False (both conditions false)

# not operator
print(not x > y)            # False (negates True)
print(not x < y)            # True (negates False)
```

---

## 5. Membership Operators

Check if a value exists in a sequence (list, string, tuple, etc.).

| Operator | Meaning                          | Example                    |
| -------- | -------------------------------- | -------------------------- |
| `in`     | Value exists in sequence         | `'a' in 'apple'` → `True`  |
| `not in` | Value does not exist in sequence | `'z' in 'apple'` → `False` |

### Examples

```python
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)        # True
print('grape' in fruits)        # False
print('apple' not in fruits)    # False
print('grape' not in fruits)    # True

# With strings
text = "Python"
print('P' in text)              # True
print('x' not in text)          # True
```

---

## 6. Identity Operators

Check if two variables refer to the same object in memory.

| Operator | Meaning                   | Example      |
| -------- | ------------------------- | ------------ |
| `is`     | Objects are identical     | `x is y`     |
| `is not` | Objects are not identical | `x is not y` |

### Examples

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True (same content)
print(a is b)       # False (different objects)
print(a is c)       # True (same object)

# With None
x = None
print(x is None)    # True
print(x is not None) # False
```

---

## 7. Bitwise Operators

Perform operations on binary representations of integers.

| Operator | Name        | Example         |
| -------- | ----------- | --------------- |
| `&`      | AND         | `5 & 3` = `1`   |
| `\|`     | OR          | `5 \| 3` = `7`  |
| `^`      | XOR         | `5 ^ 3` = `6`   |
| `~`      | NOT         | `~5` = `-6`     |
| `<<`     | Left Shift  | `5 << 1` = `10` |
| `>>`     | Right Shift | `5 >> 1` = `2`  |

### Examples

```python
a = 5    # binary: 0101
b = 3    # binary: 0011

print(a & b)    # 1 (0001)
print(a | b)    # 7 (0111)
print(a ^ b)    # 6 (0110)
print(~a)       # -6
print(a << 1)   # 10 (shift left)
print(a >> 1)   # 2 (shift right)
```

---

## 8. Operator Precedence

Order in which Python evaluates operators (highest to lowest):

1. `**` - Exponentiation
2. `~`, `+x`, `-x` - Unary operations
3. `*`, `/`, `//`, `%` - Multiplication, Division
4. `+`, `-` - Addition, Subtraction
5. `<<`, `>>` - Bitwise shifts
6. `&` - Bitwise AND
7. `^` - Bitwise XOR
8. `|` - Bitwise OR
9. `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `is`, `is not` - Comparisons
10. `not` - Logical NOT
11. `and` - Logical AND
12. `or` - Logical OR

### Examples

```python
# Precedence matters
print(2 + 3 * 4)        # 14 (multiplication first)
print((2 + 3) * 4)      # 20 (parentheses override)

print(10 - 5 + 2)       # 7 (left to right)
print(2 ** 3 ** 2)      # 512 (right to left for exponentiation)

# Complex expression
result = 2 + 3 * 4 / 2 - 1 ** 3
print(result)           # 7.0
```

---

## 9. String Operators

Special operators for working with strings.

### Concatenation (`+`)

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)           # Hello World
```

### Repetition (`*`)

```python
text = "Ha"
print(text * 3)         # HaHaHa
print("=" * 10)         # ==========
```

### Membership (`in`)

```python
text = "Python"
print("P" in text)      # True
print("x" not in text)  # True
```

---

## 10. Summary

| Category       | Purpose                      | Operators                           |
| -------------- | ---------------------------- | ----------------------------------- |
| **Arithmetic** | Mathematical operations      | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **Assignment** | Assign and modify variables  | `=`, `+=`, `-=`, `*=`, `/=`, etc.   |
| **Comparison** | Compare values               | `==`, `!=`, `>`, `<`, `>=`, `<=`    |
| **Logical**    | Boolean logic                | `and`, `or`, `not`                  |
| **Membership** | Check existence in sequences | `in`, `not in`                      |
| **Identity**   | Check object identity        | `is`, `is not`                      |
| **Bitwise**    | Binary operations            | `&`, `\|`, `^`, `~`, `<<`, `>>`     |
| **String**     | String manipulation          | `+`, `*`, `in`                      |

---

## 2.3.4 SECTION SUMMARY

**Key takeaways (in brief):**

- An _expression_ combines values, variables, operators or function calls and evaluates to a single result (for example, `1 + 2`).
- _Operators_ are symbols or keywords that perform actions on operands — for example `*` multiplies two values (`x * y`).
- Python arithmetic operators include `+`, `-`, `*`, `/` (always returns a float), `%` (remainder), `**` (power), and `//` (floor division).
- A _unary_ operator works on a single operand (e.g., `-1`), while a _binary_ operator requires two operands (e.g., `4 + 5`).
- Operators follow a precedence order: `**` (highest), then unary `+`/`-`, then `*`, `/`, `%`, and finally binary `+` and `-` (lowest among the arithmetic ones).
- Parentheses override the normal precedence: expressions inside `()` are evaluated first.
- Exponentiation binds from the right, so `2 ** 2 ** 3` is evaluated as `2 ** (2 ** 3)`.

Keep these points in mind when writing expressions so results are predictable and clear.
