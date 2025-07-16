from Extract_Specific_Details.utils.prompts import LINKS_REFERENCES_PROMPT
# from utils.prompts import LINKS_REFERENCES_PROMPT

async def run_links_reference(transcript: str, llm) -> str:
    response = await llm.ainvoke(LINKS_REFERENCES_PROMPT + "\n\n" + transcript)
    return response.content.strip()