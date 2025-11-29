# Configure AWS clients for Thai financial guardrails
import boto3

# Use us-west-2 region for consistency with the model
bedrock_client = boto3.client("bedrock", region_name="us-west-2")
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-west-2")


def create_thai_guardrail():
    """
    Create a guardrail specifically for Thai financial assistant use cases.
    Blocks cryptocurrency advice, investment scams, and inappropriate content
    common in Thai context.
    """
    guardrail_name = "guardrail-thai-financial-advisor"

    # Check if guardrail already exists
    try:
        existing_guardrails = bedrock_client.list_guardrails()
        for guardrail in existing_guardrails.get("guardrails", []):
            if guardrail.get("name") == guardrail_name:
                print(
                    f"Guardrail '{guardrail_name}' already exists. Returning existing guardrail."
                )
                return (guardrail.get("id"), guardrail.get("arn"))
    except Exception as e:
        print(f"Error checking existing guardrails: {e}")

    # Create new guardrail if it doesn't exist
    print(f"Creating new Thai financial guardrail '{guardrail_name}'...")

    response = bedrock_client.create_guardrail(
        name=guardrail_name,
        description="Guardrail for Thai personal finance assistant - blocks cryptocurrency, investment scams, and inappropriate financial advice",
        contentPolicyConfig={
            "filtersConfig": [
                {"type": "SEXUAL", "inputStrength": "HIGH", "outputStrength": "HIGH"},
                {"type": "VIOLENCE", "inputStrength": "HIGH", "outputStrength": "HIGH"},
                {"type": "HATE", "inputStrength": "HIGH", "outputStrength": "HIGH"},
                {"type": "INSULTS", "inputStrength": "HIGH", "outputStrength": "HIGH"},
                {
                    "type": "MISCONDUCT",
                    "inputStrength": "HIGH",
                    "outputStrength": "HIGH",
                },
                {
                    "type": "PROMPT_ATTACK",
                    "inputStrength": "HIGH",
                    "outputStrength": "NONE",
                },
            ]
        },
        wordPolicyConfig={
            "wordsConfig": [
                # English cryptocurrency terms
                {"text": "Bitcoin"},
                {"text": "cryptocurrency investment"},
                {"text": "crypto trading"},
                {"text": "Ethereum"},
                {"text": "altcoin"},

                # Thai cryptocurrency terms
                {"text": "คริปโต"},
                {"text": "เหรียญดิจิทัล"},
                {"text": "ลงทุนคริปโต"},
                {"text": "เทรดคริปโต"},
                {"text": "บิทคอยน์"},

                # Thai investment scam terms
                {"text": "ลงทุนรับกำไร"},
                {"text": "รับกำไรแน่นอน"},
                {"text": "รวยเร็ว"},
                {"text": "หาเงินง่าย"},
                {"text": "แชร์ลูกโซ่"},
                {"text": "ระบบพีระมิด"},

                # Forex/stock gambling
                {"text": "forex แม่นยำ"},
                {"text": "หุ้นแนะนำ"},
                {"text": "ลงทุนหุ้นกำไร"},

                # Loan sharks
                {"text": "กู้เงินด่วน"},
                {"text": "สินเชื่อไม่ต้องค้ำ"},
            ],
            "managedWordListsConfig": [{"type": "PROFANITY"}],
        },
        blockedInputMessaging="ขออภัยครับ/ค่ะ ผมไม่สามารถให้คำแนะนำเกี่ยวกับการลงทุนใน cryptocurrency, หุ้น, หรือโฟเร็กซ์ได้ กรุณาปรึกษาที่ปรึกษาการเงินที่ได้รับใบอนุญาตจาก ก.ล.ต. (Securities and Exchange Commission) สำหรับคำแนะนำด้านการลงทุน",
        blockedOutputsMessaging="ขออภัยครับ/ค่ะ ผมไม่สามารถให้คำแนะนำประเภทนี้ได้ กรุณาปรึกษาผู้เชี่ยวชาญด้านการเงินที่ได้รับการรับรองเพื่อความปลอดภัยของคุณ",
    )

    print(f"[OK] Thai guardrail created successfully!")
    return (response.get("guardrailId"), response.get("guardrailArn"))


def delete_thai_guardrail(guardrail_id=None):
    """
    Delete the Thai financial guardrail by ID, or find and delete by name if no ID provided.

    Args:
        guardrail_id: The ID of the guardrail to delete (optional)

    Returns:
        bool: True if deletion was successful, False otherwise
    """
    guardrail_name = "guardrail-thai-financial-advisor"

    try:
        # If no ID provided, find it by name
        if not guardrail_id:
            existing_guardrails = bedrock_client.list_guardrails()
            for guardrail in existing_guardrails.get("guardrails", []):
                if guardrail.get("name") == guardrail_name:
                    guardrail_id = guardrail.get("id")
                    break

            if not guardrail_id:
                print(f"Guardrail '{guardrail_name}' not found")
                return False

        # Delete the guardrail
        print(f"Deleting guardrail '{guardrail_name}' with ID: {guardrail_id}")
        bedrock_client.delete_guardrail(guardrailIdentifier=guardrail_id)
        print(f"Successfully deleted guardrail: {guardrail_name}")
        return True

    except Exception as e:
        print(f"Error deleting guardrail: {e}")
        return False


def get_thai_guardrail_id():
    """
    Get the guardrail ID for the Thai financial guardrail.

    Returns:
        str or None: The guardrail ID if found, None otherwise
    """
    guardrail_name = "guardrail-thai-financial-advisor"

    try:
        existing_guardrails = bedrock_client.list_guardrails()
        for guardrail in existing_guardrails.get("guardrails", []):
            if guardrail.get("name") == guardrail_name:
                guardrail_id = guardrail.get("id")
                print(f"Found guardrail '{guardrail_name}' with ID: {guardrail_id}")
                return guardrail_id

        print(f"Guardrail '{guardrail_name}' not found")
        return None

    except Exception as e:
        print(f"Error finding guardrail: {e}")
        return None