# University of Cape Town
# Dumisani Mathabathe
# 22/03/2025

# x for rows amd y for collumns
def print_grid(n, x, y):
    for i in range(x):
        for j in range(y):
            print(f"{n:3}", end=" ")
            n += 1
        print()

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the starting number (n):\n"))
            while True:
                x = int(input("Enter the number of rows (r):\n"))
                y = int(input("Enter the number of columns (c):\n"))
                if x > 0 and y > 0:
                    print_grid(n, x, y)
                    break
                else:
                    print("Rows and columns must be positive integers.")
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")
