# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen
# for i in range(1,11):
#     if i % 2 != 0:
#         print(i)


######################

# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x +=1

####################################

# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line.
# email = input("Enter your email address: ")
# for ch in email:
#     if ch == "@":
#         break
#     print(ch, end="")
# print()  # Move to the next line after printing the part before @

########################################
# Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen.
string_of_digits = input("Enter a string of digits: ")

for digit in string_of_digits:
    if digit == '0':
        print('x', end="")
        continue
    print(digit, end="") 
print()  # Move to the next line after printing the modified string