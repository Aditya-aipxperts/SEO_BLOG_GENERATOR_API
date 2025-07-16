ERROR_HANDLING_PROMPT = """
Objective: Generate a detailed, actionable section focused on error handling based on the provided YouTube video transcript. This section should be written after the common issues and troubleshooting section, maintaining the same structure, format, and writing style used in the previous content.

Condition: First, check if the video transcript contains relevant information on error handling related to the [specific task/topic]. If the transcript does not include such content, return only the phrase "Not Applicable" without any additional details or explanations. If the transcript includes relevant error handling information, proceed with the following steps:

Instructions:

Purpose:

* Extract and deliver a comprehensive section focused on error handling during the [specific task/topic], providing clear steps to manage and resolve errors that users might encounter.

* Ensure these error handling tips are practical, offering actionable advice to help users prevent or correct errors effectively.

Tasks:

1. Identify Error Handling Information:

* Carefully review the transcript to identify any mentions of error handling, including strategies or best practices for managing errors during the [specific task/topic].

* Expand on these mentions by providing additional context or detailed steps that make the error handling instructions practical and easy to implement.

2. Provide Error Handling Steps:

* For each identified error handling scenario, provide clear, step-by-step instructions to help users manage and resolve errors.

* Where applicable, offer preventative tips to avoid the errors in the first place and suggestions for what to do if an error cannot be easily resolved.

3. Expand on Examples:

* If the transcript mentions specific examples of error handling, integrate them into the section, providing additional context or variations that demonstrate different error handling scenarios.

* If the transcript lacks examples, infer possible errors and provide hypothetical error handling steps that could apply to a variety of situations.

4. Use of Keywords:

* Integrate primary keywords naturally within headings and key error handling steps, ensuring their relevance to the content.

* Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.

5. Visual Prompts:

* Suggest relevant visuals (e.g., screenshots, diagrams) where applicable to enhance understanding of the error handling steps. Specify how these visuals should be incorporated (e.g., callouts, inline, or separate sections).

* Provide detailed descriptions of what each visual should depict and how it supports the accompanying text.

6. Simplify Language:

* Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience.

7. Streamline Content:

* Avoid redundant content by summarizing similar error handling tips or combining them into more comprehensive advice where appropriate.

* Focus on providing efficient, actionable error handling steps that directly address the user's needs.

8. Audit for Completeness:

* Review the identified error handling information against the transcript to ensure all relevant content is covered and no essential details are omitted.

* Ensure the steps flow logically, are easy to understand, and provide real value to the reader.

Keyword Integration:

1. Primary Keywords:

* Use primary keywords in H2 headings and key error handling steps, ensuring they fit naturally within the content.

2. Secondary Keywords:

* Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit.

* Use these keywords to add context or depth without overwhelming the reader.

3. Avoid Over-Optimization:

* Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.

Examples:

1. Integration:

* Where examples of error handling are provided in the transcript, integrate them into the section to illustrate key points or concepts.

2. Modification:

* Modify examples to avoid content cannibalism by changing names, numbers, and data to make them more relevant and original.

* Provide alternative scenarios or variations to demonstrate the flexibility of the error handling steps.

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

1. Error Handling Section:

* Generate a detailed, clear, and concise section that addresses error handling and provides practical steps related to the [specific task/topic].

* Ensure the section is as long as necessary, incorporating examples, visuals, and best practices where needed.

2. Audit:

* Conduct a thorough review to ensure that all error handling steps mentioned in the transcript are captured and that no essential details are omitted.

* Ensure the content flows logically, and that there are no gaps in the information provided.

"""

