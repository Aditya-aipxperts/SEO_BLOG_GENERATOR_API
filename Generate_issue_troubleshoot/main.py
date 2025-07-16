import json
import re
from typing import Dict
from setup_env import setup_environment,get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

async def generate_issue_troubleshooting(state: Dict) -> Dict:
    # with open ("combined_data1.json","r",encoding="utf-8") as f:
    #     combined_data = json.load(f)
    combined_data = state.get("combined_data_keyword_specific_details") or ""
    prompt = """
    Objective: Generate a detailed, actionable section focused on common issues and troubleshooting based on the provided YouTube video transcript. This section should be written after the customization tips section and should maintain the same structure, format, and writing style used in the previous content.

    Condition:

    * First, check if the video transcript contains relevant information on common issues and troubleshooting related to the [specific task/topic]. If the transcript does not include such content, return "Not Applicable."

    * If "Not Applicable" is returned, consider revisiting the transcript for other potential content or confirm that the task is complete.

    Instructions:

    Purpose:

    * Extract and deliver a comprehensive section focused on common issues that users may encounter during the [specific task/topic] and provide clear troubleshooting steps to resolve them. Allow for reasonable expansion or clarification where the transcript may lack detail, ensuring the guide remains practical and useful.

    * Ensure these troubleshooting tips are practical, offering actionable advice to help users overcome obstacles efficiently.

    Tasks:

    1. Identify Common Issues:

    * Analyze the transcript to identify any mentions of common issues or challenges users might face while performing the [specific task/topic].

    * Expand on these issues by providing additional context or potential causes, making it easier for users to identify and understand the problem. Where applicable, infer common issues based on the context provided in the transcript.

    2. Provide Troubleshooting Steps:

    * For each identified issue, provide clear, step-by-step troubleshooting instructions to help users resolve the problem.

    * Where applicable, offer alternative solutions or preventative tips to avoid the issue in the future. Include conditional logic where necessary to guide users through different troubleshooting paths based on the issue encountered.

    3. Expand on Examples:

    * If the transcript mentions specific examples of issues, integrate them into the section, providing additional context or variations that demonstrate different troubleshooting scenarios.

    * If the transcript lacks examples, infer possible issues and provide hypothetical troubleshooting steps that could apply to a variety of situations, ensuring these inferences are logically derived from the transcript.

    4. Use of Keywords:

    * Integrate primary keywords naturally within headings and key troubleshooting steps, ensuring their relevance to the content.

    * Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.

    5. Visual Prompts:

    * Suggest relevant visuals (e.g., screenshots, diagrams) where applicable to enhance understanding of the troubleshooting steps.

    * Provide detailed descriptions of what each visual should depict, allowing for the inclusion of visuals based on inferred needs if they support the accompanying text and enhance comprehension.

    6. Simplify Language:

    * Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience. Retain all critical details necessary for understanding while simplifying the language.

    7. Streamline Content:

    * Avoid redundant content by summarizing similar issues or combining them into more comprehensive advice where appropriate. Retain unique or contextually significant details to ensure different troubleshooting scenarios are adequately covered.

    8. Audit for Completeness:

    * Review the identified issues and troubleshooting steps against the transcript to ensure all relevant information is covered and no essential details are omitted.

    * Ensure the steps flow logically, are easy to understand, and provide real value to the reader, with adjustments made to enhance clarity and consistency with the overall guide.

    Keyword Integration:

    1. Primary Keywords:

    * Use primary keywords in H2 headings and key troubleshooting steps, ensuring they fit naturally within the content and align with the transcript.

    2. Secondary Keywords:

    * Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit, enhancing the content without overwhelming the reader.

    3. Avoid Over-Optimization:

    * Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.

    Examples:

    1. Integration:

    * Where examples of common issues and troubleshooting steps are provided in the transcript, integrate them into the section to illustrate key points or concepts.

    2. Modification:

    * Modify examples to avoid content cannibalism by changing names, numbers, and data to make them more relevant and original, while still adhering to the transcript.

    * Provide alternative scenarios or variations to demonstrate the flexibility of the troubleshooting steps, ensuring they are logically consistent with the transcript.

    Writing Style:

    1. Voice:

    * Maintain consistency with the writing style used in the previous sections. Use first-person or third-person, depending on the context.

    2. Tone:

    * Write in a tone suitable for a 7th-grade reading level, using simple, clear language.

    3. Structure:

    * Write short sentences (5-10 words) and use short paragraphs. Use appropriate headings (H2, H3, H4) to organize content logically.

    * Enhance readability by using bullet points, numbered lists, or tables where appropriate.

    4. Maintain Continuation:

    * Ensure a seamless transition from the previous section, keeping the content engaging and easy to follow.

    Output:

    1. Common Issues and Troubleshooting Section:

    * Generate a detailed, clear, and concise section that addresses common issues and provides practical troubleshooting steps related to the [specific task/topic].

    * Ensure the section is as long as necessary, incorporating examples, visuals, and best practices where needed, with flexibility for reasonable extrapolations or inferences based on the transcript.

    2. Audit:

    * Conduct a thorough review to ensure that all common issues and troubleshooting steps mentioned in the transcript are captured and that no essential details are omitted.

    * Ensure the content flows logically, with no gaps in the information provided, and is consistent with the overall guide.

    -> If no relevant troubleshooting content is found, output exactly this:

        {
        "status": "Not Applicable"
        }
    
    -> If relevant troubleshooting / issue is found, output exactly this:

        {
        "status": "Applicable",
        "section_title": "Common Issues & Troubleshooting",
        "issues": [
            {
            "title": "string – include primary keywords here",
            "description": "string",
            "troubleshooting_steps": ["string", ...],
            "preventative_tips": ["string", ...],
            "visual_prompts": [
                {
                "purpose": "string",
                "description": "string"
                }
            ],
            "example": {
                "transcript_excerpt": "string or null",
                "expanded_context": "string"
            }
            }
            /* More issues... */
        ]
        }
    
    """

    Full_Prompt = f"{prompt}\n\n{combined_data}"
    response = await llm.ainvoke(Full_Prompt)
    issue_troubleshoot = response.content.strip()
    issue_troubleshoot = re.sub(r'\s+', ' ', issue_troubleshoot).strip()
    if issue_troubleshoot.startswith("```json"):
        issue_troubleshoot = issue_troubleshoot.split("```json")[1].split("```")[0]
    if issue_troubleshoot.startswith("```"):
        issue_troubleshoot = issue_troubleshoot.split("```")[1]
    if issue_troubleshoot.endswith("```"):
        issue_troubleshoot = issue_troubleshoot.split("```")[0]
    if issue_troubleshoot.startswith("```json"):
        issue_troubleshoot = issue_troubleshoot.split("```json")[1].split("```")[0]

    data = json.loads(issue_troubleshoot)
    # with open("issue_troubleshoot.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    
    state["issue_troubleshoot"] = data
    return state