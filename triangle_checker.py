a = int(input("Enter the first side:\n"))
b = int(input("Enter the second side:\n"))
c = int(input("Enter the third side:\n"))

if a + b > c and a + c > b and b + c > a:
    print("The given sides form a valid triangle.")
else:
    print("The given sides do NOT form a valid triangle.")
