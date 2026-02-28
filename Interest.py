# Calculate simple interest

# Take input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Calculate total amount
total_amount = principal + simple_interest

# Print the result
print("\nSimple Interest:",simple_interest)
print("Total Amount:",total_amount)