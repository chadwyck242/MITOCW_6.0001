#######################################################################################
# Finger exercise from page 42 of the textbook: Write a function isIn that accepts two
# strings as arguments and returns True if either string occurs anywhere in the other,
# and False otherwise. Hint: You might want to use the built-in str operation in
#######################################################################################


def isIn(string1, string2):
    if (string1 in string2) or (string2 in string1):
        return True
    else:
        return False


print(isIn('have', 'I have a pen'))
print(isIn('says', 'Cake is good'))
print(isIn('I have an apple', 'apple'))
