def part1_single_table():
    print("=== Part 1: Single Number Table ===")
    try:
        num = int(input("Enter a number for the multiplication table (e.g., 7): "))
        print(f"\nMultiplication table for {num}:")
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Error: Please enter a valid integer.")

def part2_full_grid():
    print("\n=== Part 2: Full 12x12 Multiplication Grid ===")
    print("    ", end="")
    # Print column header
    for col in range(1, 13):
        print(f"{col:4d}", end="")
    print("\n" + "-" * 54)
    
    # Print rows
    for i in range(1, 13):
        print(f"{i:2d} |", end="")  # Row header
        for j in range(1, 13):
            print(f"{i*j:4d}", end="")
        print()  # New line after each row

if __name__ == "__main__":
    part1_single_table()
    part2_full_grid()