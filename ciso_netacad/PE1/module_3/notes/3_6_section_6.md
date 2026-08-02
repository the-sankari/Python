# 3.6.7 Section Summary: Working with Lists

## Introduction

Lists are one of the most useful data types in Python. They allow you to store many values in one place and work with them in an organized way. In this section, you will learn how to copy lists, slice them, remove parts of them, and check whether items are present.

## 1. Understanding list assignment

When you write:

```python
vehicles_one = ['car', 'bicycle', 'motor']
vehicles_two = vehicles_one
```

both variables point to the same list in memory. This means that changing one list also changes the other.

```python
vehicles_one = ['car', 'bicycle', 'motor']
vehicles_two = vehicles_one

del vehicles_one[0]
print(vehicles_two)  # outputs: ['bicycle', 'motor']
```

### Key idea

- `=` does not create a new list.
- It creates another name for the same list.

## 2. Creating a copy of a list

If you want a true copy, use slicing.

```python
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]      # copy the entire list
copy_part_colors = colors[0:2]     # copy part of the list
```

### Why this matters

A copied list is independent from the original. Changing one will not affect the other.

## 3. Using negative indices in slices

You can also use negative numbers to count from the end of the list.

```python
sample_list = ['A', 'B', 'C', 'D', 'E']
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
```

## 4. Slice syntax made simple

The basic format is:

```python
list[start:end]
```

You may omit one or both values:

```python
my_list = [1, 2, 3, 4, 5]

slice_one = my_list[2:]     # from index 2 to the end
slice_two = my_list[:2]     # from the beginning up to index 2
slice_three = my_list[-2:]  # last two items

print(slice_one)   # outputs: [3, 4, 5]
print(slice_two)   # outputs: [1, 2]
print(slice_three) # outputs: [4, 5]
```

## 5. Deleting slices from a list

You can remove a section of a list using `del`.

```python
my_list = [1, 2, 3, 4, 5]

del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # outputs: []
```

## 6. Checking membership with `in` and `not in`

These operators help you test whether an item exists in a list.

```python
my_list = ['A', 'B', 1, 2]

print('A' in my_list)      # outputs: True
print('C' not in my_list)  # outputs: True
print(2 not in my_list)    # outputs: False
```

### Beginner tip

- Use `in` when you want to check if something exists.
- Use `not in` when you want to check if something does not exist.

## Quick summary

- `=` creates another reference to the same list.
- `[:]` creates a copy of a list.
- Slicing helps you access or remove part of a list.
- `in` and `not in` check membership.

---

# 3.6.8 Section Quiz

Try to answer these questions on your own before checking the solutions.

## Question 1

What is the output of the following code?

```python
list_1 = ['A', 'B', 'C']
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)
```

## Question 2

What is the output of the following code?

```python
list_1 = ['A', 'B', 'C']
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
```

## Question 3

What is the output of the following code?

```python
list_1 = ['A', 'B', 'C']
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
```

## Question 4

What is the output of the following code?

```python
list_1 = ['A', 'B', 'C']
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
```

## Question 5

Replace `???` with the correct operator so that the code produces the expected result.

```python
my_list = [1, 2, 'in', True, 'ABC']

print(1 ??? my_list)   # outputs True
print('A' ??? my_list) # outputs True
print(3 ??? my_list)   # outputs True
print(False ??? my_list)  # outputs False
```
