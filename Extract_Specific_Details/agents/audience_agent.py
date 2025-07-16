# from utils.prompts import AUDIENCE_PROMPT
from Extract_Specific_Details.utils.prompts import AUDIENCE_PROMPT
async def run_audience_spec(transcript: str, llm) -> str:
    response = await llm.ainvoke(AUDIENCE_PROMPT + "\n\n" + transcript)
    return response.content.strip()