import asyncio
import json
from setup_env import setup_environment, get_gemini_flash_model

# Setup environment & load model
setup_environment()
llm = get_gemini_flash_model()

# Import extraction agents 
# from agents.error_handling_agent import run_error_handling
# from agents.example_ref_agent import run_example_reference
# from agents.audience_agent import run_audience_spec
# from agents.links_ref_agent import run_links_reference
# from agents.conditional_logic_agent import run_conditional_logic

from Extract_Specific_Details.agents.error_handling_agent import run_error_handling
from Extract_Specific_Details.agents.example_ref_agent import run_example_reference
from Extract_Specific_Details.agents.audience_agent import run_audience_spec
from Extract_Specific_Details.agents.links_ref_agent import run_links_reference
from Extract_Specific_Details.agents.conditional_logic_agent import run_conditional_logic
from typing import Dict

async def extract_specific_details(state: Dict) -> dict:
    
    transcript = state.get("transcript") or ""
    error_section = await run_error_handling(transcript, llm)
    example_section = await run_example_reference(transcript, llm)
    audience_section = await run_audience_spec(transcript, llm)
    links_section = await run_links_reference(transcript, llm)
    conditional_section = await run_conditional_logic(transcript, llm)

    extracted_sections = {
        "ErrorHandlingSection": error_section,
        "ExamplesSection": example_section,
        "AudienceSection": audience_section,
        "LinksReferencesSection": links_section,
        "ConditionalLogicSection": conditional_section,
    }
    state["extracted_section"] = extracted_sections
    # print(extracted_sections)
    # data = json.loads(extracted_sections)
    # with open("extracted_sections.json", "w") as f:
    #     json.dump(extracted_sections, f, indent=4)

    print("✅ Extracted details saved to extracted_sections.json")
    return state

# if __name__ == "__main__":
#     asyncio.run(extract_specific_details())