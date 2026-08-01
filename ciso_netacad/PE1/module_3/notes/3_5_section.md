# 3.5 Section Notes

## Sorting and Reversing Lists

This section explains how to change the order of items in a list using list methods.

Lists are ordered, so the sequence of items matters. Python gives you two common ways to rearrange that order:

- `sort()` arranges items in ascending order by default.
- `reverse()` flips the current order of the list.

Both methods change the original list directly.

## 1. Sorting a list with `sort()`

Use `sort()` when you want the items in a list ordered from smallest to largest, or alphabetically for text.

```python
numbers = [5, 3, 1, 2, 4]
print(numbers)

numbers.sort()
print(numbers)
```

Output:

```python
[5, 3, 1, 2, 4]
[1, 2, 3, 4, 5]
```

### Key idea

`sort()` does not create a new list. It updates the list you already have.

```python
letters = ["D", "F", "A", "Z"]
letters.sort()
print(letters)
```

Output:

```python
['A', 'D', 'F', 'Z']
```

## 2. Reversing a list with `reverse()`

Use `reverse()` when you want to keep the same items but read them in the opposite order.

```python
numbers = [5, 3, 1, 2, 4]
print(numbers)

numbers.reverse()
print(numbers)
```

Output:

```python
[5, 3, 1, 2, 4]
[4, 2, 1, 3, 5]
```

### Key idea

`reverse()` does not sort the list. It only flips the current order.

If a list is already sorted, reversing it gives you descending order. If it is not sorted, reversing it only changes the direction, not the ranking.

## 3. Working with numbers and strings

Lists can contain values stored in variables, not just literal values.

```python
a = 3
b = 1
c = 2

numbers = [a, c, b]
numbers.sort()
print(numbers)
```

Output:

```python
[1, 2, 3]
```

For strings, sorting follows alphabetical order.

```python
a = "A"
b = "B"
c = "C"
d = " "

letters = [a, b, c, d]
letters.reverse()
print(letters)
```

Output:

```python
[' ', 'C', 'B', 'A']
```

## 4. What to remember

- `sort()` changes the list order into sorted order.
- `reverse()` changes the list order into the opposite order.
- Both methods modify the original list.
- `sort()` is for ordering by value.
- `reverse()` is for flipping whatever order already exists.

## 5. Common mistake

A common mistake is expecting `reverse()` to sort the list backward.

```python
values = [5, 1, 4, 2, 3]
values.reverse()
print(values)
```

This does **not** produce sorted descending order. It only produces:

```python
[3, 2, 4, 1, 5]
```

If you want descending order, first sort the list, then reverse it.

```python
values = [5, 1, 4, 2, 3]
values.sort()
values.reverse()
print(values)
```

Output:

```python
[5, 4, 3, 2, 1]
```

## 6. Quick recap

Sorting changes the order based on value. Reversing changes the order based on position.

If you want to practice, try predicting the output before running each snippet:

```python
lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)
```

```python
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()
print(lst)
```

```python
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()
print(lst)
```
