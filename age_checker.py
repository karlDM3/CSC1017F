# University of Cape Town
# Dumisani Mathabathe
# 11/03/2025

# Input birth year and current year
a = int(input("Enter your birth year:\n"))
b = int(input("Enter the current year:\n"))

# Calculate your age for this year
age = b - a

# Conditions to check if you were born in a leap year
if a%4==0:
    print(f"You are {age} years old.")
    print("You were born in a leap year.")
else:
    print(f"You are {age} years old.\nYou were not born in a leap year.")
    
