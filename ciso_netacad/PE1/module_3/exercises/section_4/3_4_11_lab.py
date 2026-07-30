
# 3.4.11   LAB   The basics of lists ‒ the Beatles
# Scenario
# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatles = []  # Step 1: create an empty list named beatles.
print("Step 1:", beatles)  # Printing the empty list.
beatles.append("John Lennon")  # Step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison.
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)  # Printing the list after adding the first three
# members of the band.
for i in range(2):  # Step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best.
    member = input("Enter a member of the band: ")
    beatles.append(member)
print("Step 3:", beatles)  # Printing the list after adding the last two
# members of the band.
del beatles[3:5]  # Step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list.
print("Step 4:", beatles)   

beatles.insert(0, "Ringo Starr")  # Step 5: use the insert() method to add Ringo Starr to the beginning of the list.
print("Step 5:", beatles)  # Printing the final list of members of theq

# testing the final list of members of the band.
print("\nFinal list of members of the band:", beatles)  # Printing the final list of members of the band.