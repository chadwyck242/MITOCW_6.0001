"""
Finger exercise from page 30 of text: Let s be a string that contains a
sequence of decimal numbers separated by commas, 
e.g., s = '1.23, 2.4, 3.123'. Write a program that prints the sum 
of the numbers in s.
"""

s = '1.23,2.4,3.123,100.67, 332.89'
numList = []

# split the string at the comma and append to list
for item in s.split(","):
    numList.append(item)


sum = 0
# sum each item in list, casting the strings to floats
for num in numList:
    sum += float(num)

print(sum)
