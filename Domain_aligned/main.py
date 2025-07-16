import json
import re
from typing import Dict
import asyncio
from setup_env import setup_environment, get_gemini_flash_model
from mcp_use import MCPAgent, MCPClient



setup_environment()
llm = get_gemini_flash_model()

config = {
        "mcpServers": {
            "mcp-server-firecrawl": {
                "command": "npx",
                "args": ["-y", "firecrawl-mcp"],
                "env": {
                    "FIRECRAWL_API_KEY": "fc-45f3fdc542954e90a04caad1bd06ac88"
                    }
                }
            } 
        }

client = MCPClient.from_dict(config)
agent = MCPAgent(
            llm=llm,
            client=client,
            max_steps=100,
            verbose=True
        )
async def domain_aligned(state: Dict) -> Dict:
    domain_url= state.get("domain_url") or ""
    transcript = state.get("transcript") or ""
    domain_data = {
        "domain_url": domain_url,
        "transcript": transcript
    }
    # with open ("combined_domain_transcript.json","w",encoding="utf-8") as f:
    #     json.dump(domain_data,f, ensure_ascii=False, indent=4)
    
    combined_data = domain_data
    

    prompt = """
    You have two inputs:

    1. YouTube Transcript: A detailed step-by-step guide or tutorial video transcript focused on a specific topic.

    2. Domain Name: The website domain where related services, reviews, and guides are provided.

    Objective:

    1. First, scrape the provided domain and output the main raw text content you extracted from the website. Clearly label this section as 'RAW SCRAPED CONTENT'.

    2. Then, generate two distinct and concise summaries:

        a. Tutorial-Specific Summary: A 'What We Do' statement that directly aligns with the specific topic of the YouTube tutorial, clearly reflecting the domain’s relevant services.

        b. Comprehensive Company Summary: A general company overview that thoroughly highlights all key services offered by the company, including any core areas of expertise, customization, implementation, and consultation services.

    Web Scraping Instructions:

    1. For the Comprehensive Company Summary: Perform a general audit of the provided domain by scraping the website to extract relevant information. Focus on identifying the company’s main services, areas of expertise, industries served, and any other key offerings. Use this information to craft a summary that accurately represents the company’s complete range of services, regardless of the industry or service type.

    2. For the Tutorial-Specific Summary: Analyze the tutorial content and cross-reference it with the services listed on the domain. Use web scraping to identify and list all relevant services that the domain offers. Then, align the most appropriate service(s) with the intent of the transcript, ensuring the summary reflects how the company’s offerings support or enhance the tutorial topic. Ensure the summary is adaptable to various industries and service types.

    Guidelines:

    1. Service Alignment for Tutorial-Specific Summary: Tailor the first output to the specific content of the tutorial, showcasing how the domain’s services support or relate to the tutorial topic. Highlight the company’s expertise in the specific area covered by the video. If the services extend beyond technology, adapt the summary to reflect those other service types, such as consulting, product development, or creative services.

    2. Detailed Overview for Comprehensive Company Summary: Provide a broader overview of the company’s main services. Ensure the summary covers all key offerings, including services related to any relevant platforms, tools, or industries. Reflect the company's expertise in delivering customized solutions, strategic consultations, and tailored implementations. Adapt the summary to be relevant to the company’s specific industry or niche, ensuring scalability across diverse fields.

    3. Brevity and Clarity: Both summaries should be concise, clear, and comprehensive, effectively conveying the company’s expertise without unnecessary details.

    4. Customization: After generating the summaries, adapt the examples provided to better fit the specific details and context of the domain and YouTube transcript. Ensure that the tone and style match the intended audience (e.g., formal vs. informal, technical vs. marketing-focused).

    5. Handling Complex or Niche Services: For companies offering specialized or niche services, ensure the summaries accurately reflect these unique offerings. Highlight the company’s specific value proposition and how it stands out in its industry.

    * STRICTLY DO NOT ADD ANY EXPLANATION

    * Return strictly valid JSON only, no extra text, using this schema:

        {
        "Tutorial-Specific Summary" : "...",
        "Comprehensive Company Summary" : "..."
        }
    
    """

    Full_prompt = f"{prompt}\n\n{combined_data}"
    response = await agent.run(Full_prompt)
    # print(response)
    llm_output = response.strip()
    print(llm_output)
    llm_output = re.sub(r'\s+', ' ', llm_output).strip()
    if llm_output.startswith("```json"):
        llm_output = llm_output.split("```json")[1].split("```")[0]
    if llm_output.startswith("```"):
        llm_output = llm_output.split("```")[1]
    if llm_output.endswith("```"):
        llm_output = llm_output.split("```")[0]
    if llm_output.startswith("```json"):
        llm_output = llm_output.split("```json")[1].split("```")[0]

    data = json.loads(llm_output)
    # with open("Domain_aligned_cta.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)

    state["domain_aligned_cta"] = data
    return state



# if __name__ == "__main__":
#     transcript="""Nothing Phone 3 Review: They Lied!
#     (funky upbeat music)
#     - This is the Nothing Phone 3
#     and yeah, it's ugly.
#     (funky music)
#     You know, people say beauty is in the eye
#     of the beholder and stuff like that.
#     I get it. You can find
#     beauty in anything, for sure.
#     But also, you know,
#     there's a nice alignment
#     to things that feels good.
#     And you know, when things are,
#     when things are where
#     you expect them to be,
#     doesn't that feel better?
#     Okay. All right, carcinisation.
#     I learned about this recently.
#     """
#     asyncio.run(domain_aligned("https://aipxperts.com/",transcript))