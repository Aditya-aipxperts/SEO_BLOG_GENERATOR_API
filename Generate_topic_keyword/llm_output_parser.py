import re
import json
import os

def parse_keywords_output(text: str):
    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Extract Output 1: Primary Keywords
    primary_keywords_match = re.search(r"\*\*Output 1: Primary Keywords:\*\*\s*(.*?)\n\n", text, re.DOTALL)
    primary_keywords = [kw.strip() for kw in primary_keywords_match.group(1).split(",")] if primary_keywords_match else []

    # Extract Output 3: Secondary Keywords
    secondary_keywords_match = re.search(r"\*\*Output 3: Secondary Keywords:\*\*\s*(.*?)\n\n", text, re.DOTALL)
    secondary_keywords = [kw.strip() for kw in secondary_keywords_match.group(1).split(",")] if secondary_keywords_match else []

    # Extract Output 2: Justification Primary
    justification_primary_block = re.search(
        r"\*\*Output 2: Justification Primary:\*\*\s*(.*?)\n\n\*\*Output 3:",
        text,
        re.DOTALL
    )
    justification_primary_text = justification_primary_block.group(1) if justification_primary_block else ""

    # Extract Output 4: Justification Secondary
    justification_secondary_block = re.search(
        r"\*\*Output 4: Justification Secondary:\*\*\s*(.*)",
        text,
        re.DOTALL
    )
    justification_secondary_text = justification_secondary_block.group(1) if justification_secondary_block else ""

    # Helper: Extract justifications into dictionary
    def extract_justifications(block, keywords):
        justifications = {}
        for kw in keywords:
            pattern = rf"\*\*\s*{re.escape(kw)}\s*:\*\*\s*(.*?)(?=\n\s*\*\*|$)"
            match = re.search(pattern, block, re.DOTALL | re.IGNORECASE)
            if match:
                justification = ' '.join(match.group(1).split())
                justifications[kw] = justification
        return justifications

    primary_justifications = extract_justifications(justification_primary_text, primary_keywords)
    secondary_justifications = extract_justifications(justification_secondary_text, secondary_keywords)

    return {
        "primary_keywords": primary_keywords,
        "primary_justification": primary_justifications,
        "secondary_keywords": secondary_keywords,
        "secondary_justification": secondary_justifications
    }

# === MAIN ===
async def parse_keywords_output_main() -> dict:
    INPUT_PATH = "/home/aip-63/Desktop/Seo_Blog_Generator/Generate_topic_keyword/raw_output.json"
    OUTPUT_PATH = "parsed_keywords.json"

    # Detect if the input is JSON with { "text": "..." }
    if INPUT_PATH.endswith(".json"):
        with open(INPUT_PATH, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                raw_text = data["text"] if isinstance(data, dict) and "text" in data else str(data)
            except json.JSONDecodeError:
                print("⚠️ File is not valid JSON. Trying to read as plain text.")
                raw_text = f.read()
    else:
        # Plain text file
        with open(INPUT_PATH, "r", encoding="utf-8") as f:
            raw_text = f.read()

    result = parse_keywords_output(raw_text)

    # Save result
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ Extraction complete. Saved to {OUTPUT_PATH}")

    return result