EXAMPLE_REFERENCE_PROMPT = """
Objective: Generate a detailed, actionable section focused on extracting and presenting references, examples, and relevant data points based on the provided YouTube video transcript. This section should be written after the error handling section, maintaining the same structure, format, and writing style used in the previous content.

Condition: First, check if the video transcript contains references, examples, or relevant data points that are closely related to the core [specific task/topic]. If the transcript does not include such content, return only the phrase "Not Applicable" and do not provide any additional details, explanations, or context. If the transcript includes relevant information, proceed with the following steps:

Instructions:

Purpose:

* Extract and deliver a comprehensive section focused on references, examples, and data points that directly support or illustrate key aspects of the [specific task/topic] discussed in the video.

* Ensure these references and examples are presented clearly, offering actionable insights or reinforcing the guide's key points.

Tasks:

1. Identify Relevant References and Examples:

* Carefully analyze the transcript to identify any references, examples, or data points that are closely related to the [specific task/topic].

* Prioritize those that are most relevant to the core topic and can provide valuable context or clarification for the reader.

2. Integrate References and Examples:

* Organize the identified references and examples into a structured section that flows naturally from the error handling section.

* Provide detailed explanations or context for each reference or example, ensuring that their relevance to the core topic is clear.

3. Expand on Examples:

* If the transcript mentions specific examples, integrate them into the section, providing additional context or variations that demonstrate their applicability to different scenarios.

* If the transcript lacks sufficient detail, infer possible examples or data points and expand on them to illustrate the key points effectively.

4. Use of Keywords:

* Integrate primary keywords naturally within headings and key references or examples, ensuring their relevance to the content.

* Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.

5. Visual Prompts:

* Suggest relevant visuals (e.g., screenshots, charts, tables) where applicable to enhance understanding of the references and examples. Specify how these visuals should be incorporated (e.g., callouts, inline, or separate sections).

* Provide detailed descriptions of what each visual should depict and how it supports the accompanying text.

6. Simplify Language:

* Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience.

7. Streamline Content:

* Avoid redundant content by summarizing similar references or examples, combining them into more comprehensive insights where appropriate.

* Focus on providing references and examples that directly support the key points and enhance the reader's understanding.

8. Audit for Completeness:

* Review the identified references and examples against the transcript to ensure all relevant content is covered and no essential details are omitted.

* Ensure the references and examples flow logically, are easy to understand, and provide real value to the reader.

Keyword Integration:

1. Primary Keywords:

* Use primary keywords in H2 headings and key references or examples, ensuring they fit naturally within the content.

2. Secondary Keywords:

* Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit.

* Use these keywords to add context or depth without overwhelming the reader.

3. Avoid Over-Optimization:

* Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.

Examples:

1. Integration:

* Where examples, references, or data points are provided in the transcript, integrate them into the section to illustrate key points or concepts.

2. Modification:

* Modify examples to avoid content cannibalism by changing names, numbers, and data to make them more relevant and original.

* Provide alternative scenarios or variations to demonstrate the flexibility and applicability of the references and examples.

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

1. References, Examples, and Data Points Section:

* Generate a detailed, clear, and concise section that provides relevant references, examples, and data points related to the [specific task/topic].

* Ensure the section is as long as necessary, incorporating visuals, examples, and best practices where needed.

2. Audit:

* Conduct a thorough review to ensure that all references, examples, and data points mentioned in the transcript are captured and that no essential details are omitted.

* Ensure the content flows logically, and that there are no gaps in the information provided.

"""

AUDIENCE_PROMPT = """
Objective: Generate a detailed, actionable section focused on extracting and presenting audience specification or persona information based on the provided YouTube video transcript. This section should be written after the references, examples, and data points section, maintaining the same structure, format, and writing style used in the previous content.

Condition: First, check if the video transcript contains relevant information on audience specification or persona related to the [specific task/topic]. If the transcript does not include such content, return only the phrase "Not Applicable" without any additional details, explanations, or context. If the transcript includes relevant audience specification or persona information, proceed with the following steps:

Instructions:

Purpose:

* Extract and deliver a comprehensive section that identifies the target audience or personas mentioned in the transcript, focusing on their characteristics, needs, and preferences related to the [specific task/topic].

* If multiple audiences are mentioned, group them based on shared characteristics or relevant distinctions to provide a clear understanding of who the guide is intended for.

Tasks:

1. Identify Audience or Persona Information:

* Carefully review the transcript to identify any mentions of the target audience, user personas, or specific groups that the content is intended to address.

* Note any characteristics, needs, goals, or challenges that are highlighted in relation to these audiences.

2. Group and Categorize Audiences:

* If multiple audiences are mentioned, categorize them into groups based on shared characteristics, such as experience level, industry, or specific needs related to the [specific task/topic].

* Provide a brief description of each group, highlighting their unique characteristics and how the guide’s content is tailored to meet their needs.

3. Expand on Audience Needs:

* Where applicable, expand on the needs, preferences, or challenges of each audience group. Explain how the content or tools discussed in the transcript address these aspects.

* If the transcript lacks detailed information, infer possible needs or challenges based on the audience characteristics and provide practical insights or solutions.

4. Use of Keywords:

* Integrate primary keywords naturally within headings and key audience specifications, ensuring their relevance to the content.

* Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.

5. Visual Prompts:

* Suggest relevant visuals (e.g., persona profiles, audience segmentation charts) where applicable to enhance understanding of the audience specification. Specify how these visuals should be incorporated (e.g., callouts, inline, or separate sections).

* Provide detailed descriptions of what each visual should depict and how it supports the accompanying text.

6. Simplify Language:

* Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience.

7. Streamline Content:

* Avoid redundant content by summarizing similar audience characteristics or combining them into more comprehensive personas where appropriate.

* Focus on providing clear, actionable insights that help the reader understand the target audience and how the content addresses their specific needs.

8. Audit for Completeness:

* Review the identified audience information against the transcript to ensure all relevant content is covered and no essential details are omitted.

* Ensure the audience personas or specifications flow logically, are easy to understand, and provide real value to the reader.

Keyword Integration:

1. Primary Keywords:

* Use primary keywords in H2 headings and key audience specifications, ensuring they fit naturally within the content.

2. Secondary Keywords:

* Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit.

* Use these keywords to add context or depth without overwhelming the reader.

3. Avoid Over-Optimization:

* Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.

Examples:

1. Integration:

* Where examples of audience personas or specifications are provided in the transcript, integrate them into the section to illustrate key points or concepts.

2. Modification:

* Modify examples to avoid content cannibalism by changing names, details, and data to make them more relevant and original.

* Provide alternative scenarios or variations to demonstrate the flexibility and applicability of the audience specifications.

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

1. Audience Specification / Persona Section:

* Generate a detailed, clear, and concise section that identifies and describes the target audience or personas related to the [specific task/topic].

* Ensure the section is as long as necessary, incorporating visuals, examples, and best practices where needed.

2. Audit:

* Conduct a thorough review to ensure that all audience specification and persona information mentioned in the transcript is captured and that no essential details are omitted.

* Ensure the content flows logically, and that there are no gaps in the information provided.

"""

