# main_program.py - Main script using custom module and standard libraries

import my_utils
import math
import random

def main():
    print("--- Testing Custom Module (my_utils) ---")
    # Call greet function from custom module
    my_utils.greet("Alice")[cite: 3]
    
    # Test is_prime function with a few numbers
    test_numbers = [7, 10, 13, 1, 15][cite: 3]
    for num in test_numbers:
        prime_status = my_utils.is_prime(num)[cite: 3]
        print(f"Is {num} prime? {prime_status}")

    print("\n--- Testing Standard Library (math) ---")
    # Use math.sqrt() to calculate square root
    sqrt_val = math.sqrt(25)[cite: 3]
    print(f"Square root of 25: {sqrt_val}")
    print(f"Value of pi: {math.pi}")

    print("\n--- Testing Standard Library (random) ---")
    # Use random.randint() to generate a random number between 1 and 100
    random_num = random.randint(1, 100)[cite: 3]
    print(f"Random number (1-100): {random_num}")

if __name__ == "__main__":
    main()