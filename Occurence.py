# Find occurrence of a character using count()

# Take input from the user
string = input("Enter a string: ")
char = input("Enter the character to find: ")

# Use built-in count() function
count = string.count(char)

# Print the result
print(char," occurs ",count," time's in the string.")