LINKS_REFERENCES_PROMPT = """
Objective: Generate a detailed, actionable section focused on extracting and presenting links and references based on the provided YouTube video transcript. This section should be written after the audience specification/persona section, maintaining the same structure, format, and writing style used in the previous content.

Condition: First, check if the video transcript contains relevant information on links, external references, or resources related to the [specific task/topic]. If the transcript does not include such content, return only the phrase "Not Applicable" without any additional details, explanations, or context. If the transcript includes relevant links and references, proceed with the following steps:

Instructions:

Purpose:

* Extract and deliver a comprehensive section that identifies and presents any external links, references, or resources mentioned in the transcript, focusing on their relevance to the [specific task/topic].

* Ensure these links and references are presented clearly, offering actionable insights or further reading opportunities for the reader.

Tasks:

1. Identify Links and References:

* Carefully review the transcript to identify any mentions of external links, references, or resources that are related to the [specific task/topic].

* Note any URLs, document titles, or specific references to external sources that are highlighted as useful or essential for the reader.

2. Organize and Present References:

* Organize the identified links and references into a structured section that flows naturally from the audience specification/persona section.

* Provide brief descriptions of each link or reference, explaining its relevance to the core topic and why the reader might find it useful.

3. Categorize References:

* If multiple types of references are mentioned (e.g., articles, tutorials, tools), categorize them accordingly to help readers quickly find the resources that are most relevant to their needs.

* Offer context or background for each category, if necessary, to clarify its importance in relation to the [specific task/topic].

4. Use of Keywords:

* Integrate primary keywords naturally within headings and key references, ensuring their relevance to the content.

* Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.

5. Visual Prompts:

* Suggest relevant visuals (e.g., screenshots of web pages, icons representing tools) where applicable to enhance understanding of the links and references. Specify how these visuals should be incorporated (e.g., callouts, inline, or separate sections).

* Provide detailed descriptions of what each visual should depict and how it supports the accompanying text.

6. Simplify Language:

* Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience.

7. Streamline Content:

* Avoid redundant content by summarizing similar references or combining them into more comprehensive insights where appropriate.

* Focus on providing links and references that directly support the key points and enhance the reader's understanding.

8. Audit for Completeness:

* Review the identified links and references against the transcript to ensure all relevant content is covered and no essential details are omitted.

* Ensure the links and references flow logically, are easy to understand, and provide real value to the reader.

Keyword Integration:

1. Primary Keywords:

* Use primary keywords in H2 headings and key references, ensuring they fit naturally within the content.

2. Secondary Keywords:

* Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit.

* Use these keywords to add context or depth without overwhelming the reader.

3. Avoid Over-Optimization:

* Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.

Examples:

1. Integration:

* Where external links, references, or resources are provided in the transcript, integrate them into the section to illustrate key points or concepts.

2. Modification:

* Modify the presentation of links or references to avoid content cannibalism by changing descriptions or context to make them more relevant and original.

* Provide alternative scenarios or variations to demonstrate the flexibility and applicability of the references.

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

1. Links and References Section:

* Generate a detailed, clear, and concise section that identifies and presents relevant links, external references, and resources related to the [specific task/topic].

* Ensure the section is as long as necessary, incorporating descriptions, visuals, and best practices where needed.

2. Audit:

* Conduct a thorough review to ensure that all links, references, and resources mentioned in the transcript are captured and that no essential details are omitted.

* Ensure the content flows logically, and that there are no gaps in the information provided.

"""

