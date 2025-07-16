import json
import re
from typing import Dict
from setup_env import setup_environment,get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

async def generate_guide(state: Dict) -> Dict:
    combined_data = state.get("combined_data_keyword_specific_details")
    # if not combined_data:
    #     with open("combined_data1.json", "r", encoding="utf-8") as f:
    #         combined_data = json.load(f)
    prompt = """
    Objective: Generate a comprehensive, actionable, and detailed step-by-step guide for creating a [specific task/topic] based on the provided YouTube video transcript. The guide should naturally integrate primary and secondary keywords, reflect the context and justification provided, and be structured with appropriate headings. Ensure that all content remains grounded in the transcript, with minor extrapolation allowed to enhance clarity, context, and user understanding.

    Instructions:

    Purpose:    



    Deliver a thorough and detailed guide for completing the [specific task/topic] covered in the video, ensuring each step is clearly explained and directly derived from the transcript.

    Incorporate best practices and actionable tips within the steps to enhance the user's workflow and comprehension.

    If conditional logic or examples are mentioned, include practical, easy-to-follow examples. If not discussed in the transcript, consider adding relevant logical steps or examples if they enhance clarity.



    Tasks:



    Outline Steps:

    Sequentially list all necessary steps to complete the task, ensuring each step is thoroughly grounded in the transcript. Break down complex tasks into detailed sub-steps, providing clear instructions for each part of the process.

    Include any contextual information or justifications provided in the transcript to explain why each step is important.

    Integrate best practices naturally within the steps, offering actionable tips that are embedded in the workflow. Ensure these are either mentioned or implied in the transcript or logically derived from the context.

    Verification: Continuously verify that each step and example is supported by the transcript. Add necessary details to enhance the guide’s usefulness without straying from the transcript’s content.



    Incorporate Context:

    Use the context of the video topic and any justifications provided in the transcript to ensure the content is relevant and aligned with the video’s focus.

    Provide brief explanations or context where necessary to improve user understanding, ensuring these additions support the instructions and are consistent with the transcript.



    Use of Keywords:

    Integrate primary keywords naturally within headings and key instructions, ensuring their relevance to the step being described.

    Use secondary keywords to provide additional context and depth, ensuring these keywords are relevant and align with the transcript.



    Avoid Keyword Overuse:

    Maintain natural readability by limiting the repetition of keywords. Use synonyms or rephrase content where necessary to avoid over-optimization, ensuring all language remains consistent with the transcript.



    Visual Prompts:

    Include relevant visuals (e.g., screenshots) where applicable to enhance understanding. If the transcript does not explicitly reference visuals, feel free to incorporate them where they would aid comprehension. Specify how these visuals should be incorporated (e.g., callouts, inline, or separate sections).



    Simplify Language:

    Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience. Balance simplicity with sufficient detail to ensure all necessary information is included.



    Streamline Redundant Content:

    Summarize repetitive steps to avoid unnecessary detail, ensuring the content remains clear but concise. However, ensure that all critical information and context are retained.



    Provide Conditional Logic Examples:

    If the transcript includes conditional logic, provide step-by-step examples detailing how to apply it within the task. If not mentioned but relevant, consider including logical steps that enhance the user's understanding, ensuring they are practical and contextually appropriate.



    Handling Unclear or Missing Information:

    If the transcript is unclear or lacks specific details, note these areas and provide reasonable, context-based extrapolations to fill gaps. Avoid introducing any external knowledge that is not aligned with the transcript’s content.



    Heading Structure:



    Use H2 for major sections or key steps in the process.

    Use H3 for sub-steps or detailed actions within a major step.

    Use H4 for minor details or specific elements within a sub-step.

    Allow flexibility in structure to ensure the guide flows logically and is easy to follow.



    Audit for Completeness:



    Review the guide against the transcript to ensure all steps are covered and no essential details are omitted. Ensure the content flows logically and naturally, allowing for minor additions that enhance clarity and user understanding.



    Incorporate Feedback or Revisions:



    If provided with feedback or revisions, integrate these into the guide while ensuring all content remains grounded in the transcript.



    Keyword Integration:



    Primary Keywords:

    Use primary keywords in H2 headings and key instructions, ensuring they fit naturally within the content and are supported by the transcript.



    Secondary Keywords:

    Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit, ensuring these are relevant and derived from the transcript.



    Avoid Over-Optimization:

    Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary, ensuring everything remains consistent with the transcript.



    Examples:



    Integration:

    Where examples are provided in the transcript, integrate them into the guide to illustrate key steps or concepts. If not explicitly provided, consider adding relevant examples that enhance the guide’s clarity.



    Modification:

    Modify examples to avoid content cannibalism by changing names, numbers, and data to make them more relevant and original, while still adhering to the transcript.



    Example Instruction:

    For instance, if the transcript includes an example using "John Doe" in a form, replace it with a more contextually relevant name like "Jane Smith" and adjust the associated data accordingly.



    Writing Style:



    Voice:

    Maintain consistency with the writing style from previous sections. Use first-person or third-person, depending on the context, ensuring consistency with the transcript.



    Tone:

    Write in a tone suitable for a 7th-grade reading level, using simple, clear language that aligns with the transcript.



    Structure:

    Write short sentences (5-10 words) and use short paragraphs. Use appropriate headings (H2, H3, H4) to organize content logically.



    Maintain Continuation:

    Ensure a seamless flow from previous sections. Content should be easy to follow and engaging without feeling overly technical or repetitive, and should align with the transcript’s structure.



    Output:



    Step-by-Step Guide:

    Generate a detailed, clear, and comprehensive step-by-step guide that helps the reader complete the task, based on the transcript but with flexibility for necessary enhancements. The guide should be as long as necessary, incorporating visuals, examples, modified data, and best practices where needed, all derived from or aligned with the transcript.

    Ensure that each step is detailed and thorough, breaking down complex tasks into sub-steps and including explanations where necessary to aid user understanding.



    Audit:

    Conduct a thorough review to ensure that all steps mentioned in the transcript are captured and that no essential details are omitted. Ensure the content flows logically, with minor enhancements allowed to improve clarity and completeness.

    STRICTLY DO NOT ADD ANY EXPLANATION OTHER THAN THE GUIDE.

    ### Output Format:
    Return only valid JSON matching this schema (no extra text):

    {
    "title": "string",
    "overview": "string",
    "sections": [
        {
        "title": "string",
        "subsections": [
            {
            "title": "string",
            "content": "string"
            },
            ...
        ]
        },
        ...
    ]
    }

    """

    Prompt = f"{prompt}\n\n{combined_data}"
    response = await llm.ainvoke(Prompt)
    Guide = response.content.strip()
    Guide = re.sub(r'\s+', ' ', Guide).strip()
    if Guide.startswith("```json"):
        Guide = Guide.split("```json")[1].split("```")[0]
    if Guide.startswith("```"):
        Guide = Guide.split("```")[1]
    if Guide.endswith("```"):
        Guide = Guide.split("```")[0]
    if Guide.startswith("```json"):
        Guide = Guide.split("```json")[1].split("```")[0]

    data = json.loads(Guide)
    # with open("Guide.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)

    state["guide"]=data
    return state