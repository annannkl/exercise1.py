# Ask user for a number n and calculate n!
# n! is called n factorial. Formula: n! = 1 * 2 * 3 * ... * n.
# Also, 0! = 1 and 1! =1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
   
n = int(input("Please give a number: "))
counter = 0

print("The factorial is: ", factorial(n))