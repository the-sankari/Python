# 4.1 Section 1 - Functions

## What you should know

Functions let you package a repeated or complex piece of logic into a named block of code. That makes programs easier to read, easier to test, and easier to change later.

Use a function when:

- the same code appears in more than one place
- a task is too large to keep in one long block
- you want one place to update behavior later

## Where functions come from

Python functions can come from three main sources:

- built-in functions, such as `print()` and `input()`
- functions from modules that ship with Python
- functions you write yourself

## Defining a function

The basic syntax is:

```python
def function_name():
    function_body
```

Important rules:

- `def` starts the definition
- the function name follows the same rules as variable names
- parentheses hold parameters, if there are any
- the line ends with a colon
- the indented block below is the function body

Example:

```python
def message():
    print("Enter a value:")
```

## Calling a function

Defining a function does not run it. You must call it explicitly.

```python
def message():
    print("Enter a value:")

print("We start here.")
message()
print("We end here.")
```

Output:

```text
We start here.
Enter a value:
We end here.
```

## How execution works

When Python reaches a function call, it jumps into the function, runs its body, and then returns to the line after the call.

## Common rules to remember

- A function must be defined before it is called.
- A function name and a variable name cannot be the same.
- A function can appear anywhere in the file, as long as it is defined before the call happens.

Example of a wrong order:

```python
print("We start here.")
message()
print("We end here.")


def message():
    print("Enter a value:")
```

This raises a `NameError` because Python has not seen `message()` yet.

## Why functions help

Functions reduce duplication and make updates cheaper. If you need to change the prompt message, you only change it in one place.

```python
def message():
    print("Enter a value:")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
```

## Section summary

- A function is a reusable block of code that performs a specific task.
- Functions improve reuse, organization, readability, and maintainability.
- You create a function with `def` and call it by writing its name followed by parentheses.
- Python includes built-in functions, module functions, user-defined functions, and lambda functions.
- More advanced functions with parameters are covered next.
