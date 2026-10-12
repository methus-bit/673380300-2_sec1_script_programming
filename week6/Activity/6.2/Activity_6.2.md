### **Activity 6.2: Discussion: Benefits of Modular Programming & Standard Library Exploration**

#### **1. ประโยชน์ของการเขียนโปรแกรมแบบแยกส่วน (Benefits of Modularity)**

การแบ่งโค้ดออกเป็นฟังก์ชันและโมดูลย่อยมีประโยชน์สำคัญดังนี้:

* **การบำรุงรักษาและการแก้จุดบกพร่อง (Debugging & Maintenance):** เมื่อเกิดข้อผิดพลาด (Bug) เราสามารถระบุตำแหน่งและแก้ไขได้ง่ายขึ้นภายในฟังก์ชันนั้นๆ โดยไม่ต้องไล่อ่านโค้ดทั้งหมดหลายร้อยบรรทัด
* **การทำงานเป็นทีม (Teamwork):** สมาชิกในทีมสามารถแบ่งหน้าที่กันเขียนแต่ละฟังก์ชันหรือแต่ละโมดูลพร้อมๆ กันได้ โดยไม่ทับซ้อนหรือขัดแย้งกันในไฟล์เดียวกัน
* **การนำกลับมาใช้ซ้ำ (Code Reusability - DRY Principle):** ไม่ต้องเขียนโค้ดชุดเดิมซ้ำๆ หากต้องการใช้ตรรกะเดิมในโปรแกรมอื่น สามารถอิมพอร์ต (Import) โมดูลนั้นมาใช้ได้ทันที
* **การทดสอบระบบ (Code Testing):** ช่วยให้สามารถเขียน Unit Test เพื่อทดสอบการทำงานของแต่ละฟังก์ชันแยกจากกันได้อย่างแม่นยำ

---

#### **2. การสำรวจ Standard Library ที่น่าสนใจ (Standard Library Exploration)**

Python มีโมดูลมาตรฐานที่ติดตั้งมาให้อยู่แล้วจำนวนมาก ซึ่งช่วยลดเวลาในการพัฒนาโปรแกรมได้อย่างมหาศาล ตัวอย่าง 3 โมดูลที่น่าสนใจพร้อมตัวอย่างการใช้งาน:

##### **ก) โมดูล `datetime` (จัดการเกี่ยวกับวันที่และเวลา)**

* **ประโยชน์:** ใช้คำนวณช่วงเวลา, แปลงรูปแบบวันที่, หรือดึงเวลาปัจจุบันของระบบ
* **ตัวอย่างการใช้งาน:**
```python
import datetime

# ดึงวันและเวลาปัจจุบัน
now = datetime.datetime.now()
print(f"Current Date and Time: {now}")

# คำนวณวันในอนาคต (อีก 7 วันข้างหน้า)
future_date = now + datetime.timedelta(days=7)
print(f"Date after 7 days: {future_date.strftime('%Y-%m-%d')}")

```



##### **ข) โมดูล `os` (โต้ตอบกับระบบปฏิบัติการ)**

* **ประโยชน์:** ใช้จัดการไฟล์และโฟลเดอร์ ตรวจสอบเส้นทางไฟล์ หรือสั่งงานระบบปฏิบัติการ
* **ตัวอย่างการใช้งาน:**
```python
import os

# ดูว่าปัจจุบันเราอยู่โฟลเดอร์ใด (Current Working Directory)
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# ตรวจสอบว่ามีไฟล์นี้อยู่จริงหรือไม่
file_exists = os.path.exists("my_utils.py")
print(f"Does my_utils.py exist? {file_exists}")

```



##### **ค) โมดูล `collections` (โครงสร้างข้อมูลขั้นสูง)**

* **ประโยชน์:** มีเครื่องมือจัดเก็บข้อมูลที่มีประสิทธิภาพสูงกว่าโครงสร้างข้อมูลพื้นฐาน เช่น `Counter` สำหรับนับความถี่ของข้อมูล
* **ตัวอย่างการใช้งาน:**
```python
from collections import Counter

# นับความถี่ของคำหรือตัวอักษรในลิสต์
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
fruit_count = Counter(fruits)

print("Fruit Frequencies:", fruit_count)
# ผลลัพธ์: Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print("Most common fruit:", fruit_count.most_common(1))

```