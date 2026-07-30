3.3 Section 3 – Logic and bit operations in Python

3.3.7 Section Summary

This section teaches two important ideas:

1. How to use logical operators to make decisions.
2. How to use bitwise operators to work with numbers at the bit level.

3. Logical operators

Logical operators help us decide whether a condition is true or false.

Common logical operators:

- and: returns True only if both conditions are True.
  - Example: `True and False` → `False`
  - Example: `10 > 5 and 3 < 4` → `True`

- or: returns True if at least one condition is True.
  - Example: `True or False` → `True`
  - Example: `5 > 10 or 2 < 3` → `True`

- not: reverses the result.
  - Example: `not True` → `False`
  - Example: `not (5 > 3)` → `False`

Simple example:

```python
is_student = True
age = 20

print(age > 18 and is_student)  # True
print(age > 18 or is_student)   # True
print(not is_student)          # False
```

2. Bitwise operators

Bitwise operators work with the binary form of numbers. They check or change individual bits.

Let us use these values:

- `x = 15` → binary `0000 1111`
- `y = 16` → binary `0001 0000`

Now let us look at the main bitwise operators:

- `&` (AND): keeps a bit only if it is 1 in both numbers.
  - Example: `x & y` → `0`
  - Binary: `0000 0000`

- `|` (OR): keeps a bit if it is 1 in at least one number.
  - Example: `x | y` → `31`
  - Binary: `0001 1111`

- `~` (NOT): flips the bits.
  - Example: `~x` → `-16`
  - This may look unusual because Python uses a special way to represent negative numbers.

- `^` (XOR): keeps a bit if it is different in the two numbers.
  - Example: `x ^ y` → `31`
  - Binary: `0001 1111`

- `>>` (right shift): moves bits to the right.
  - Example: `y >> 1` → `8`
  - Binary: `0000 1000`

- `<<` (left shift): moves bits to the left.
  - Example: `y << 3` → `128`
  - Binary: `1000 0000`

3. Why this is useful

Logical operators are used in conditions like `if` statements.
Bitwise operators are useful in low-level programming, binary data, and some advanced coding tasks.

4. Quick summary

- `and` needs both conditions to be True.
- `or` needs only one condition to be True.
- `not` reverses the result.
- Bitwise operators work directly with binary bits.

If you want, I can also turn this into a shorter classroom-style note or add more simple examples in Arabic or Sinhala.
