# Conditions and Conditional Execution in Python

## 1. What is a condition?

A condition is an expression that evaluates to either True or False. Conditions are used to make decisions in a program.

Examples:

- `5 > 3` → True
- `10 == 7` → False
- `age >= 18` → depends on the value of `age`

## 2. Why do we use conditions?

Conditions allow programs to run different code depending on the situation. This is called conditional execution.

Example:

- If a user is logged in, show the dashboard.
- If the password is wrong, show an error message.

## 3. The `if` statement

The `if` statement executes a block of code only when a condition is True.

```python
age = 20

if age >= 18:
    print("You are an adult")
```

### How it works

- Python checks the condition after `if`.
- If the condition is True, the indented code runs.
- If the condition is False, the code is skipped.

## 4. Indentation in Python

Python uses indentation to define blocks of code. The code inside an `if` statement must be indented.

```python
temperature = 30

if temperature > 25:
    print("It is hot")
    print("Drink water")
```

A common mistake is forgetting the indentation.

## 5. The `else` statement

The `else` statement provides an alternative block of code when the condition is False.

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

## 6. The `elif` statement

`elif` means “else if”. It allows you to check multiple conditions in order.

```python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

## 7. Comparison operators

These operators are commonly used in conditions:

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

Example:

```python
x = 10

print(x > 5)
print(x == 10)
print(x != 7)
```

## 8. Logical operators

You can combine conditions using logical operators:

- `and` → both conditions must be True
- `or` → at least one condition must be True
- `not` → reverses the condition

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter")
```

## 9. Nested conditions

A condition can contain another condition inside it.

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You may enter")
    else:
        print("You need a ticket")
```

## 10. Common examples of conditional execution

- Checking if a number is even or odd
- Validating user input
- Controlling program flow based on user choices
- Making decisions in games or calculators

Example:

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 11. Summary

Conditional execution helps a program make decisions. The main tools are:

- `if`
- `else`
- `elif`

These statements let your program respond differently depending on the values of variables and expressions.

## 12. 3.1.9 Pseudocode and introduction to loops

Sometimes a problem is too big to solve with many repeated `if` statements. For example, finding the largest number among 200 or 1000 values would be very long and repetitive.

In that case, we use an algorithm, which is a step-by-step solution to a problem. Before writing actual Python code, we can describe the solution in pseudocode.

### What is pseudocode?

Pseudocode is a simple, human-readable way to describe an algorithm. It is not real Python, so it cannot be executed directly.

Example:

```text
largest_number = -999999999

read a number

if number == -1:
    print largest_number
    stop

if number > largest_number:
    largest_number = number

repeat the process
```

### Why do we need loops?

A loop allows us to repeat a block of code as many times as needed. This is useful when we want to process many values without writing the same code again and again.

### Key idea

The program keeps reading numbers until the user enters `-1`, which tells the program that there are no more values.

### Example of the idea in Python

```python
largest_number = -999999999

number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number (-1 to stop): "))

print("The largest number is:", largest_number)
```

### Important note

This example introduces the idea of a loop using `while`. A loop repeats the code inside it until the condition becomes False.

### Extra information

Python also provides built-in functions such as `max()` and `min()` to find the largest and smallest values easily.

```python
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

largest_number = max(number1, number2, number3)
print("The largest number is:", largest_number)
```

### Summary

- Pseudocode helps us plan an algorithm before writing code.
- Loops let us repeat code without rewriting it.
- A loop is useful when processing many values or unknown amounts of input.
