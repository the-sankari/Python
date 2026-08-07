# 4.2 Section 2 - How Functions Communicate with Their Environment

This section explains how functions receive information from the outside world. You will learn the difference between parameters and arguments, how positional and keyword passing work, and how default values make functions easier to use.

## 4.2.1 Parameters and arguments

A function can accept data through **parameters**. A parameter is a variable defined inside the function header, between the parentheses in the `def` statement.

An **argument** is the actual value you pass when you call the function.

```python
def message(number):
    print("Enter a number:", number)

message(1)
```

What happens here:

- `number` is the parameter
- `1` is the argument
- the value from the call is copied into the parameter

Important points:

- parameters exist only inside the function
- arguments exist outside the function and are passed in during the call
- the number of arguments should match the number of parameters

If you forget an argument, Python raises an error.

```python
def message(number):
    print("Enter a number:", number)

message()
```

This produces a `TypeError` because the function expects one value.

## Variables with the same name

It is possible to use the same name for a variable outside a function and a parameter inside a function.

```python
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)
```

The parameter inside the function does not replace the external variable. This is called **shadowing**.

## Multiple parameters

Functions can accept more than one parameter.

```python
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
```

The output depends on the values you pass in. More parameters give you more flexibility, but they also make the function harder to remember and use correctly.

## 4.2.2 Positional argument passing

With **positional arguments**, Python matches values by their position.

```python
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)
```

In this call:

- `1` goes to `a`
- `2` goes to `b`
- `3` goes to `c`

This is the most common and simplest way to call a function.

Example:

```python
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
```

Order matters here. If you swap the values, the meaning changes too.

## 4.2.3 Keyword argument passing

With **keyword arguments**, you name the target parameter explicitly.

```python
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")
```

Benefits of keyword arguments:

- the order does not matter
- the code is easier to read
- the call documents itself

Be careful to use the correct parameter name.

```python
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke")
```

This fails because `surname` is not a valid parameter name.

## 4.2.4 Mixing positional and keyword arguments

Python lets you combine both styles in one call, but there is one rule:

- positional arguments must come before keyword arguments

```python
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, c=1, b=2)
```

Here, `3` is matched positionally to `a`, while `c` and `b` are matched by name.

The following call is invalid because the value for `a` is provided twice:

```python
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, a=1, b=2)
```

## 4.2.5 Default parameter values

Sometimes a function should use a common value unless the caller chooses something else. In that case, you can give a parameter a **default value**.

```python
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
```

Now these calls are both valid:

```python
introduction("James", "Doe")
introduction("Henry")
```

If the caller does not supply `last_name`, Python uses the default value `"Smith"`.

You can also give defaults to both parameters:

```python
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()
introduction(last_name="Hopkins")
```

Default values make functions more convenient and reduce the amount of repeated code.

## Common mistakes to avoid

- forgetting to pass required arguments
- using the wrong keyword name
- placing a positional argument after a keyword argument
- giving the same parameter two values in one call

## Section summary

- Parameters are variables defined in a function header.
- Arguments are the values passed to a function when it is called.
- Positional arguments depend on order.
- Keyword arguments depend on name.
- You can mix both styles, but positional arguments must come first.
- Default values let a function work even when the caller omits some arguments.

## Quick self-check

Try to answer these without running the code first:

```python
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()
intro(b="Sean Connery")
```

```python
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")
```

```python
def add_numbers(a, b=2, c):
    print(a + b + c)
```

The last snippet is invalid because a non-default argument cannot follow a default argument.
