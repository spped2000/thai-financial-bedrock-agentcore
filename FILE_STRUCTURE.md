# Lab1 File Structure

```
C:\Users\natdh\Documents\AWS_Workshop\Lab1\
│
├── 📓 lab1_thai_personal_budget_assistant.ipynb
│   └── Jupyter notebook หลัก - Interactive Thai budget assistant
│
├── 🐍 budget_agent_thai_v2.py
│   └── Standalone Python script - ใช้งานได้เลยโดยไม่ต้อง notebook
│
├── 🔍 check_thai_fonts.py
│   └── ตรวจสอบ fonts ที่รองรับภาษาไทย
│
├── 📋 requirements.txt
│   └── Python packages ที่ต้องใช้
│
├── 📚 Documentation
│   ├── README.md - Quick overview
│   ├── README_THAI.md - เอกสารภาษาไทยฉบับเต็ม
│   ├── THAI_VERSION_SUMMARY.md - สรุปการทำงาน
│   ├── THAI_FONT_SETUP.md - วิธีแก้ปัญหา fonts
│   ├── QUICKSTART.md - เริ่มใช้งานภายใน 5 นาที
│   └── FILE_STRUCTURE.md - ไฟล์นี้
│
├── 🛠️ utils/
│   ├── __init__.py - Package initialization
│   ├── guardrail_thai.py - Thai-specific guardrails
│   └── message_formatter.py - Format conversation messages
│
└── .gitignore - Git ignore rules

```

## 📁 File Descriptions

### Main Files

#### lab1_thai_personal_budget_assistant.ipynb
- **Type**: Jupyter Notebook
- **Size**: ~140 KB
- **Purpose**: Interactive workshop notebook
- **Features**:
  - Step-by-step tutorial
  - Thai language support
  - Live code execution
  - Charts and visualizations

#### budget_agent_thai_v2.py
- **Type**: Python Script
- **Size**: ~8 KB
- **Purpose**: Standalone budget assistant
- **Features**:
  - English system prompt (best practice)
  - Auto language detection
  - Structured outputs
  - Thai context awareness

#### check_thai_fonts.py
- **Type**: Utility Script
- **Size**: ~2.5 KB
- **Purpose**: Font compatibility checker
- **Output**: 
  - List of Thai-compatible fonts
  - Test image (thai_font_test.png)

### Configuration

#### requirements.txt
- **Type**: Package manifest
- **Size**: ~8.5 KB
- **Packages**:
  - strands
  - strands-tools
  - boto3
  - matplotlib
  - pydantic
  - And dependencies...

### Documentation

#### README.md
- **Language**: Mixed (Thai/English)
- **Length**: Short (quick reference)
- **Audience**: All users

#### README_THAI.md
- **Language**: Thai
- **Length**: Comprehensive (~17 KB)
- **Audience**: Thai developers
- **Contents**:
  - Full documentation in Thai
  - Thai examples
  - Thai context explanations

#### THAI_VERSION_SUMMARY.md
- **Language**: Mixed
- **Length**: Medium (~9.5 KB)
- **Audience**: Developers
- **Contents**:
  - Implementation summary
  - Best practices
  - Comparison tables

#### THAI_FONT_SETUP.md
- **Language**: Mixed
- **Length**: Medium (~5.4 KB)
- **Purpose**: Troubleshooting guide
- **Contents**:
  - Font installation
  - Matplotlib configuration
  - Platform-specific fixes

#### QUICKSTART.md
- **Language**: Mixed
- **Length**: Short
- **Time**: 5-minute setup
- **Steps**: 4 simple steps

### Utils Package

#### utils/__init__.py
- **Type**: Package init
- **Size**: ~500 bytes
- **Exports**:
  - create_thai_guardrail
  - get_thai_guardrail_id
  - delete_thai_guardrail
  - pretty_print_messages

#### utils/guardrail_thai.py
- **Type**: Guardrail configuration
- **Size**: ~7 KB
- **Features**:
  - Thai-specific blocked terms
  - Cryptocurrency blocking
  - Investment scam detection
  - Thai blocked messages

#### utils/message_formatter.py
- **Type**: Utility
- **Size**: ~6 KB
- **Purpose**: Format conversation history

## 🎯 Usage Patterns

### For Learning (Recommended)
```
1. Read QUICKSTART.md
2. Open lab1_thai_personal_budget_assistant.ipynb
3. Run cells step by step
4. Refer to README_THAI.md for details
```

### For Production
```
1. Use budget_agent_thai_v2.py
2. Import: from budget_agent_thai_v2 import budget_agent_thai
3. Integrate into your application
```

### For Troubleshooting
```
1. Font issues → THAI_FONT_SETUP.md
2. General issues → README_THAI.md
3. API reference → THAI_VERSION_SUMMARY.md
```

## 📊 File Sizes

```
Total: ~210 KB

Large files:
- lab1_thai_personal_budget_assistant.ipynb: 140 KB
- README_THAI.md: 17 KB
- THAI_VERSION_SUMMARY.md: 9.5 KB
- requirements.txt: 8.5 KB
- budget_agent_thai_v2.py: 8 KB
- utils/guardrail_thai.py: 7 KB
- utils/message_formatter.py: 6 KB
```

## 🔄 Dependencies

```
External Dependencies:
├── strands (Strands Agents SDK)
├── strands-tools (Pre-built tools)
├── boto3 (AWS SDK)
├── matplotlib (Charts)
└── pydantic (Data validation)

Internal Dependencies:
└── utils/
    ├── guardrail_thai.py
    └── message_formatter.py
```

## 🚀 Quick Commands

```bash
# Setup
pip install -r requirements.txt

# Check fonts
python check_thai_fonts.py

# Run standalone
python budget_agent_thai_v2.py

# Open notebook
jupyter notebook lab1_thai_personal_budget_assistant.ipynb

# Create guardrail
python -c "from utils.guardrail_thai import create_thai_guardrail; create_thai_guardrail()"
```

---

**Total Files**: 11 core files + 3 utils
**Total Size**: ~210 KB
**Languages**: Python, Jupyter, Markdown
**AWS Services**: Bedrock (Claude Sonnet 4.5)
