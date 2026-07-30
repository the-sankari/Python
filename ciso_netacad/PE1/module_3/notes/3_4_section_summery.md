# 3.4.12 Section Summary

This section introduces lists in Python.
A list is a way to store many values in one variable.
It is useful when you want to keep related items together.

1. What is a list?

A list is written inside square brackets [] and items are separated by commas.

```python
fruits = ["apple", "banana", "mango"]
print(fruits)
```

A list can contain numbers, strings, booleans, and even other lists.

```python
mixed = [1, "hello", True]
print(mixed)
```

2. Accessing items in a list

Each item in a list has an index.
Python starts counting from 0.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # mango
```

The index 0 means the first item, and -1 means the last item.

3. Changing items in a list

Lists are mutable, which means you can change them.

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)
```

Now the list becomes:

```python
["apple", "orange", "mango"]
```

4. Adding items to a list

You can add items to the end of a list using append().

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
```

You can also insert an item at a specific position using insert().

```python
fruits.insert(0, "grape")
print(fruits)
```

5. Removing items from a list

You can delete an item by its index.

```python
fruits = ["apple", "banana", "mango"]
del fruits[1]
print(fruits)
```

You can also delete the whole list.

```python
del fruits
```

6. Lists inside lists

A list can contain another list. This is called a nested list.

```python
nested = [1, "a", ["x", "y", "z"]]
print(nested[2])
```

7. Looping through a list

You can go through each item in a list using a for loop.

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

8. Checking the length of a list

Use len() to find how many items are in a list.

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))  # 3
```

9. Functions and methods

A function is called like this:

```python
len(fruits)
```

A method is called using a dot after the object:

```python
fruits.append("mango")
```

10. Important idea

A list helps you store many values in one place.
You can access, change, add, remove, and repeat through its items.

11. Quick practice

```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
```

Try changing the code and see what happens.

3.4.13 Section Quiz

1. What is the output of this code?

```python
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)
```

2. What is the output of this code?

```python
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
```

3. What happens if you run this code?

```python
lst = []
del lst
print(lst)
```

4. What is the output of this code?

```python
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
```
