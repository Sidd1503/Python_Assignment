# Print multiplication table using for loop

# Take input from the user
num = int(input("Enter a number: "))

# Print multiplication table (1 to 10)
print("\nMultiplication Table of",num,":")
for i in range(1, 11):
    print(num, "x {i} = {num * i}")