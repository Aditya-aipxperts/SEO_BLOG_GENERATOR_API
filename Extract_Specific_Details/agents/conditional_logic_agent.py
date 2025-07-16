from Extract_Specific_Details.utils.prompts import CONDITIONAL_LOGIC_PROMPT
# from utils.prompts import CONDITIONAL_LOGIC_PROMPT

async def run_conditional_logic(transcript: str, llm) -> str:
    response = await llm.ainvoke(CONDITIONAL_LOGIC_PROMPT + "\n\n" + transcript)
    return response.content.strip()