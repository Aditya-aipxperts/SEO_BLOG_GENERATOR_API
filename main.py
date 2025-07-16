import asyncio
import json
import re
import traceback
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Fetch_transcript.main import get_transcript_with_backoff
from Extract_Specific_Details.main import extract_specific_details
from Generate_topic_keyword.llm_output import generate_topic_keyword
from Generate_Intro.main import generate_intro, refine_intro
from Generate_Guide.main import generate_guide
from Generate_issue_troubleshoot.main import generate_issue_troubleshooting
from Generate_Conclusion.main import generate_conclusion
from Generate_CTA.main import generate_cta
from Generate_Customization_tips.main import generate_customization_tips
from Domain_aligned.main import domain_aligned
from Rewrite_Blog.main import rewrite_blog
from schemas import SEOBlogGenerator
from setup_env import setup_environment, get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

app = FastAPI()

class PipelineRequest(BaseModel):
    video_url: str
    domain_url: str
    raw_blog: str

class PipelineResponse(BaseModel):
    Transcript: Optional[str] = None
    Specific_Details: Optional[dict] = None
    Topic_Keyword: Optional[dict] = None
    Refined_Intro: Optional[dict] = None
    Guide: Optional[dict] = None
    Issue_Troubleshoot: Optional[dict] = None
    Conclusion: Optional[dict] = None
    CTA: Optional[dict] = None
    Customization_Tips: Optional[dict] = None
    Domain_Aligned: Optional[dict] = None
    Final_Blog: Optional[str] = None
    error: Optional[str] = None

def extract_video_id(state: dict) -> dict:
    video_url = state.get("video_url") or ""
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", video_url)
    if match:
        state["video_id"] = match.group(1)
        return state
    raise ValueError("Could not extract video ID from URL")

async def full_pipeline(state: dict) -> dict:
    video_url = state.get("video_url") or ""
    domain_url = state.get("domain_url") or ""
    raw_blog = state.get("raw_blog") or ""
    results = {}
    extract_video_id(state)
    transcript = get_transcript_with_backoff(state)
    if not transcript or "Failed after multiple retries" in transcript:
        return {"error": f"Transcript not available for: {video_url}"}
    # results = {"Transcript": transcript}
    state["transcript"] = transcript

    specific_details = await extract_specific_details(state)
    # results["Specific_Details"] = state["extracted_section"]

    topic_keyword = await generate_topic_keyword(state)
    # results["Topic_Keyword"] = state["extracted_keywords"]

    state["combined_data_keyword_specific_details"] = {
        "topic_keyword": state.get("extracted_keywords"),
        "specific_details": state.get("extracted_section")
    }

    state = await generate_intro(state)
    state = await refine_intro(state)
    # results["Refined_Intro"] = state["refined_intro"]

    state = await generate_guide(state)
    # results["Guide"] = state["guide"]

    state = await generate_issue_troubleshooting(state)
    # results["Issue_Troubleshoot"] = state['issue_troubleshoot']

    state = await generate_conclusion(state)
    # results["Conclusion"] = state["conclusion"]

    state = await generate_cta(state)
    # results["CTA"] = state["cta"]

    state = await generate_customization_tips(state)
    # results["Customization_Tips"] = state["customization_tips"]

    state["combined_data"] = {
        "introduction": state.get("refined_intro"),
        "guide": state.get("guide"),
        "issue_troubleshoot": state.get("issue_troubleshoot"),
        "conclusion": state.get("conclusion"),
        "cta": state.get("cta"),
        "customization_tips": state.get("customization_tips"),
    }

    state = await domain_aligned(state)
    # results["Domain_Aligned"] = state["domain_aligned_cta"]

    state = await rewrite_blog(state)
    results["Final_Blog"] = state["final_blog"]["Polished_Blog"]
    print(f"/n/n/n/n{results}")
    return results

@app.post("/run-pipeline")
async def run_pipeline(request: PipelineRequest):
    initial_state: SEOBlogGenerator = {
        "video_url": request.video_url,
        "domain_url": request.domain_url,
        "raw_blog": request.raw_blog,
        "video_id": None,
        "transcript": None,
        "topic_keyword": None,
        "specific_details": None,
        "introduction": None,
        "refined_intro": None,
        "guide": None,
        "issue_troubleshoot": None,
        "conclusion": None,
        "cta": None,
        "customization_tips": None,
        "domain_aligned": None,
        "final_blog": None
    }
    try:
        results = await full_pipeline(initial_state)
        return results
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
