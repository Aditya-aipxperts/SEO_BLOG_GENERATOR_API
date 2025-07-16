from setup_env import setup_environment, get_gemini_flash_model
import asyncio
import json
import re
from typing import Dict

setup_environment()
llm = get_gemini_flash_model()

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

async def rewrite_blog(state: Dict) -> Dict:
    # data = {
    #     "domain_aligned_cta": state.get("domain_aligned_cta"),
    #     "introduction": state.get("refined_intro"),
    #     "guide": state.get("guide"),
    #     "customization_tips": state.get("customization_tips"),
    #     "issue_troubleshoot": state.get("issue_troubleshoot"),
    #     "conclusion": state.get("conclusion"),
    #     "cta": state.get("cta"),
    #     "raw_blog": state.get("raw_blog"),
    #     "topic_keyword": state.get("extracted_keywords"),
    #     "specific_details": state.get("extracted_section"),
    # }
    combined_data = {}
    combined_data.update(state.get("combined_data_keyword_specific_details"))
    combined_data.update(state.get("combined_data"))
    combined_data.update(state.get("domain_aligned_cta"))
    print("Merged combined_data for LLM:", json.dumps(combined_data, indent=2, ensure_ascii=False))
    print("Data sent to LLM for final blog:", json.dumps(combined_data, indent=2, ensure_ascii=False))
    prompt = """
    Objective: Generate a comprehensive, cohesive, and detailed blog post using the provided key inputs. The blog should seamlessly integrate all sections while maintaining the depth, length, and clarity of the content.

    Inputs:

    * Raw Text Content: Includes an introduction, step-by-step guide, customization tips, issues and troubleshooting, conclusion, and CTAs. This content is detailed but may have disjointed sections due to being generated from various prompts.

    * Tutorial-Specific Service Overview: A summary of services specifically related to the tutorial content, including references to the domain name.

    * Comprehensive Service Summary: A broad overview of the company's key services and areas of expertise, especially in relation to project management tools or relevant products.

    * Domain Name: The name of the website where the blog will be published, reflecting the company’s brand and services.

    Objectives:

    1. Preserve Length and Detail:

    * Maintain the richness and length of the content provided. Every detail is important, and no information should be lost or overly condensed during the rewriting process.

    * Include all raw content provided, ensuring that every section retains its original depth and detail.

    2. Ensure Cohesive Flow and Transitions:

    * Seamlessly integrate and connect each section of the blog to create a smooth and logical flow from one part to the next. Use linking sentences or transitional paragraphs that connect ideas without reducing content.

    * Ensure that transitions add to the content, enhancing the reader’s understanding while maintaining the length and detail of the original material.

    3. Seamless Integration of Services:

    * Ensure that the "Tutorial-Specific Service Overview" and "Comprehensive Service Summary" are seamlessly integrated throughout the blog. References to the company’s expertise and services should be woven into relevant sections, such as customization tips and troubleshooting, while retaining the full detail of each section.

    * Highlight how the company’s services enhance each aspect of the tutorial, subtly promoting the offerings without reducing the content’s depth.

    4. Increased Personalization and Engagement:

    * Maintain an engaging and conversational tone, particularly in the introduction and CTAs. Personalize the content to make it more relatable to the reader, using language that connects with the audience.

    * Ensure that personalized content enhances the reader’s experience without simplifying or reducing the content’s richness.

    5. Detailed Examples in Customization Tips:

    * In the customization tips section, provide specific examples of how the company has helped clients with similar customization needs. These examples should add to the content, not replace broader advice or other details.

    * Include both general tips and specific examples to maintain the section’s full length and richness.

    6. Consistent and Subtle Branding Throughout:

    * Incorporate the domain name and branding references consistently and subtly throughout the blog. Ensure that these references enhance the content without reducing its length.

    * Rather than isolating branding mentions at the end, integrate the domain name naturally into the content while maintaining the detail and depth of each section.

    Desired Output:

    A comprehensive, polished blog post that includes:

    1. Introduction:

    * Engages the reader with a clear and compelling introduction that sets the context for the guide.

    * Ensure the introduction retains all provided details and sets the tone for the rest of the blog.

    2. Step-by-Step Guide:

    * Presents detailed instructions in a logical, easy-to-follow format using numbered steps and bullet points.

    * Maintain the full length and depth of the step-by-step guide, ensuring all steps are thoroughly explained.

    3. Customization Tips:

    * Offers practical advice on how to customize relevant tools or platforms with clear, actionable tips that enhance both visual and functional aspects.

    * Include specific examples of how the company has helped clients, while also providing broader advice to ensure the section is comprehensive and detailed.

    4. Troubleshooting Section:

    * Clearly identifies common issues and provides step-by-step solutions, organized in a user-friendly manner.

    * Ensure all provided troubleshooting tips are included, with no reduction in detail or length.

    5. Conclusion:

    * Summarizes the key takeaways and reinforces the benefits of using the tools or platforms discussed.

    * Maintain the full length of the conclusion, ensuring it effectively wraps up the blog and reinforces the overall message.

    6. CTAs:

    * Provides well-aligned CTAs that guide the reader towards relevant services and next steps, ensuring they are actionable and directly tied to the "Tutorial-Specific Service Overview."

    * Ensure CTAs are personalized and engaging, with no reduction in their detail or impact.

    7. Consistent Branding and Theme:

    * Integrates references to the "Comprehensive Service Summary" and the domain name throughout the blog, ensuring the content is aligned with the company's broader service offerings and maintains consistent branding.

    * Ensure branding is woven into the content naturally, without reducing the blog's length or detail.

    * STRICTLY DO NOT ADD ANY EXPLANATION OTHER THAN THE Blog Post Content. The content should be polished and ready for publishing.

    * Return strictly valid JSON only, matching this schema:

    {
        "Polished_Blog" : "..."
    }

    """
    Full_prompt = f"{prompt}\n\n{json.dumps(combined_data, indent=2, ensure_ascii=False)}"
    response = await llm.ainvoke(Full_prompt)
    Blog = response.content.strip()
    # print(Blog)
    Blog = re.sub(r'\s+', ' ', Blog).strip()
    if Blog.startswith("```json"):
        Blog = Blog.split("```json")[1].split("```")[0]
    if Blog.startswith("```"):
        Blog = Blog.split("```")[1]
    if Blog.endswith("```"):
        Blog = Blog.split("```")[0]
    if Blog.startswith("```json"):
        Blog = Blog.split("```json")[1].split("```")[0]
    # Escape all backslashes to prevent invalid escape errors
    Blog = Blog.replace('\\', '\\\\')
    try:
        data = json.loads(Blog)
    except Exception as e:
        print("rewrite_blog: JSON decode error:", e)
        print("rewrite_blog: Output was:", repr(Blog))
        raise
    # with open ("FINAL_BLOG.json","w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    
    state["final_blog"] = data
    return state



if __name__ == "__main__":
    asyncio.run(rewrite_blog())