CONDITIONAL_LOGIC_PROMPT = """
Objective: Generate a detailed, actionable section focused on extracting and presenting information about the depth and types of conditional logic mentioned in the provided YouTube video transcript. This section should be written after the links and references section, maintaining the same structure, format, and writing style used in the previous content.



Condition: First, check if the video transcript contains relevant information on conditional logic related to the [specific task/topic]. If the transcript does not include such content, return only the phrase "Not Applicable" without any additional details, explanations, or context. If the transcript includes relevant information on conditional logic, proceed with the following steps:

Instructions:



Purpose:



Extract and deliver a comprehensive section that identifies and presents the depth of detail or types of conditional logic mentioned in the transcript, focusing on how they relate to the [specific task/topic].

Ensure these insights into conditional logic are presented clearly, offering actionable advice on how to implement or understand the conditional logic discussed.



Tasks:



Identify Conditional Logic Information:

Carefully review the transcript to identify any mentions of conditional logic, including how it is set up, types of conditions used, and the level of detail provided.

Note the complexity of the conditional logic described, whether it involves simple conditions or more advanced, nested logic.



Describe Conditional Logic Depth:

Organize the identified information into a structured section that flows naturally from the links and references section.

Provide detailed explanations of each type of conditional logic mentioned, highlighting its relevance to the core topic and how it enhances the [specific task/topic].



Expand on Examples:

If the transcript mentions specific examples of conditional logic, integrate them into the section, providing additional context or variations that demonstrate different levels of complexity.

If the transcript lacks sufficient detail, infer possible applications of conditional logic and expand on them to illustrate how it can be used effectively.



Use of Keywords:

Integrate primary keywords naturally within headings and key explanations of conditional logic, ensuring their relevance to the content.

Use secondary keywords to provide additional context and depth, maintaining readability and avoiding over-optimization.



Visual Prompts:

Suggest relevant visuals (e.g., flowcharts, decision trees) where applicable to enhance understanding of the conditional logic discussed. Specify how these visuals should be incorporated (e.g., callouts, inline, or separate sections).

Provide detailed descriptions of what each visual should depict and how it supports the accompanying text.



Simplify Language:

Write at a 7th-grade reading level, using simple, clear language to ensure accessibility to a wide audience.



Streamline Content:

Avoid redundant content by summarizing similar types of conditional logic or combining them into more comprehensive explanations where appropriate.

Focus on providing clear, actionable insights that help the reader understand and implement the conditional logic discussed.



Audit for Completeness:

Review the identified conditional logic information against the transcript to ensure all relevant content is covered and no essential details are omitted.

Ensure the explanations of conditional logic flow logically, are easy to understand, and provide real value to the reader.



Keyword Integration:



Primary Keywords:

Use primary keywords in H2 headings and key descriptions of conditional logic, ensuring they fit naturally within the content.



Secondary Keywords:

Integrate secondary keywords in H3 and H4 headings or within the body text where they naturally fit.

Use these keywords to add context or depth without overwhelming the reader.



Avoid Over-Optimization:

Focus on readability and natural flow. Keywords should enhance the content, not dominate it. Avoid excessive repetition, using synonyms or rephrasing when necessary.



Examples:



Integration:

Where examples of conditional logic are provided in the transcript, integrate them into the section to illustrate key points or concepts.



Modification:

Modify examples to avoid content cannibalism by changing names, conditions, and data to make them more relevant and original.

Provide alternative scenarios or variations to demonstrate the flexibility and applicability of the conditional logic.



Writing Style:



Voice:

Maintain consistency with the writing style used in the previous sections. Use first-person or third-person, depending on the context.



Tone:

Write in a tone suitable for a 7th-grade reading level, using simple, clear language.



Structure:

Write short sentences (5-10 words) and use short paragraphs. Use appropriate headings (H2, H3, H4) to organize content logically.

Enhance readability by using bullet points, numbered lists, or tables where appropriate.



Maintain Continuation:

Ensure a seamless transition from the previous section, keeping the content engaging and easy to follow.



Output:



Conditional Logic Depth Section:

Generate a detailed, clear, and concise section that explains the depth and types of conditional logic related to the [specific task/topic].

Ensure the section is as long as necessary, incorporating descriptions, examples, visuals, and best practices where needed.



Audit:

Conduct a thorough review to ensure that all conditional logic information mentioned in the transcript is captured and that no essential details are omitted.

Ensure the content flows logically, and that there are no gaps in the information provided.
"""
