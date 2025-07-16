import json
import re
from typing import Dict
from setup_env import setup_environment,get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

async def generate_conclusion(state: Dict) -> Dict:
    # with open("combined_data1.json","r",encoding="utf-8") as f:
    #     combined_data = json.load(f)
    combined_data = state.get("combined_data_keyword_specific_details") or ""
    prompt = """
    Objective: Generate a concise, impactful conclusion for a blog post about [specific task/topic]. The conclusion should summarize the key points discussed in the blog and reinforce the value of the content. This section should be based on the provided YouTube video transcript, with an emphasis on integrating primary and secondary keywords naturally. Avoid any unnecessary repetition or overly general content.



    Condition:



    First, check if the video transcript contains relevant content that can be summarized in a conclusion for a blog post about [specific task/topic]. If the transcript does not include such content, return "Not Applicable."

    If "Not Applicable" is returned, consider revisiting the transcript for other potential content that could be repurposed for a conclusion or confirm that the task is complete.



    Instructions:

    Purpose:



    Summarize the key points covered in the blog, reinforcing the value of the content for the reader. Focus on the most impactful points that align with the blog’s main message.



    Tasks:



    Recap:

    Summarize the main benefits and key takeaways from the [specific task/topic] discussed in the video. The summary should be concise and focused, ensuring that the reader remembers the most important aspects of the blog. Allow for flexibility in selecting the most relevant points if the transcript covers multiple aspects.



    Structure:

    Provide a brief recap of the blog’s main points. Highlight the key benefits of the techniques or information discussed in the blog, ensuring the conclusion reinforces the overall message.

    Avoid introducing new content. Focus solely on summarizing what was covered in the blog.



    Keyword Integration:



    Primary Keywords:

    Use primary keywords naturally within the summary to reinforce the main topic without overstuffing. Ensure they fit seamlessly into the content, prioritizing readability and natural flow.



    Secondary Keywords:

    Integrate secondary keywords where they naturally fit, enhancing the relevance of the conclusion without overwhelming the reader.



    Avoid Over-Optimization:

    Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.



    Writing Style:



    Voice:

    Write in the first person or third person, using the past tense where applicable.

    Ensure consistency with the tone and style used throughout the blog.



    Tone:

    Be concise and avoid mentioning ‘today’ to keep the content timeless.

    Maintain an engaging tone that encourages the reader to reflect on what they’ve learned and how it benefits them.



    Clarity:

    Use short sentences (5-10 words) and short paragraphs to ensure the summary is clear and easy to read.



    Focus:

    Reiterate the primary keyword to ensure the reader feels confident about the topic. The tone should be reflective, reinforcing the value of the content and what the reader has learned.



    Output:



    Conclusion Section:

    Generate a concise, clear, and well-structured conclusion that effectively summarizes the blog's content. Avoid any introductory or new content, focusing solely on recapping what was covered.

    Ensure the conclusion aligns with the blog's overall tone and message, leaving the reader with a strong understanding of the key takeaways.



    Audit:

    Review the conclusion to ensure it effectively summarizes the key points from the blog without unnecessary repetition or new content.

    Ensure the conclusion flows logically, reinforces the blog’s message, and provides a strong, impactful end to the post.

    STRICTLY DO NOT ADD ANY EXPLANATION OTHER THAN THE CONCLUSION.

    Return strictly valid JSON only, matching this format (no extra text):

        {
        "conclusion": "string – concise wrap‑up of key ideas"
        }

    """

    Full_prompt = f"{prompt}\n\n{combined_data}"
    response = await llm.ainvoke(Full_prompt)
    conclusion = response.content.strip()
    # print(conclusion)
    conclusion = re.sub(r'\s+', ' ', conclusion).strip()
    if conclusion.startswith("```json"):
        conclusion = conclusion.split("```json")[1].split("```")[0]
    if conclusion.startswith("```"):
        conclusion = conclusion.split("```")[1]
    if conclusion.endswith("```"):
        conclusion = conclusion.split("```")[0]
    if conclusion.startswith("```json"):
        conclusion = conclusion.split("```json")[1].split("```")[0]
   
    data = json.loads(conclusion)
    # with open ("Conclusion.json","w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    state["conclusion"] = data
    return state