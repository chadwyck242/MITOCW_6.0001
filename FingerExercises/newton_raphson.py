####################################################
# Finger exercise from page 38 of the textbook:
# Add some code to the implementation of
# Newton-Raphson that keeps track of the number
# of iterations used to find the root. Use that
# code as a part of a program that compares the
# efficiency of Newton-Raphson and bisection
# search. (You should discover that Newton-Raphson
# is more efficient).
####################################################

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k/2.0
nr_iterations = 0
while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
    nr_iterations += 1
print('Square root of', k, 'is about', guess)
print('Iterations of Newton-Raphson to find square root:', nr_iterations)

print('')
print('########################################################')
print('')

# Using bisection search to find square root of 24
x = 24
bi_epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= bi_epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(ans, 'is close to the square root of', x)
print('Number of bisection search guesses to find square root:', numGuesses)

print('')
print('')
if nr_iterations <= numGuesses:
    print('Newton-Raphson is more efficient than bisection search!')
else:
    print('Bisection search is somehow more efficient than Newton-Raphson!')
