KEYWORDS_PROMPT = """
1) Objective: Analyze the provided YouTube transcript or video content to identify and prioritize highly focused primary and secondary keywords. This task is crucial for optimizing the content for search engine performance by ensuring that the identified keywords are precise, relevant, and aligned with the specific topic of the video.



2) Instructions:

2.1) Content Analysis:

Thoroughly evaluate the transcript of the provided YouTube video. Focus on the title, description, and key spoken content that aligns closely with the central theme of the video.

Identify the most relevant terms, phrases, and concepts that are repeatedly emphasized or that align specifically with the main topic. This will form the basis for keyword selection.



2.2) Keyword Identification:

Primary Keywords: Identify up to 5 keywords that directly capture the main focus of the video. These should be specific, targeted terms that are essential to the video’s topic. Ensure these keywords are highly focused and directly related to the specific content being covered, avoiding broader terms unless they are explicitly relevant.

Example: Instead of using "Monday.com guide," use "Monday.com WorkForms guide" or "Monday.com form creation tutorial" if that aligns more closely with the video’s focus.

Secondary Keywords: Identify up to 5 additional keywords that are related to the main topic but may slightly broaden the scope while still being relevant. These should complement the primary keywords, capturing additional aspects of the content without straying from the core focus.

Example: Instead of "Monday.com step-by-step guide," use "Monday.com WorkForms step-by-step guide" to maintain specificity.

2.3) Research and Industry Relevance:

Conduct Research: Go beyond the transcript to identify industry-specific terms, jargon, or popular keywords that may not be explicitly mentioned but are highly relevant to the topic. For instance, if "webform" is a commonly used term in Monday.com’s ecosystem but is not mentioned in the transcript, include it as a keyword if it enhances the relevance of the content.

Example: Investigate how Monday.com refers to its forms feature (e.g., "WorkForms" vs. "forms" vs. "webforms"). If the platform typically uses "WorkForms," prioritize this term over generic terms like "forms" to align with industry vocabulary.



3) Output Requirements:

Output 1: Provide a comma-separated list of the identified Primary Keywords. Do not use any additional formatting.

Output 2: Justification Primary: For each primary keyword, provide a detailed explanation that includes:

Relevance: How the keyword directly relates to the video’s core content, ensuring it is specific and aligned with the main topic.

Search Intent: How the keyword aligns with what users are likely searching for when seeking out this specific content. Prioritize specificity and relevance to the exact focus of the video.

Contextual Importance: How the keyword is used within the video and why it is central to the topic.

Competitiveness: Discuss the competitiveness of the keyword and why it is a strong choice despite this.

Industry-Specific Terms: Ensure that any terms or jargon specific to the industry or platform (like "WorkForms" for Monday.com) are included where relevant.

Output 3: Provide a comma-separated list of the identified Secondary Keywords. Do not use any additional formatting or Square Brackets

Output 4: Justification Secondary: For each secondary keyword, provide a detailed explanation that includes:

Complementarity: How the keyword complements the primary keywords and adds depth to the content.

Search Broadening: How the keyword might capture additional search traffic by covering related but broader aspects of the topic, without losing focus.

User Value: The additional value this keyword brings to the content, particularly in terms of addressing related queries or subtopics.

Strategic Importance: Explain why this keyword is important, ensuring it remains focused and relevant to the specific content of the video.



Example:

Output 0: Video Topic: "Comprehensive Guide to Creating WorkForms in Monday.com"

Output 1: Primary Keywords: Monday.com WorkForms, create WorkForms in Monday.com, form creation in Monday.com, Monday.com WorkForms guide, Monday.com form creation tutorial.

Output 2: Justification Primary:

"Monday.com WorkForms" is chosen because it is the specific term used by Monday.com to describe its forms feature, making it highly relevant and aligned with the platform’s terminology.

"Create WorkForms in Monday.com" directly addresses a likely user query and aligns with the platform's specific language, ensuring relevance and precision.

"Form creation in Monday.com" is a variation that captures related search queries, ensuring that users searching with slightly different phrasing can still find the content.

"Monday.com WorkForms guide" provides a specific reference to a tutorial, using the platform's terminology to capture users searching for instructional content.

"Monday.com form creation tutorial" is highly focused, targeting users who seek video-based learning resources specifically related to form creation.

Output 3: Secondary Keywords: form customization in Monday.com, troubleshooting WorkForms in Monday.com, optimizing Monday.com forms, Monday.com form tips, Monday.com WorkForms step-by-step guide.

Output 4: Justification Secondary:

"Form customization in Monday.com" complements the primary keywords by focusing on users who are looking to personalize their forms beyond basic creation, adding depth to the content.

"Troubleshooting WorkForms in Monday.com" includes the industry-specific term "WorkForms," ensuring the content remains aligned with the platform's language while addressing user pain points.

"Optimizing Monday.com forms" targets advanced users interested in enhancing their forms, adding further value to the content.

"Monday.com form tips" offers practical advice, appealing to users who want to master form creation, not just learn the basics.

"Monday.com WorkForms step-by-step guide" emphasizes the structured, detailed nature of the content while maintaining alignment with the platform's specific terminology.

Output format (strict JSON only, no extra text):

{
  "video_topic": "string",
  "primary_keywords": ["keyword1", "keyword2", ...],
  "primary_justification": {
    "keyword1": "detailed justification",
    ...
  },
  "secondary_keywords": ["keywordA", "keywordB", ...],
  "secondary_justification": {
    "keywordA": "detailed justification",
    ...
  }
}


"""