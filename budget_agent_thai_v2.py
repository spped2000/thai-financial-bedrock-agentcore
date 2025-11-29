#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thai Personal Budget Assistant - Version 2
Best Practice: English system prompt with Thai context awareness
"""

from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import calculator
from pydantic import BaseModel, Field
from typing import List
import matplotlib.pyplot as plt

# System prompt in ENGLISH (best practice for better model comprehension)
# Agent will respond in Thai when user inputs Thai, English when user inputs English
THAI_BUDGET_SYSTEM_PROMPT = """You are a friendly personal financial advisor assistant for Thai users.

Your responsibilities:
- Provide budgeting and savings advice tailored to Thai context
- Analyze spending patterns and give practical recommendations
- Help with financial calculations and planning
- ALWAYS use Thai Baht (฿) as the currency in all calculations and outputs
- Consider Thai cost of living, salary ranges, and cultural financial practices
- Respond in Thai language when users write in Thai
- Respond in English when users write in English

Important guidelines:
- DO NOT provide investment advice on stocks, funds, or cryptocurrency
- DO NOT guarantee investment returns
- DO NOT recommend unregulated financial products
- Focus on budgeting, saving, and expense management only

Response format:
- Keep responses concise and actionable
- Provide 2-3 clear steps the user can implement
- Use friendly, easy-to-understand language
- Include specific Thai Baht amounts in examples

Thai context awareness:
- Typical Bangkok monthly salary: 25,000-60,000 THB
- Typical provincial salary: 15,000-30,000 THB
- Typical rent in Bangkok: 5,000-15,000 THB
- Typical food costs: 150-400 THB/day
- Common expenses: phone 300-600 THB/month, utilities 1,000-2,500 THB/month
- Respect Thai cultural values around family savings and support
- Consider Thai government savings programs (กบข., สบท., etc.)
"""

# Pydantic models for structured outputs
class BudgetCategoryThai(BaseModel):
    name: str = Field(description="Budget category name in Thai")
    amount: float = Field(description="Amount in Thai Baht")
    percentage: float = Field(description="Percentage of total income")


class FinancialReportThai(BaseModel):
    monthly_income: float = Field(description="Monthly income in Thai Baht")
    budget_categories: List[BudgetCategoryThai] = Field(
        description="List of budget categories"
    )
    recommendations: List[str] = Field(
        description="Specific recommendations in Thai"
    )
    financial_health_score: int = Field(
        ge=1, le=10, description="Financial health score (1-10)"
    )


# Bedrock Model Configuration
bedrock_model = BedrockModel(
    model_id="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
    region_name="us-west-2",
    temperature=0.7,  # Slightly higher for more natural Thai responses
)


@tool
def calculate_budget_thai(monthly_income: float) -> str:
    """Calculate 50/30/20 budget breakdown for Thai Baht monthly income."""
    needs = monthly_income * 0.50  # Essentials
    wants = monthly_income * 0.30  # Non-essentials
    savings = monthly_income * 0.20  # Savings

    return f"""💰 แผนงบประมาณสำหรับเงินเดือน {monthly_income:,.0f} บาท/เดือน:

📌 ค่าใช้จ่ายจำเป็น (50%): {needs:,.0f} บาท
   - ค่าเช่าบ้าน/ผ่อนบ้าน
   - ค่าอาหาร ค่าน้ำ ค่าไฟ
   - ค่าเดินทาง ค่าโทรศัพท์
   - ค่าประกันสุขภาพ/สังคม

🎉 ค่าใช้จ่ายไม่จำเป็น (30%): {wants:,.0f} บาท
   - ความบันเทิง ท่องเที่ยว
   - ช้อปปิ้ง งานอดิเรก
   - กินนอกบ้าน

💎 เงินออม (20%): {savings:,.0f} บาท
   - กองทุนฉุกเฉิน
   - เงินออมระยะยาว
   - ลงทุนเพื่ออนาคต (กบข., สบท., กองทุนรวม)
"""


@tool
def create_financial_chart_thai(
    data_dict: dict, chart_title: str = "กราฟการเงิน"
) -> str:
    """Create a pie chart from financial data with Thai labels."""
    if not data_dict:
        return "❌ ไม่มีข้อมูลสำหรับสร้างกราฟ"

    labels = list(data_dict.keys())
    values = list(data_dict.values())
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57", "#FF9FF3"]

    plt.figure(figsize=(10, 7))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors[: len(values)],
        startangle=90,
        textprops={'fontsize': 10}
    )
    plt.title(f"📊 {chart_title}", fontsize=16, fontweight="bold", pad=20)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

    return f"✅ สร้างกราฟ '{chart_title}' เรียบร้อยแล้ว!"


# Create the Thai budget agent
budget_agent_thai = Agent(
    model=bedrock_model,
    system_prompt=THAI_BUDGET_SYSTEM_PROMPT,
    tools=[calculate_budget_thai, create_financial_chart_thai, calculator],
)


if __name__ == "__main__":
    import sys

    # Set UTF-8 encoding for Windows console
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("\n" + "=" * 80)
    print("📊 ผู้ช่วยวางแผนงบประมาณส่วนบุคคลภาษาไทย (Thai Budget Assistant)")
    print("=" * 80)

    # Test 1: Thai input - should get Thai response
    print("\n[TEST 1] Thai Input")
    print("-" * 80)
    response = budget_agent_thai(
        "ผมมีเงินเดือน 35,000 บาท ใช้จ่ายค่าอาหารนอกบ้าน 9,000 บาทต่อเดือน มากไปไหม?"
    )
    print(response)

    # Test 2: Generate structured report
    print("\n[TEST 2] Structured Financial Report")
    print("-" * 80)
    try:
        report = budget_agent_thai.structured_output(
            output_model=FinancialReportThai,
            prompt="สร้างรายงานการเงินสำหรับคนที่มีเงินเดือน 40,000 บาท และใช้จ่ายค่าอาหารนอกบ้าน 10,000 บาทต่อเดือน",
        )

        print(f"\n💰 รายได้ต่อเดือน: {report.monthly_income:,.0f} บาท")
        print("\n📋 แผนการใช้จ่าย:")
        print("-" * 80)
        for category in report.budget_categories:
            print(f"  • {category.name}: {category.amount:,.0f} บาท ({category.percentage:.1f}%)")

        print(f"\n🏆 คะแนนสุขภาพทางการเงิน: {report.financial_health_score}/10")

        print("\n💡 คำแนะนำ:")
        print("-" * 80)
        for i, rec in enumerate(report.recommendations, 1):
            print(f"  {i}. {rec}")

    except Exception as e:
        print(f"Error generating report: {e}")

    # Test 3: English input - should get English response
    print("\n[TEST 3] English Input")
    print("-" * 80)
    response = budget_agent_thai(
        "I earn 50,000 baht per month in Bangkok. How should I budget my money?"
    )
    print(response)

    print("\n" + "=" * 80)
    print("✓ Testing complete!")
    print("=" * 80)
