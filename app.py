import streamlit as st
import asyncio
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
from typing import Dict
from schemas import SEOBlogGenerator

import json
import re

def extract_video_id(state: Dict)-> Dict:
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", video_url)
    if match:
        state["video_id"]=match.group(1)
        return state
    raise ValueError("Could not extract video ID from URL")

async def full_pipeline(state: Dict) -> Dict:
    video_url=state.get("video_url") or ""
    domain_url=state.get("domain_url") or ""
    raw_blog=state.get("raw_blog") or ""

    video_id = extract_video_id(state)
    transcript = get_transcript_with_backoff(state)
    if not transcript or "Failed after multiple retries" in transcript:
        return {"error": f"Transcript not available for: {video_url}"}
    results = {"Transcript": transcript}
    state["transcript"] = transcript

    specific_details = await extract_specific_details(state)
    results["Specific Details"] = state["extracted_section"]

    topic_keyword = await generate_topic_keyword(state)
    results["Topic Keyword"] = state["extracted_keywords"]

    # Now write combined_data1.json, after both are available
    # combined_data1 = {
    #     "topic_keyword": state.get("extracted_keywords"),
    #     "specific_details": state.get("extracted_section"),
    # }
    # with open("combined_data1.json", "w", encoding="utf-8") as f:
    #     json.dump(combined_data1, f, indent=2, ensure_ascii=False)

    # Build combined_data dynamically from current state
    state["combined_data_keyword_specific_details"] = {
        "topic_keyword": state.get("extracted_keywords"),
        "specific_details": state.get("extracted_section")
    }

    state = await generate_intro(state)
    print('After generate_intro, state type:', type(state))
    state = await refine_intro(state)
    print('After refine_intro, state type:', type(state))
    results["Refined Intro"] = state["refined_intro"]

    state = await generate_guide(state)
    print('After generate_guide')
    results["Guide"] = state["guide"]
    # state["guide"] = guide

    state = await generate_issue_troubleshooting(state)
    print('After generate_issue_troubleshooting')
    results["Issue Troubleshoot"] = state['issue_troubleshoot']
    # state["issue_troubleshoot"] = issue_troubleshoot

    state = await generate_conclusion(state)
    print('After generate_conclusion')
    results["Conclusion"] = state["conclusion"]
    # state["conclusion"] = conclusion

    state = await generate_cta(state)
    print('After generate_cta')
    results["CTA"] = state["cta"]
    # state["cta"] = cta

    state = await generate_customization_tips(state)
    print('After generate_customization_tips')
    results["Customization Tips"] = state["customization_tips"]
    # state["customization_tips"] = customization_tips

    # Write combined_data2.json after generating all main sections
    state["combined_data"] = {
        "introduction": state.get("refined_intro"),
        "guide": state.get("guide"),
        "issue_troubleshoot": state.get("issue_troubleshoot"),
        "conclusion": state.get("conclusion"),
        "cta": state.get("cta"),
        "customization_tips": state.get("customization_tips"),
    }
    # with open("combined_data2.json", "w", encoding="utf-8") as f:
    #     json.dump(combined_data2, f, indent=2, ensure_ascii=False)

    state = await domain_aligned(state)
    print('After domain_aligned')
    results["Domain Aligned"] = state["domain_aligned_cta"]
    # Write combined_data3.json after domain aligned
    # combined_data3 = state.get("domain_aligned_cta")
    # with open("combined_data3.json", "w", encoding="utf-8") as f:
    #     json.dump(combined_data3, f, indent=2, ensure_ascii=False)

    state = await rewrite_blog(state)
    print('After rewrite_blog, blog type:', type(state))
    results["Final Blog"] = state["final_blog"]
    # state["final_blog"] = blog
    print('At end of pipeline, state type:', type(state))

    return results

def run_async_pipeline(video_url, domain_url, raw_blog):
    initial_state: SEOBlogGenerator = {
        "video_url": video_url,
        "domain_url": domain_url,
        "raw_blog": raw_blog,
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
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    if loop.is_running():
        # If already running (e.g., in Streamlit), use create_task and run_until_complete
        task = loop.create_task(full_pipeline(initial_state))
        return asyncio.run_coroutine_threadsafe(task, loop).result()
    else:
        return loop.run_until_complete(full_pipeline(initial_state))

# Streamlit UI
st.title("SEO Blog Generator")

video_url = st.text_input("Enter the YouTube video URL:")
domain_url = st.text_input("Enter your Domain URL:")
raw_blog = st.text_area("Enter the raw blog:")

if st.button("Run Pipeline"):
    with st.spinner("Processing..."):
        try:
            results = run_async_pipeline(video_url, domain_url, raw_blog)
            if "error" in results:
                st.error(results["error"])
            else:
                st.success("Pipeline completed!")
                st.subheader("Transcript")
                st.code(results["Transcript"])
                st.subheader("Specific Details")
                st.json(results["Specific Details"])
                st.subheader("Topic Keyword")
                st.json(results["Topic Keyword"])
                st.subheader("Refined Intro")
                st.json(results["Refined Intro"])
                st.subheader("Guide")
                st.json(results["Guide"])
                st.subheader("Issue Troubleshoot")
                st.json(results["Issue Troubleshoot"])
                st.subheader("Conclusion")
                st.json(results["Conclusion"])
                st.subheader("CTA")
                st.json(results["CTA"])
                st.subheader("Customization Tips")
                st.json(results["Customization Tips"])
                st.subheader("Domain Aligned")
                st.write(results["Domain Aligned"])
                st.subheader("Final Blog")
                st.write(results["Final Blog"])
        except Exception as e:
            st.error(f"Error: {e}")
