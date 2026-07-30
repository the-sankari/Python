# i = 1
# j = not not i

# print(j)
# print(type(j))

# i = 15
# j = 22

# print("Bitwise AND:", i & j)
# print("Bitwise OR:", i | j)
# print("Bitwise XOR:", i ^ j)
# print("Bits: ", bin(i), "and", bin(j))
# print("Bitwise image of", i, "and", j, "is", bin(i & j)
#       )
# log = i and j
# print("Logical AND:", log)

# logneg = not i
# print("Logical NOT:", logneg)

# bitneg = ~i
# print("Bitwise NOT:", bitneg)


##############
# Dealing with single bits
flag_register = 0x1234
print("Flag register:", bin(flag_register))

# bit mask

the_mask = 8
if flag_register & the_mask:
    print("The bit is set")
else:
    print("The bit is not set")

flag_register = flag_register & ~the_mask
flag_register &= ~the_mask
print("Flag register after clearing the bit:", bin(flag_register))

###################################
# shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).

# Binary shifting
number = 0b00001111
print("Original number:", bin(number))
number = number << 2
print("After left shift by 2:", bin(number))
number = number >> 3
print("After right shift by 3:", bin(number))

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
