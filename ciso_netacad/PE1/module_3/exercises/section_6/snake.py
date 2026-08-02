list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# new_list = my_list[1:-1]
# new_list = my_list[-1:1]
# new_list = my_list[3:]
new_list = my_list[:]
print(my_list)
print(new_list)


print(5 in my_list)
print(5 not in my_list)
print(10 in my_list)


##################################

checklist = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = checklist[0]
for i in range(1, len(checklist)):
    if checklist[i] > largest:
        largest = checklist[i]
print("The largest number in the checklist is:", largest)
largest = checklist[0]
for i in checklist:
    if i > largest:
        largest = i
print("The largest number in the checklist is:", largest)

for i in checklist[1:]:
    if i > largest:
        largest = i
print("The largest number in the checklist is:", largest)
