from Extract_Specific_Details.utils.prompts import ERROR_HANDLING_PROMPT
# from utils.prompts import ERROR_HANDLING_PROMPT

async def run_error_handling(transcript: str, llm) -> str:
    prompt = ERROR_HANDLING_PROMPT
    full_prompt = prompt + "\n\n" + transcript
    response = await llm.ainvoke(full_prompt)
    return response.content.strip()