import re
import json
from typing import Dict
from setup_env import setup_environment, get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

async def generate_cta(state: Dict) -> Dict:
    # with open("combined_data1.json","r",encoding="utf-8") as f:
    #     combined_data = json.load(f)
    combined_data = state.get("combined_data_keyword_specific_details") or ""
    prompt = """
    Objective: Generate a compelling and action-oriented "Call to Action" (CTA) section that encourages the reader to engage further with the content. The CTA should be based on the provided YouTube video transcript and integrate primary and secondary keywords naturally. This section should focus on prompting the reader to take specific actions without including any general introductory content.

    Condition: First, check if the video transcript contains relevant content that can be used to craft a CTA related to the [specific task/topic]. If the transcript does not include such content, simply return "Not Applicable" without any additional details.

    If the transcript includes relevant content, proceed with the following steps:

    Instructions:

    1. Purpose:

    * Prompt the reader to engage further with the content by exploring related articles, signing up for a service, or applying what they’ve learned. The CTA should be direct, persuasive, and motivating.

    2. Tasks:

    * Engage: Encourage the reader to take a specific action, such as reading more related content, signing up for a service, or applying the knowledge gained.

    * Link: Provide relevant links that cta the reader to the next step. Use internal links to related articles or external links to sign-up pages or tools that support the CTA.

    3. Structure:

    * Action Prompt: Start with a direct and clear call to action that uses action-oriented language. For example, "Explore more about [specific topic] by visiting our other guides."

    * Link: Include a relevant link to internal content that enhances the reader’s understanding or to an external resource that provides further value.

    * Limit CTAs: Focus on one or two CTAs to keep the message clear and impactful.

    4. Keyword Integration:

    * Primary Keywords: Incorporate the primary keyword naturally within the CTA. It should be relevant and guide the reader to useful next steps.

    * Secondary Keywords: Use secondary keywords to provide additional context or detail where they naturally fit, ensuring they complement the primary keyword and enhance the CTA.

    5. Writing Style:

    * Voice: Use first-person and action-oriented language. The tone should be persuasive, motivating, and encourage immediate action.

    * Clarity: Keep the CTA short, clear, and to the point. Avoid unnecessary words or phrases that could dilute the impact.

    * Avoid Over-Optimization: Focus on making the CTA feel natural and engaging, not forced or overly commercial.

    Output:

    1. Call to Action Section: Generate a concise, engaging CTA that directs the reader to the next steps. The CTA should include a strong action prompt and relevant links, encouraging further engagement without feeling overly pushy. Limit the CTA to one or two key actions to maintain focus and effectiveness.

    Example:

    * Action Prompt: Ready to take your [specific task/topic] to the next level? Dive deeper into our [related content] or sign up for [service/tool] to start implementing these strategies today.

    * Link: ...(internal link to related articles).

    * Return valid JSON only (no extra text), using this schema:

        {
        "call_to_action": "string – summary of next step"
        }

    """

    Full_prompt = f"{prompt}\n\n{combined_data}"
    response = await llm.ainvoke(Full_prompt)
    cta = response.content.strip()

    cta = re.sub(r'\s+', ' ', cta).strip()
    if cta.startswith("```json"):
        cta = cta.split("```json")[1].split("```")[0]
    if cta.startswith("```"):
        cta = cta.split("```")[1]
    if cta.endswith("```"):
        cta = cta.split("```")[0]
    if cta.startswith("```json"):
        cta = cta.split("```json")[1].split("```")[0]

    data = json.loads(cta)
    # with open("CTA.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    
    state["cta"] = data
    return state