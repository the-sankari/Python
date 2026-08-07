#4.2.1 Parameterized functions
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)


#4.2.2 Positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

###################
# 4.2.3 Keyword argument passing

def introduction(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)
introduction("Skywalker", "Luke")
introduction(first_name="James", last_name="Bond")

# 4.2.4 Mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# 4.2.5 Parametrized functions – more details
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")

introduction("Henry")

introduction(first_name="William")


def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction()


