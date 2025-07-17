import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def setup_environment():
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        raise EnvironmentError("GOOGLE_API_KEY not found in .env file")
    if not os.getenv("YOUTUBE_API_KEY"):
        raise EnvironmentError("YOUTUBE_API_KEY not found in .env file")
    # if not os.getenv("OPENAI_API_KEY"):
    #     raise EnvironmentError("OPENAI_API_KEY not found in .env file")

def get_gemini_flash_model():
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1)






# def get_model(model_type="gemini", model_name=None, temperature=1):
#     if model_type == "gemini":
#         name = model_name or "gemini-1.5-flash"
#         return ChatGoogleGenerativeAI(model=name, temperature=temperature)
#     elif model_type == "gpt":
#         from langchain_openai import ChatOpenAI
#         name = model_name or "gpt-4o"
#         return ChatOpenAI(model=name, temperature=temperature)
#     else:
#         raise ValueError("Unsupported model type")