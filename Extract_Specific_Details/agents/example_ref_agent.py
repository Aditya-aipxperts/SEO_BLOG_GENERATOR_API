from Extract_Specific_Details.utils.prompts import EXAMPLE_REFERENCE_PROMPT
# from utils.prompts import EXAMPLE_REFERENCE_PROMPT

async def run_example_reference(transcript: str, llm) -> str:
    response = await llm.ainvoke(EXAMPLE_REFERENCE_PROMPT + "\n\n" + transcript)
    return response.content.strip()