"""
Finger excercise page 24 of textbook: Convert displayed comment in example code to
a while loop. 
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
index = numXs

while index > 0:
    toPrint = toPrint + 'X'
    index = index - 1

print(toPrint)
