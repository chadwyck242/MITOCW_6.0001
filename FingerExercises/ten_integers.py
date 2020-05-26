"""
Finger exercise from page 24 of textbook: Ask user to input 10 integers, and then print the largest odd integer entered. 
If no odd integers were entered, print a message to that effect.
"""
# Initialize the variables
index = 0
oddCount = 0
evenCount = 0
largestOdd = 1

# Start while loop asking for next integer to test
while index < 10:
    nextInt = int(input('Enter an integer '))
    if nextInt % 2 != 0:
        if nextInt > largestOdd:
            largestOdd = nextInt
            oddCount = oddCount + 1
    else:
        evenCount = evenCount + 1
    # test if all numbers were even and print that message
    # otherwise print the largest odd once input is complete
    if evenCount == 10 and oddCount == 0:
        print("No odd numbers were entered at all")
        break
    elif index == 9:
        print(largestOdd)
    # Increment index
    index = index + 1
