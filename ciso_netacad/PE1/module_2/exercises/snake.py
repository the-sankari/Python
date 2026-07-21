## print("Tell me something!")
"""anything = input("Tell me something: ")
print("Hmm...", anything, "... Really?")

num = input("Give me a number: ")
modesone = int(num) % 2
print("You entered:", num)
print("The remainder when divided by 2 is:", modesone)
"""
"""
2.6.9   LAB   Simple input and output
Scenario
Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.

The results have to be printed to the console.

You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.

Test your code ‒ does it produce the results you expect?

We won't show you any test data ‒ that would be too simple.
"""
"""
# input a float value for variable a here
a = float(input("Enter the first number: "))
# input a float value for variable b here
b = float(input("Enter the second number: "))

# output the result of addition here
print("Addition:", a + b)

# output the result of subtraction here
print("Subtraction:", a - b)

# output the result of multiplication here
print("Multiplication:", a * b)
# output the result of division here
print("Division:", a / b)

print("\nThat's all, folks!")
"""

"""

2.6.10   LAB   Operators and expressions
Scenario
Your task is to complete the code in order to evaluate the following expression:

Math expression
The result should be assigned to y. Be careful ‒ watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.


Test Data
Sample input:

1
Expected output:

Output
y = 0.6000000000000001
Sample input:

10
Expected output:

Output
y = 0.09901951266867294
Sample input:

100
Expected output:

Output
y = 0.009999000199950014
Sample input:

-5
Expected output:

Output
y = -0.19258202567760344
"""
"""
x = float(input("Enter value for x: "))

# Write your code here.
y = 1/(x+(1/(x+(1/(x+(1/x))))))

print("y =", y)

"""
"""

2.6.11   LAB   Operators and expressions – 2
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.


Test Data
Sample input:

12
17
59
Expected output:

Output
13:16
Sample input:

23
58
642
Expected output:

Output
10:40
Sample input:

0
1
2939
Expected output:

Output
1:0
"""

"""
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

total_mins = hour * 60 + mins + dura    
end_hour = (total_mins // 60) % 24
end_mins = total_mins % 60
print(end_hour, ":", end_mins, sep="")
"""

# x = int(input())
# y = int(input())

# x = x / y
# y = y / x

# print(y)
x = int(input())
y = int(input())

print(x + y)



x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)



z = y = x = 1
print(z, y, x)
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

x = int(input())
y = int(input())

print(x + y)

x = input()
y = int(input())

print(x * y)

