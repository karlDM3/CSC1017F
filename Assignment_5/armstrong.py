# University of Cape Town
# Dumisani Mathabathe
# 23/03/2025

# Defining armstrong numbers
def armstrong_s(number):
    x = [int(y) for y in str(number)]
    power = len(x)
    armstrong_add = sum(y ** power for y in x)
    return armstrong_add == number

if __name__ == "__main__":
    num = int(input("Enter a number:\n"))
    if armstrong_s(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")