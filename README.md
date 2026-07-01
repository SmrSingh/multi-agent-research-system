# AI Multi-Agent Research Assistant

A modular AI-powered research assistant built using **LangChain**, **Google Gemini**, **Tavily Search API**, and **BeautifulSoup**. The system employs multiple specialized agents to search the web, extract relevant information, generate structured research reports, and evaluate the quality of the generated content.

---

## Features

- Multi-agent architecture using LangChain
- Web search powered by Tavily Search API
- Web scraping with BeautifulSoup
- AI-generated research reports
- Automated report evaluation using a Critic Agent
- LCEL (LangChain Expression Language) pipelines
- Modular and extensible codebase

---

## Architecture

```
                User Query
                     │
                     ▼
             Search Agent
                     │
             Tavily Search Tool
                     │
                     ▼
              Search Results
                     │
                     ▼
             Reader Agent
                     │
         BeautifulSoup Scraper
                     │
                     ▼
            Extracted Web Content
                     │
                     ▼
              Writer Chain
                     │
             Research Report
                     │
                     ▼
              Critic Chain
                     │
                     ▼
             Final Evaluation
```

---

## Tech Stack

- Python
- LangChain
- Google Gemini
- Tavily Search API
- BeautifulSoup
- Requests
- LCEL (LangChain Expression Language)
- Python-dotenv

---

## Project Structure

```
multi-agent-research-system/
│
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/SmrSingh/multi-agent-research-system.git
cd multi-agent-research-system
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Run the application

```bash
python pipeline.py
```

---

## Workflow

### Search Agent

- Searches the web using Tavily
- Retrieves relevant URLs and summaries

### Reader Agent

- Selects a relevant webpage
- Extracts clean text using BeautifulSoup

### Writer Chain

Generates a structured research report including:

- Introduction
- Key Findings
- Conclusion
- Sources

### Critic Chain

Evaluates the generated report by providing:

- Overall score
- Strengths
- Areas for improvement
- Final verdict

---

## Sample Output

```
Enter a research topic:

Artificial Intelligence

Step 1 - Search Agent
Searching latest information...

Step 2 - Reader Agent
Scraping relevant webpage...

Step 3 - Writer Chain
Generating research report...

Step 4 - Critic Chain
Evaluating report...

Research completed successfully.
```

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Multi-Agent Systems
- LangChain Agents
- Tool Calling
- LCEL Pipelines
- Prompt Engineering
- LLM Integration
- Web Scraping
- API Integration
- Modular Software Design

---

## Author

**Smriti Singh**

GitHub: https://github.com/SmrSingh
