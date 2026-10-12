# number_classifier_refactored.py

def is_positive_negative_zero(num):
    """ตรวจสอบว่าตัวเลขเป็น บวก, ลบ หรือ ศูนย์"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def is_even_odd(num):
    """ตรวจสอบว่าตัวเลขเป็นเลขคู่หรือเลขคี่ (ใช้เฉพาะกรณีที่เป็นจำนวนเต็ม)"""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    print("--- Number Classifier (Refactored with Functions) ---")
    try:
        user_input = float(input("Enter a number to classify: "))
        
        # เรียกใช้งานฟังก์ชันที่แยกไว้
        pos_neg_result = is_positive_negative_zero(user_input)
        print(f"The number is: {pos_neg_result}")
        
        # ถ้าเป็นจำนวนเต็ม สามารถตรวจสอบคู่/คี่ได้ด้วย
        if user_input.is_integer():
            int_num = int(user_input)
            even_odd_result = is_even_odd(int_num)
            print(f"The integer value is: {even_odd_result}")
            
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()