# Create a list and fill with 100 random numbers in the range 1-50.
# Ask user for a number and find how many times the numbers is found in the list.
# If not found, display appropriate message.

import random

list = []
for i in range(1,101):
    list.append(random.randint(1,50))
print(list)

n = int(input("Please enter a number here: "))

for i in list:
        if n == i:
            counts = list.count(i)
print(counts)

while False:
    for e in i:
        if i != e:
            print("Not in the list.")