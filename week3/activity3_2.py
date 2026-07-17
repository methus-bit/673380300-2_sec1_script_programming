def draw_square(size=5):
    print("--- 1. Square of Asterisks ---")
    for row in range(size):
        for col in range(size):
            print("* ", end="")
        print()

def draw_triangle(height=5):
    print("\n--- 2. Right-Angled Triangle ---")
    for row in range(1, height + 1):
        for col in range(row):
            print("* ", end="")
        print()

def draw_inverted_triangle(height=5):
    print("\n--- 3. Inverted Right-Angled Triangle ---")
    for row in range(height, 0, -1):
        for col in range(row):
            print("* ", end="")
        print()

def draw_pyramid(height=5):
    print("\n--- 4. Full Pyramid Challenge ---")
    for row in range(1, height + 1):
        # พิมพ์ช่องว่างนำหน้าเพื่อความสมดุล
        for space in range(height - row):
            print("  ", end="")
        # พิมพ์เครื่องหมายดาวตามสูตรเลขคี่ (2*n - 1)
        for col in range(2 * row - 1):
            print("* ", end="")
        print()

if __name__ == "__main__":
    draw_square()
    draw_triangle()
    draw_inverted_triangle()
    draw_pyramid()