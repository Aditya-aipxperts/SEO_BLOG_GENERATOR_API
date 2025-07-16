import json
import re
from typing import Dict
from setup_env import setup_environment,get_gemini_flash_model

setup_environment()
llm = get_gemini_flash_model()

async def generate_intro(state: Dict) -> Dict:
    # with open("combined_data1.json", "r", encoding="utf-8") as f:
    #     state["combined_data"] = json.load(f)
    #     # combined_data = json.load(f)
    # combined_data = state["combined_data"]
    combined_data = state.get("combined_data_keyword_specific_details") or ""
    # combined_data = state.get("combined_data") or ""
    prompt = """
    Objective: Generate a compelling and SEO-optimized "Introduction" section for a blog post centered around "How to" guides and tutorials, based on the provided YouTube video transcript and inputs.



    Inputs:



    Primary Keywords

    Justification Primary

    Secondary Keywords

    Justification Secondary

    Video Topic

    Video Transcript

    Audience Specification

    Examples & References

    Conditional Logic Depth

    Error Handling

    Links and References



    Condition:



    Keyword Check: Ensure that the provided context includes specific "Primary Keywords" and "Secondary Keywords."

    Content Relevance: Confirm that the context aligns with the "Video Topic" and overall theme of the "How to" guide or tutorial blog post.

    Ignore Non-Applicable Inputs: If any of the input values are marked as "Not Applicable," ignore those specific inputs when generating the introduction.



    If the necessary elements are not present or aligned, return "Not Applicable" without additional details.

    Introduction Guidelines:



    1. Keyword Integration:



    Primary Keywords: Incorporate the primary keywords naturally to set the stage for the blog content without redundancy.

    Secondary Keywords: Introduce the secondary keywords seamlessly to support the introduction without overcrowding it.



    2. Relevance and Alignment:



    Ensure the introduction is aligned with the video topic, specifically focusing on the "How to" guide or tutorial theme, providing a clear and engaging preview of the content.



    3. Engage the Reader:



    Provide a concise and focused overview that hooks the reader by clearly outlining the value they will gain from following the tutorial or guide.



    4. Use of Transcript Details:



    Leverage relevant details from the video transcript to add credibility and depth, ensuring the content aligns with the step-by-step nature of "How to" guides and tutorials.



    5. Mention Tools or Resources:



    If applicable, mention any tools, setup instructions, or resources necessary for first-time users, as per the links and references provided. Include hyperlinks or references to these resources.



    Writing Style & Structure:



    1. Voice and Tone:



    Use a conversational tone suitable for a 7th-grade reading level, making the introduction feel personalized and engaging, ideal for "How to" guides and tutorials.



    2. Structure:



    Limit the introduction to three paragraphs, with 3-4 sentences in each paragraph.

    Each sentence should contain 5-10 words to ensure clarity and accessibility.

    Avoid clichés and use fresh, original language to keep the content engaging.

    Focus on clarity and avoid over-explaining concepts.



    3. Length:



    Keep the introduction concise, ensuring each sentence adds value and doesn’t repeat information unnecessarily.



    4. Flow:



    Ensure a seamless transition from the introduction to the main content, keeping the reader engaged and eager to follow the tutorial or guide.



    Output:



    1. Introduction Section:



    Generate a polished, concise, and SEO-optimized introduction tailored for a "How to" guide or tutorial blog post that effectively uses keywords, aligns with the video content, and guides first-time users through any necessary setup or sign-up processes.

    The introduction should be clear, focused, and engaging, setting the tone for the rest of the blog post.



    2. Examples (Templates):



    Example 1: "Are you struggling to keep your projects on track? This guide will show you how to create a project management plan that works. By following these simple steps, you'll ensure your team stays organized and meets deadlines. Let’s dive into the essentials of successful project management."



    Example 2: "Looking to streamline your data collection process? This tutorial will walk you through creating custom forms that suit your specific needs. With just a few clicks, you'll have a system in place that saves time and reduces errors. Get ready to transform the way you handle data!"

    STRICTLY DO NOT ADD EXPLANATION TO THE INTRO EXCEPT THE INTRO ITSELF.
    """


    prompt = f"{prompt}\n\n{json.dumps(combined_data, indent=2, ensure_ascii=False)}"

    response = await llm.ainvoke(prompt)  
    llm_output = response.content.strip()
    state["intro"] = llm_output
    return state


