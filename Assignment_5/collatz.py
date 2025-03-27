# University of Cape Town
# Dumisani Mathabathe
# 22/03/2025

def colz_sequence(n):
    if n <= 0:
        print("Expecting a positive integer...")
        return
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer:\n"))
        colz_sequence(num)
    except ValueError:
        print("Expecting a positive integer...")


