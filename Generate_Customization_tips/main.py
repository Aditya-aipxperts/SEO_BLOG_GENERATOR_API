import re
import json
from typing import Dict
from setup_env import setup_environment, get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

async def generate_customization_tips(state: Dict) -> Dict:
    # with open("combined_data1.json","r",encoding="utf-8") as f:
    #     combined_data = json.load(f)
    combined_data = state.get("combined_data_keyword_specific_details") or ""
    prompt = """
    Objective: Generate a detailed, actionable section focused on extracting and presenting customization tips based on the provided YouTube video transcript. This section should follow the step-by-step guide, seamlessly maintaining the structure, format, and writing style used in the earlier content.

    Condition:

    * First, check if the video transcript contains relevant information on customization tips related to the [specific task/topic]. If the transcript does not include such content, return "Not Applicable." If customization tips are found, proceed with the following steps.

    * If "Not Applicable" is returned, consider revisiting the transcript for other potential content or confirm that the task is complete.

    Instructions:

    Purpose:

    * Extract and deliver a comprehensive section focused on customization tips to enhance the [specific task/topic] discussed in the video.

    * Ensure these tips are directly applicable, offering actionable advice on how to personalize or optimize the process to suit different needs or preferences. Allow for reasonable expansion or clarification where the transcript may lack detail, ensuring the guide remains practical and useful.

    Tasks:

    1. Identify Customization Opportunities:

    * Carefully analyze the transcript to identify any mentions of customization, personalization, or optimization opportunities related to the [specific task/topic].

    * Expand on these mentions by providing additional context or actionable steps, ensuring they are grounded in the transcript’s content and logically inferred if necessary.

    2. Integrate Customization Tips:

    * Organize the customization tips into a structured section that flows naturally from the step-by-step guide, maintaining consistency in tone and format.

    * Include detailed instructions or sub-steps where necessary, ensuring each customization tip is easy to follow and implement without sacrificing clarity.

    3. Expand on Examples:

    * Where examples of customization are mentioned in the transcript, integrate them into the section, providing additional context or variations that demonstrate the versatility of the tips.

    * If the transcript lacks examples, infer possible scenarios where these customizations could be applied, ensuring these inferences are logically derived from the transcript and contextually appropriate.

    4. Use of Keywords:

    * Integrate primary keywords naturally within headings and key customization tips, ensuring their relevance to the content.

    * Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.

    5. Visual Prompts:

    * Suggest relevant visuals (e.g., screenshots, diagrams) where applicable to enhance understanding of the customization tips.

    * Provide detailed descriptions of what each visual should depict, and allow for the inclusion of visuals based on inferred needs if they support the accompanying text and enhance comprehension.

    6. Simplify Language:

    * Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience. Ensure that simplification does not omit critical details necessary for understanding.

    7. Streamline Content:

    * Avoid redundant content by summarizing similar customization tips or combining them into more comprehensive advice where appropriate. Retain unique or contextually significant details to ensure different customization scenarios are adequately covered.

    8. Audit for Completeness:

    * Review the extracted tips against the transcript to ensure all relevant customization opportunities are covered and no essential details are omitted.

    * Ensure the tips flow logically, are easy to understand, and provide real value to the reader, with adjustments made to enhance clarity and consistency with the overall guide.

    Keyword Integration:

    1. Primary Keywords:

    * Use primary keywords in H2 headings and key customization tips, ensuring they fit naturally within the content and align with the transcript.

    2. Secondary Keywords:

    * Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit, enhancing the content without overwhelming the reader.

    3. Avoid Over-Optimization:

    * Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.

    Examples:

    1. Integration:

    * Where examples of customization are provided in the transcript, integrate them into the section to illustrate key tips or concepts.

    2. Modification:

    * Modify examples to avoid content cannibalism by changing names, numbers, and data to make them more relevant and original, while still adhering to the transcript.

    * Provide alternative scenarios or variations to demonstrate the flexibility of the customization tips, ensuring they are logically consistent with the transcript.

    Writing Style:

    1. Voice:

    * Maintain consistency with the writing style used in the step-by-step guide. Use first-person or third-person, depending on the context.

    2. Tone:

    * Write in a tone suitable for a 7th-grade reading level, using simple, clear language.

    3. Structure:

    * Write short sentences (5-10 words) and use short paragraphs. Use appropriate headings (H2, H3, H4) to organize content logically.

    * Enhance readability by using bullet points, numbered lists, or tables where appropriate.

    4. Maintain Continuation:

    * Ensure a seamless transition from the previous section, keeping the content engaging and easy to follow.

    Output:

    1. Customization Tips Section:

    * Generate a detailed, clear, and concise section that provides practical customization tips related to the [specific task/topic].

    * Ensure the section is as long as necessary, incorporating examples, visuals, and best practices where needed, with flexibility for reasonable extrapolations or inferences based on the transcript.

    2. Audit:

    * Conduct a thorough review to ensure that all customization tips mentioned in the transcript are captured and that no essential details are omitted.

    * Ensure the content flows logically, with no gaps in the information provided, and is consistent with the overall guide.

    * If Customization Tips are applicable then return in this format:

        Return strictly valid JSON only (no extra text), following this schema:

            {
            "status": "Applicable",   // or "Not Applicable" if no tips found
            "section_title": "Customization Tips",
            "tips": [
                {
                "title": "string – include primary keyword",
                "description": "string – what the customization does",
                "steps": ["string", ...],           // actionable steps to apply the tip
                "example": {
                    "transcript_excerpt": "string or null",
                    "expanded_context": "string"
                },
                "visual_prompt": {
                    "purpose": "string – why this visual helps",
                    "description": "string – what the image/diagram should show"
                }
                }
                // ... more tips
            ]
            }
    
    * If Customization Tips are NOT APPLICABLE then return in this format:

        {
        "status": "Not Applicable"
        }
            """

    Full_prompt = f"{prompt}\n\n{combined_data}"
    response = await llm.ainvoke(Full_prompt)
    customization_tips = response.content.strip()
    # print(customization_tips)

    customization_tips = re.sub(r'\s+', ' ', customization_tips).strip()
    if customization_tips.startswith("```json"):
        customization_tips = customization_tips.split("```json")[1].split("```")[0]
    if customization_tips.startswith("```"):
        customization_tips = customization_tips.split("```")[1]
    if customization_tips.endswith("```"):
        customization_tips = customization_tips.split("```")[0]
    if customization_tips.startswith("```json"):
        customization_tips = customization_tips.split("```json")[1].split("```")[0]

    data = json.loads(customization_tips)
    # with open("Customization_Tips.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    
    state["customization_tips"] = data
    return state
