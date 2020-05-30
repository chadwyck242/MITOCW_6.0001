"""
  Finger exercise from page 27 of textbook: Write a program that asks the user to enter an integer and prints 
  two integers, root and pwr, such that 1 < pwr < 6 and root ** pwr is equal to the integer entered by
  the user. If no such pair of integers exists, it should print a message to that effect.
"""

x = int(input("Enter an integer: "))

root = 0
pwr = 2

while pwr < 6:
    while root**pwr < abs(x):
        root = root + 1
    if root**pwr == abs(x) and pwr % 2 != 0:
        if x < 0:
            root = -root
        print("The integer root and power of", x, "is", root, "and", pwr)
        break
    else:
        root = 1
        pwr = pwr + 1
else:
    print("No such root and power exist withing these constraints to give the integer", x)
