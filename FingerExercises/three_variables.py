"""

Write a program that examines three variables - x, y and z - and prints 
the largest odd number among them. If none of them are odd, it should 
print a message to that effect.

"""

# Initialize variables
x = 3
y = 4
z = 1
largest = 0

# Branching logic to test for largest odd number
if (x % 2 or y % 2 or z % 2) != 0:
    if (x % 2 == 0 and y % 2 == 0):
        largest = z
    elif (x % 2 == 0 and z % 2 == 0):
        largest = y
    elif (y % 2 == 0 and z % 2 == 0):
        largest = x

    if (x % 2 != 0 and y % 2 != 0 and z % 2 != 0):
        if x > y and x > z:
            largest = x
        elif y > x and y > z:
            largest = y
        else:
            largest = z

    if (x % 2 != 0 and y % 2 != 0 and z % 2 == 0):
        if x > y:
            largest = x
        else:
            largest = y
    elif(x % 2 != 0 and y % 2 == 0 and z % 2 != 0):
        if x > z:
            largest = x
        else:
            largest = z
    elif(x % 2 == 0 and y % 2 != 0 and z % 2 != 0):
        if y > z:
            largest = y
        else:
            largest = z

    print(largest)
# Print message if all numbers even and nothing odd
else:
    print("All numbers are even!")
