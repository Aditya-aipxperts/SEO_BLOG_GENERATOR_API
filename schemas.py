from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class TopicKeyword(BaseModel):
    video_topic: str
    primary_keywords: List[str]
    primary_justification: Dict[str, str]
    secondary_keywords: List[str]
    secondary_justification: Optional[Dict[str, str]] = None

class ErrorHandlingSection(BaseModel):
    errors: Optional[List[str]] = None
    details: Optional[Any] = None

class ExampleSection(BaseModel):
    examples: Optional[List[str]] = None
    details: Optional[Any] = None

class AudienceSection(BaseModel):
    audience: Optional[str] = None
    details: Optional[Any] = None

class LinksReferencesSection(BaseModel):
    links: Optional[List[str]] = None
    details: Optional[Any] = None

class ConditionalLogicSection(BaseModel):
    logic: Optional[str] = None
    details: Optional[Any] = None

class ExtractedSections(BaseModel):
    ErrorHandlingSection: Optional[ErrorHandlingSection]
    ExamplesSection: Optional[ExampleSection]
    AudienceSection: Optional[AudienceSection]
    LinksReferencesSection: Optional[LinksReferencesSection]
    ConditionalLogicSection: Optional[ConditionalLogicSection]

class SpecificDetails(BaseModel):
    extracted_section: ExtractedSections

class GuideSubsection(BaseModel):
    title: str
    content: str

class GuideSection(BaseModel):
    title: str
    subsections: List[GuideSubsection]

class Guide(BaseModel):
    title: str
    overview: str
    sections: List[GuideSection]

class IssueExample(BaseModel):
    transcript_excerpt: Optional[str]
    expanded_context: str

class IssueVisualPrompt(BaseModel):
    purpose: str
    description: str

class Issue(BaseModel):
    title: str
    description: str
    troubleshooting_steps: List[str]
    preventative_tips: List[str]
    visual_prompts: List[IssueVisualPrompt]
    example: IssueExample

class IssueTroubleshoot(BaseModel):
    status: str
    section_title: Optional[str] = None
    issues: Optional[List[Issue]] = None

class CustomizationTipExample(BaseModel):
    transcript_excerpt: Optional[str]
    expanded_context: str

class CustomizationTipVisualPrompt(BaseModel):
    purpose: str
    description: str

class CustomizationTip(BaseModel):
    title: str
    description: str
    steps: List[str]
    example: CustomizationTipExample
    visual_prompt: CustomizationTipVisualPrompt

class CustomizationTips(BaseModel):
    status: str
    section_title: Optional[str] = None
    tips: Optional[List[CustomizationTip]] = None

class Conclusion(BaseModel):
    conclusion: str

class CTA(BaseModel):
    call_to_action: str

class DomainAligned(BaseModel):
    Tutorial_Specific_Summary: str = Field(..., alias="Tutorial-Specific Summary")
    Comprehensive_Company_Summary: str = Field(..., alias="Comprehensive Company Summary")

class FinalBlog(BaseModel):
    Polished_Blog: str

class SEOBlogGenerator(BaseModel):
    video_url: str
    domain_url: str
    raw_blog: str
    transcript: str
    topic_keyword: TopicKeyword
    specific_details: SpecificDetails
    introduction: str
    refined_intro: str
    guide: Guide
    video_id: str
    issue_troubleshoot: IssueTroubleshoot
    conclusion: Conclusion
    cta: CTA
    customization_tips: CustomizationTips
    domain_aligned: DomainAligned
    final_blog: FinalBlog
    combined_data: Dict
    combined_data_keyword_specific_details: Dict
    