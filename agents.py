from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url 
from dotenv import load_dotenv
load_dotenv()
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

def build_search_agent():
    return create_agent(
        model = llm,
        tools= [web_search]
    )

def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a senior research analyst.

Your job is to create professional, evidence-based research reports.

Rules:
- Use ONLY the information provided in the research.
- Never invent facts, statistics, names, or events.
- If information is insufficient, explicitly state that.
- If different sources present different viewpoints, mention the disagreement instead of choosing one.
- Write objectively and avoid speculation.
- Clearly organize information into sections.
- Every important claim should be supported by the supplied research.
- Include all unique source URLs exactly as provided.
"""
    ),

    (
        "human",
        """
Create a comprehensive research report.

Topic:
{topic}

Research:
{research}

Write the report using the following structure.

# Introduction

- Explain the topic.
- Give background and context.

# Key Findings

Include at least 4 well-developed findings.

For each finding:
- Explain it clearly.
- Mention why it is important.
- Reference the available research.
- Do not repeat information.

# Analysis

Summarize patterns, trends, or relationships observed across the gathered sources.

If the available research is limited, explicitly mention that.

# Conclusion

Provide a balanced summary of the research.

Do not introduce any new information.

# Sources

List every unique URL exactly as provided in the research.

Requirements:
- Professional tone
- Clear headings
- Well-structured paragraphs
- No hallucinated information
- No unsupported claims
- Do not fabricate citations
"""
    )
])

writer_chain = writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()