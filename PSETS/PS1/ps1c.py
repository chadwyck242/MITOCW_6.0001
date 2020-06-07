####################################
# MIT OpenCourseWare
# 6.0001 Introduction to Computer Science
# and Programming in Python
# Problem Set PS1 Part C
####################################

# Part C: Finding the right amount to save away

# Request initial starting salary as input
annual_salary = float(input("Enter the starting salary: "))

# Initialize variables
r = 0.04  # annual rate of return on investment
monthly_salary = annual_salary / 12
current_savings = 0
semi_annual_raise = 0.07
portion_down_payment = 0.25
total_cost = 1000000
down_payment = total_cost * portion_down_payment

# set the "close enough" approximation of epsilon
# as well as initial high and low values
epsilon = 100
max_value = 10000
high = max(1.0, max_value)
low = 0
numSteps = 0
# looking for portion_saved using this algorithm
portion_saved = (high + low) // 2

# find best value for portion_saved using bi-section search
while abs(current_savings - down_payment) >= epsilon:

    current_savings = 0
    # temporary variable for use in the loop
    temp_salary = annual_salary
    # convert portion_saved into a float
    float_rate = portion_saved / 10000

    # begin looping over 36 months to calculate amount saved
    for month in range(36):
        if month % 6 == 0 and month > 0:
            temp_salary += temp_salary * semi_annual_raise
        monthly_salary = temp_salary / 12
        current_savings += monthly_salary * float_rate + current_savings * r/12

    # conditional statements to determine new high and low values
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved

    # reset the portion_saved value to the new high / low midpoint
    portion_saved = (high + low) // 2
    numSteps += 1

    # handle situation when too many steps are needed for a given salary,
    # meaning that is it not possible to save the down payment given those
    # constraints
    if numSteps > 13:
        break


# produce the output following the bi-section search algorithm
if numSteps > 13:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search:", numSteps)
