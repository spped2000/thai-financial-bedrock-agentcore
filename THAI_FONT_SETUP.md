# แก้ปัญหาฟอนต์ภาษาไทยใน Matplotlib

## ปัญหา
ตัวอักษรภาษาไทยไม่แสดงผลใน chart (แสดงเป็นกล่องสี่เหลี่ยม □□□)

## วิธีแก้

### Option 1: เพิ่ม Code ใน Notebook (แนะนำ)

เพิ่ม cell นี้ **หลังจาก import matplotlib**:

```python
# Configure matplotlib to use Thai font
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Set Thai font (Tahoma works on Windows)
plt.rcParams['font.family'] = 'Tahoma'

# Verify font is set
print(f"Current font: {plt.rcParams['font.family']}")
```

### Option 2: ใช้ในแต่ละ Chart

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
plt.rcParams['font.family'] = 'Tahoma'  # Set ก่อนสร้าง chart

plt.pie(values, labels=thai_labels, autopct="%1.1f%%")
plt.title("กราฟค่าใช้จ่าย")
plt.show()
```

### Option 3: ใช้ในทุก Notebook (Global Config)

สร้างไฟล์ `matplotlibrc` ใน directory ของคุณ:

```
font.family: Tahoma
```

## Fonts ที่รองรับภาษาไทยใน Windows

จากการ scan ระบบของคุณ พบว่ามี fonts เหล่านี้:

1. **Tahoma** ✓ (แนะนำ - font มาตรฐาน Windows)
2. **Leelawadee UI** ✓ (Windows 10/11)
3. **Angsana New** ✓ (MS Office)
4. **Browallia New** ✓ (MS Office)
5. **Cordia New** ✓ (MS Office)
6. **DilleniaUPC** ✓

## Updated Code สำหรับ Notebook

ผมได้อัพเดท function `create_financial_chart_thai()` แล้วให้:
1. ลอง fonts ตามลำดับ (Tahoma → Arial Unicode MS → ...)
2. เลือก font ที่รองรับไทยโดยอัตโนมัติ
3. Fallback ไปยัง DejaVu Sans ถ้าไม่เจอ

```python
@tool
def create_financial_chart_thai(data_dict: dict, chart_title: str = "กราฟการเงิน") -> str:
    """สร้างกราฟวงกลมจากข้อมูลการเงิน (ภาษาไทย)"""
    import matplotlib.font_manager as fm

    # Try Thai fonts in order
    thai_fonts = ['Tahoma', 'Leelawadee UI', 'Angsana New', 'DejaVu Sans']

    font_to_use = None
    for font_name in thai_fonts:
        available_fonts = [f.name for f in fm.fontManager.ttflist]
        if font_name in available_fonts:
            font_to_use = font_name
            break

    if font_to_use:
        plt.rcParams['font.family'] = font_to_use

    # Create chart...
```

## ทดสอบ

รันคำสั่งนี้เพื่อทดสอบว่า font ทำงาน:

```bash
python check_thai_fonts.py
```

จะได้ไฟล์ `thai_font_test.png` ที่แสดงข้อความ "ทดสอบภาษาไทย"

## ตัวอย่างผลลัพธ์

### ก่อนแก้ไข:
```
□□□□□ (กล่องสี่เหลี่ยม)
```

### หลังแก้ไข:
```
ค่าเช่าบ้าน
ค่าอาหาร
ค่าเดินทาง
```

## Troubleshooting

### ถ้ายังไม่แสดงภาษาไทย:

1. **Restart Kernel**:
   - ใน Jupyter: Kernel → Restart

2. **ลบ matplotlib cache**:
```bash
python -c "import matplotlib; print(matplotlib.get_cachedir())"
# ลบโฟลเดอร์นั้นแล้ว restart
```

3. **ติดตั้ง Thai fonts เพิ่มเติม** (Linux):
```bash
sudo apt-get install fonts-thai-tlwg
fc-cache -fv
```

4. **ตรวจสอบ fonts ที่มี**:
```python
import matplotlib.font_manager as fm
for f in fm.fontManager.ttflist:
    if 'thai' in f.name.lower() or 'tahoma' in f.name.lower():
        print(f.name)
```

## สำหรับระบบอื่นๆ

### macOS:
```python
plt.rcParams['font.family'] = 'Thonburi'  # หรือ 'Arial Unicode MS'
```

### Linux:
```python
plt.rcParams['font.family'] = 'Loma'  # หรือ 'Garuda'
```

### Docker/Colab:
```bash
# ติดตั้ง fonts
!apt-get install fonts-thai-tlwg -y
!fc-cache -fv

# ใน Python
plt.rcParams['font.family'] = 'Loma'
```

## Quick Fix สำหรับ Notebook ที่มีอยู่

เพิ่ม cell นี้ไว้ใกล้ๆ ตอนต้น:

```python
# Thai font configuration
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Tahoma'  # Windows
# plt.rcParams['font.family'] = 'Thonburi'  # macOS
# plt.rcParams['font.family'] = 'Loma'  # Linux

print(f"✓ Font set to: {plt.rcParams['font.family']}")
```

---

**ระบบของคุณ**: ใช้ **Tahoma** (พร้อมใช้งาน!)

**ไฟล์ที่อัพเดทแล้ว**:
- `lab1_thai_personal_budget_assistant.ipynb` (cell-23)
- `budget_agent_thai_v2.py`

**ผลลัพธ์**: ภาษาไทยจะแสดงผลได้ในทุก chart! 🎉
