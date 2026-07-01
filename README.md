# AI Multi-Agent Research Assistant

An AI-powered research assistant that autonomously searches the web, scrapes relevant sources, generates a structured research report, and critiques its own output using a multi-agent workflow built with LangChain and Google Gemini.

## Live Demo

**Live Application:** https://multi-agent-research-system-8l0p.onrender.com

## GitHub Repository

https://github.com/SmrSingh/multi-agent-research-system

---

## Features

- Multi-agent research workflow using LangChain
- Web search using Tavily Search API
- Automatic extraction of top search results
- Web scraping with BeautifulSoup
- AI-generated research reports
- AI-powered report review and feedback
- Interactive Streamlit interface
- Download generated reports
- Deployed on Render

---

## Workflow

```text
                User Query
                     │
                     ▼
             Search Agent (Gemini)
                     │
                     ▼
             Tavily Web Search
                     │
                     ▼
          Extract Top 3 Relevant URLs
                     │
                     ▼
      Scrape Webpages (BeautifulSoup)
                     │
                     ▼
        Combine Research Information
                     │
                     ▼
          Writer Agent (Gemini)
                     │
                     ▼
      Generate Research Report
                     │
                     ▼
          Critic Agent (Gemini)
                     │
                     ▼
      Report + Feedback + Sources
```

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Search API | Tavily Search |
| Web Scraping | Requests, BeautifulSoup |
| Frontend | Streamlit |
| Deployment | Render |
| Environment | Python Dotenv |

---

## Project Structure

```text
multi-agent-research-system/
│
├── app.py                  # Streamlit frontend
├── pipeline.py             # Multi-agent research pipeline
├── agents.py               # Search, Writer and Critic agents
├── tools.py                # Search and scraping tools
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/SmrSingh/multi-agent-research-system.git

cd multi-agent-research-system
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Example Workflow

1. Enter a research topic.
2. The Search Agent searches the web using Tavily.
3. The top search results are extracted.
4. Relevant webpages are scraped.
5. The Writer Agent generates a structured research report.
6. The Critic Agent reviews the report and provides feedback.
7. The report, feedback, and source links are displayed in the Streamlit interface.

---

## Screenshots


### Home Page


<img width="1917" height="886" alt="image" src="https://github.com/user-attachments/assets/3a874765-7e54-43b0-abee-229a8ea62c90" />


### Generated Report


<img width="1902" height="893" alt="image" src="https://github.com/user-attachments/assets/dac89d04-268b-400d-a85e-f4ff696d00fc" />


### Critic Feedback


<img width="1696" height="557" alt="image" src="https://github.com/user-attachments/assets/1ffb1830-68b8-4090-819e-a7d07879e253" />


---

## Skills Demonstrated

- Multi-Agent AI Systems
- LangChain Agents
- Prompt Engineering
- Tool Calling
- Google Gemini API Integration
- Web Search Integration
- Web Scraping
- AI Report Generation
- Streamlit Development
- Deployment on Render





GitHub: https://github.com/SmrSingh

LinkedIn: *(Add your LinkedIn profile here)*
