# If a number is a palindrome using string reversal

num = input("Enter a number: ")
reversed_num = num[::-1]

if num == reversed_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")