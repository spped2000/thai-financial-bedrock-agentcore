# Quick Start - Thai Budget Assistant

## ⚡ เริ่มใช้งานภายใน 5 นาที

### Step 1: ติดตั้ง Dependencies

```bash
cd C:\Users\natdh\Documents\AWS_Workshop\Lab1
pip install -r requirements.txt
```

### Step 2: ตรวจสอบ Thai Fonts

```bash
python check_thai_fonts.py
```

คุณควรเห็น:
```
✓ Thai-compatible fonts found on your system:
  • Tahoma
  • Leelawadee UI
  ...
```

### Step 3: เลือกวิธีใช้งาน

#### Option A: Jupyter Notebook (แนะนำ)

```bash
jupyter notebook lab1_thai_personal_budget_assistant.ipynb
```

แล้วรัน cells ทีละอัน:
1. Cell 1-5: Setup
2. Cell 6-11: Test basic agent
3. Cell 12-15: Budget agent
4. Cell 16-25: Advanced features

#### Option B: Python Script

```bash
python budget_agent_thai_v2.py
```

จะได้ผลลัพธ์ตัวอย่างทันที!

### Step 4: ทดสอบ

ใน notebook หรือ Python:

```python
from strands import Agent
from strands.models import BedrockModel

bedrock_model = BedrockModel(
    model_id="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
    region_name="us-west-2",
    temperature=0.7,
)

agent = Agent(model=bedrock_model)

# ทดสอบภาษาไทย
response = agent("ผมมีเงินเดือน 30,000 บาท ช่วยแนะนำหน่อย")
print(response)

# ทดสอบภาษาอังกฤษ  
response = agent("I earn 50,000 baht. How should I budget?")
print(response)
```

## 🎯 ทดสอบ Guardrails

```python
# ควรถูกบลอก
response = agent("แนะนำการลงทุนบิทคอยน์หน่อย")
print(response)
# Output: ขออภัยครับ/ค่ะ ผมไม่สามารถให้คำแนะนำเกี่ยวกับการลงทุนใน cryptocurrency...
```

## 📊 ทดสอบ Tools

```python
from utils.guardrail_thai import create_thai_guardrail

# สร้าง guardrail
guardrail_id, _ = create_thai_guardrail()

# สร้าง agent พร้อม tools
from budget_agent_thai_v2 import budget_agent_thai

response = budget_agent_thai("ผมมีเงินเดือน 35,000 บาท ช่วยวางแผนงบประมาณหน่อย")
print(response)
```

## ❓ Troubleshooting

### ปัญหา: ไม่มี module 'strands'
```bash
pip install strands strands-tools
```

### ปัญหา: Thai fonts ไม่แสดงใน chart
```bash
python check_thai_fonts.py
# ดู THAI_FONT_SETUP.md สำหรับวิธีแก้
```

### ปัญหา: Guardrail not found
```bash
python -c "from utils.guardrail_thai import create_thai_guardrail; create_thai_guardrail()"
```

### ปัญหา: AWS Credentials
```bash
aws configure
# หรือ
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx
export AWS_DEFAULT_REGION=us-west-2
```

## 📚 Next Steps

1. อ่าน [README_THAI.md](README_THAI.md) สำหรับรายละเอียดเต็ม
2. ดู [THAI_VERSION_SUMMARY.md](THAI_VERSION_SUMMARY.md) สำหรับสรุปการทำงาน
3. ทดลองแก้ system prompt ตามใจชอบ
4. เพิ่ม custom tools ของคุณเอง

---

**เวลาที่ใช้**: ~5 นาที
**ความยาก**: ⭐⭐☆☆☆ (ง่าย)
**Prerequisites**: Python 3.11+, AWS Account with Bedrock access

🎉 **เริ่มต้นได้เลย!**
