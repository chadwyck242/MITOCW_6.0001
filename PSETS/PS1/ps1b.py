####################################
# MIT OpenCourseWare
# 6.0001 Introduction to Computer Science
# and Programming in Python
# Problem Set PS1 Part B
####################################

# Part B: Saving, with a raise

# Get input as floats
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# initialize state variables
portion_down_payment = 0.25
current_savings = 0
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
r = 0.04  # annual rate of return on investment
months_required = 0
required_down_payment = total_cost * portion_down_payment

# Use looping and exhaustive enumeration to reach test condition
while current_savings < required_down_payment:
    current_savings = current_savings + \
        (current_savings * r / 12) + monthly_savings
    months_required += 1
    # Every six months apply the semi-annual raises
    if months_required % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved

print("Number of months: ", months_required)
