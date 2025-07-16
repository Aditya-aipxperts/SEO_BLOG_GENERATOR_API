from Generate_topic_keyword.utils.prompts import KEYWORDS_PROMPT
# from utils.prompts import KEYWORDS_PROMPT

async def  keywords(transcript:str, llm) -> str:
    response = await llm.ainvoke(KEYWORDS_PROMPT + "\n\n" + transcript)
    return response.content.strip()

