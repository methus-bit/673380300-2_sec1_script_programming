def snippet_a_fixed():
    print("--- Buggy Snippet A (Fixed) ---")
    counter = 0
    while counter < 5:
        print(f"Counter is: {counter}")
        counter += 1  # เพิ่มการอัปเดตเพื่อหลีกเลี่ยง Loop ตัน

def snippet_b_fixed():
    print("\n--- Buggy Snippet B (Fixed) ---")
    print("Goal: Print 1 to 5")
    for i in range(1, 6):  # ปรับขอบเขตเป็น 6 เพื่อรันค่า 5 ด้วย
        print(i)

def snippet_c_fixed():
    print("\n--- Buggy Snippet C (Fixed) ---")
    for char in "hello":
        if char == 'l':
            print("Found 'l', stopping!")
            break
        print(char)

if __name__ == "__main__":
    snippet_a_fixed()
    snippet_b_fixed()
    snippet_c_fixed()