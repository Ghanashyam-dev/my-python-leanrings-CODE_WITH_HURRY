# PRACTICE REVERSING OF NUMBER ! ! ! ! ! 

# Take input from the user
num = int(input("Enter a number: "))

reversed_num = 0
original_num = num  # store original number (optional)

# While loop to reverse the number
while num > 0:
    digit = num % 10          # get the last digit
    reversed_num = reversed_num * 10 + digit  # append digit to reversed number
    num = num // 10           # remove last digit from original number

print(f"Reversed number of {original_num} is {reversed_num}")
