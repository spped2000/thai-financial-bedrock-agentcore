# Lab1 - Thai Personal Budget Assistant

ผู้ช่วยวางแผนงบประมาณส่วนบุคคลภาษาไทย

## 📁 ไฟล์ในโฟลเดอร์นี้

### หลัก (Main Files):
- **lab1_thai_personal_budget_assistant.ipynb** - Jupyter notebook หลัก
- **budget_agent_thai_v2.py** - Python script แบบ standalone
- **requirements.txt** - Python packages ที่ต้องใช้

### Utilities:
- **utils/guardrail_thai.py** - Thai-specific guardrails
- **utils/__init__.py** - Package initialization
- **check_thai_fonts.py** - ตรวจสอบ fonts ภาษาไทย

### เอกสาร (Documentation):
- **README_THAI.md** - เอกสารภาษาไทยฉบับเต็ม
- **THAI_VERSION_SUMMARY.md** - สรุปการทำงาน
- **THAI_FONT_SETUP.md** - วิธีแก้ปัญหา fonts

## 🚀 เริ่มต้นใช้งาน

### 1. ติดตั้ง dependencies:

```bash
pip install -r requirements.txt
```

### 2. ตรวจสอบ Thai fonts:

```bash
python check_thai_fonts.py
```

### 3. เปิด Jupyter Notebook:

```bash
jupyter notebook lab1_thai_personal_budget_assistant.ipynb
```

### 4. หรือรัน Python script:

```bash
python budget_agent_thai_v2.py
```

## 🎯 คุณสมบัติ

✅ ตอบคำถามภาษาไทยได้
✅ Auto-detect ภาษา (Thai/English)
✅ ใช้สกุลเงินบาท (฿)
✅ Guardrails สำหรับภาษาไทย
✅ Tools: คำนวณงบประมาณ, สร้างกราฟ
✅ Structured outputs
✅ Thai font support ใน charts

## 💡 ตัวอย่างการใช้งาน

```python
from strands import Agent
from strands.models import BedrockModel
from utils.guardrail_thai import create_thai_guardrail

# สร้าง guardrail
guardrail_id, guardrail_arn = create_thai_guardrail()

# สร้าง agent
bedrock_model = BedrockModel(
    model_id="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
    region_name="us-west-2",
    temperature=0.7,
    guardrail_id=guardrail_id,
    guardrail_version="DRAFT",
)

agent = Agent(model=bedrock_model)

# ใช้งาน
response = agent("ผมมีเงินเดือน 30,000 บาท ช่วยวางแผนงบประมาณหน่อย")
print(response)
```

## 📊 Thai Context

- เงินเดือนกรุงเทพฯ: 25,000-60,000 บาท
- เงินเดือนต่างจังหวัด: 15,000-30,000 บาท
- ค่าเช่ากรุงเทพฯ: 5,000-15,000 บาท
- ค่าอาหาร: 150-400 บาท/วัน

## 🔐 Thai Guardrails

ป้องกัน:
- คริปโต, บิทคอยน์
- กลโกงการลงทุน (รวยเร็ว, แชร์ลูกโซ่)
- Forex, หุ้นแนะนำ
- กู้เงินด่วน

## 📚 เอกสารเพิ่มเติม

- [README_THAI.md](README_THAI.md) - เอกสารฉบับเต็ม
- [THAI_FONT_SETUP.md](THAI_FONT_SETUP.md) - แก้ปัญหา fonts

---

**สร้างเมื่อ**: 2025-11-29
**Model**: Claude Sonnet 4.5
**Region**: us-west-2