async def refine_intro(state: Dict) -> Dict:
    intro = state["intro"]
    
    prompt = """
    Refine and polish the provided text with a focus on improving originality, clarity, engagement, and accessibility. This task should be approached in two stages, each with specific goals:

    Stage 1: Content Enhancement

        Eliminate Clichés:

        Carefully identify and replace any overused or generic phrases, such as "Supercharge," "Unlock the power," and "take your [product/service] to the next level." These phrases should be substituted with more specific and original expressions that directly convey the benefits of your product or service.

        Avoid using vague or broad claims. Instead, focus on concrete, actionable benefits that the reader can immediately relate to and understand.

        Simplify Language for a 7th-Grade Reading Level:

        Review the text for any complex words or phrases. Simplify these to ensure the content is accessible to a broad audience, including those with a 7th-grade reading level.

        Each sentence should be concise, ideally between 5-10 words, with straightforward vocabulary that doesn't compromise the key message.

        Remove Redundancy:

        Examine the text for any repeated ideas, phrases, or concepts. Consolidate similar ideas into single, powerful statements to ensure that each sentence adds new and valuable information.

        Eliminate any repetitive explanations and ensure that the text flows logically without unnecessary duplication.

        Enhance Clarity and Focus:

        Ensure that each sentence directly contributes to the overall message of the introduction. Avoid any vague or ambiguous statements, and make sure the content remains on-topic throughout.

        Structure the introduction to provide a clear and logical preview of what the reader can expect from the guide, sticking to essential points that build on each other.

        Adjust Tone to Be More Personal and Conversational:

        Rephrase the text to create a direct, personal, and engaging tone. The goal is to make the reader feel as if they are being personally guided through the content.

        Use language that is approachable and relatable, transforming formal instructions into friendly advice. For example, replace "we'll show you" with "you'll learn," making the tone more conversational.

        Limit Length and Ensure Proper Structure:

        Keep the introduction concise and well-structured, adhering to a maximum of three paragraphs. Each paragraph should contain 3-4 sentences, and each sentence should be between 5-10 words long.

        Ensure that the introduction flows smoothly from one idea to the next, with a clear beginning (problem), middle (solution), and end (call to action).

        STRICTLY DO NOT ADD EXPLANATION TO THE INTRO EXCEPT THE INTRO ITSELF.

    Stage 2: Final Double-Check and Polish

        Refine and polish the provided text to enhance originality, clarity, engagement, and accessibility. This task should be approached in a single, comprehensive pass, with the following specific goals:

        1. Eliminate Clichés:

        Strictly Avoid Common Clichés: Carefully review the text to ensure it does not include any of the following overused phrases, which can weaken the originality and impact of the content:

        Game-changer
        Transform the way you work
        Unlock the full potential
        Take your productivity to new heights
        Leave no stone unturned
        Really help
        Change your [process/workflow]
        Boost your productivity
        Revolutionize your workflows
        Say goodbye to [problem], say hello to [solution]
        Make your [process] easier
        Simplify your workflow
        Improve how you [perform task]
        Make the most of
        Get the best results from
        Work well and look good
        Greatly help
        Maximize your efficiency
        Make [task] easy and efficient
        Get the most out of your [tool/product]

        Replace with Specific and Original Phrasing: Replace any identified clichés with specific, original language that is directly relevant to your product or service context. For example:

        Instead of "game-changer," use "valuable tool" or "effective solution."
        Replace "transform the way you work" with "simplify your daily tasks" or "optimize your workflow."
        Swap out "unlock the full potential" for "make the most of" or "get the best results from."

        Use Concrete and Descriptive Language: Ensure that every replacement is concrete and descriptive, adding new value to the text. For example:

        Rather than saying "change your process," say "improve how you handle [specific task]," which is more specific and actionable.

        Tailor to the Specific Context: Focus on language that directly references the actions and benefits related to your specific product or service. Avoid broad, non-specific phrases that could apply to any tool or situation, ensuring the content is highly relevant to the audience's needs.

        2. Simplify Language for a 7th-Grade Reading Level:

        Simplify Complex Words and Phrases: Review the text to replace any complex words or phrases with simpler alternatives. The content should be easily understood by a broad audience, including those at a 7th-grade reading level. For example:

        Instead of "utilize," use "use."
        Instead of "optimize," use "improve."

        Keep Sentences Concise: Aim for concise sentences that are ideally between 5-10 words long. Avoid long, complex sentences that could confuse the reader or make the text less accessible. For example:

        Instead of "By utilizing this tool, you can significantly streamline your process," use "This tool can simplify your process."

        Straightforward Vocabulary: Use straightforward vocabulary that conveys the message clearly without oversimplifying the content. Ensure that key points are communicated effectively and in a way that is easy to follow.

        3. Remove Redundancy:

        Consolidate Similar Ideas: Ensure that the text does not repeat ideas or phrases. For example, if the text mentions both "boosting productivity" and "streamlining workflows," consider merging these into one clear statement to avoid redundancy, such as "This tool helps you work more efficiently."

        Every Sentence Adds Value: Each sentence should contribute something new to the overall message. Avoid any repetitive explanations or statements that do not add fresh information to the introduction. Ensure that the introduction remains focused and concise.

        4. Enhance Clarity and Focus:

        Direct Contribution to the Message: Make sure that each sentence directly contributes to the main point of the introduction. Avoid vague or off-topic statements that could distract from the core message. For example:

        Instead of "This tool can change how you manage your work," specify "This tool makes managing your work faster and easier."

        Logical Structure: Structure the introduction in a way that provides a clear and logical preview of what the reader can expect from the guide. Start with the problem (e.g., current challenges), introduce the solution (e.g., your product/service), and conclude with the benefits the reader will gain (e.g., improved efficiency and ease of use).

        5. Adjust Tone to Be More Personal and Conversational:

        Friendly Guidance: Rephrase the text to create a more direct, personal, and engaging tone. The content should feel like friendly guidance rather than formal instructions. For example:

        Replace "We will show you" with "You'll learn how to."

        Engage the Reader Personally: Use language that makes the reader feel as though they are being personally guided through the content. For example, instead of "Users can benefit from this guide," say "You'll benefit from this guide."

        Avoid Overly Formal Language: Ensure that the language is approachable and avoids overly formal phrasing. Aim for a tone that feels inclusive and engaging, helping the reader feel connected to the content.

        6. Limit Length and Ensure Proper Structure:

        Concise and Well-Structured: Keep the introduction concise and well-structured. Adhere to a maximum of three paragraphs, with 3-4 sentences per paragraph. Ensure that the introduction is focused and flows smoothly.

        Flow from One Idea to the Next: Ensure a smooth flow from one idea to the next, with a clear beginning (identifying the problem), middle (introducing the solution), and end (highlighting the benefits and call to action). For example:

        Start with the challenge your target audience faces, introduce your product/service as the solution, and conclude with how it can make their work easier and more efficient.

        Sentence Length: Each sentence should be between 5-10 words long, ensuring that the text is easy to read and digest. For example:

        "This tool makes [task] simple." (5 words)

    Stage 3: Final Tone Adjustment

        Rewrite the 'Introduction' as if you're responding to a colleague in a friendly, natural, and human way. Keep the tone conversational and respectful, treating the readers as approachable colleagues—warm and friendly, but with clear boundaries. Use professional language that is not overly formal or corporate, avoiding any tone that might seem overly affectionate. Aim for a warm, chatty feel while staying authentic. Address any potential challenges or needs of the reader to make the content more relatable and engaging. If any mistakes or issues arise, provide a genuine apology and a clear solution. Ensure the final output resonates with your target audience, maintaining a natural and genuine conversational flow without feeling forced. Break up the content into smaller paragraphs for better readability, especially in an online context. The output should be only the 'Introduction' text, with no additional commentary or preamble.

        STRICTLY DO NOT ADD EXPLANATION TO THE INTRO EXCEPT THE INTRO ITSELF.
        GIVE ME IN THIS FORMAT:
        {
            "introduction":".."
        }

    """

    prompt = f"{prompt}\n\n{intro}"
    response = await llm.ainvoke(prompt)  
    refined_intro = response.content.strip()
    refined_intro = re.sub(r'\s+', ' ', refined_intro).strip()
    if refined_intro.startswith("```json"):
        refined_intro = refined_intro.split("```json")[1].split("```")[0]
    if refined_intro.startswith("```"):
        refined_intro = refined_intro.split("```")[1]
    if refined_intro.endswith("```"):
        refined_intro = refined_intro.split("```")[0]
    if refined_intro.startswith("```json"):
        refined_intro = refined_intro.split("```json")[1].split("```")[0]

    print("LLM OUTPUT:", repr(refined_intro))
    if not refined_intro:
        print("refine_intro: No output received to parse as JSON.")
        raise ValueError("refine_intro: No output received to parse as JSON.")
    try:
        data = json.loads(refined_intro)
    except Exception as e:
        # print("JSON decode error:", e)
        print("refine_intro: JSON decode error:", e)
        print("refine_intro: Output was:", repr(refined_intro))
        raise

    # with open("intro.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    
    state["refined_intro"] = data
    return state