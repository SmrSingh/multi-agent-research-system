from agents import build_search_agent, writer_chain, critic_chain
from tools import scrape_url
import re

def extract_urls(text):
    pattern = r'https?://[^\s)]+'
    return re.findall(pattern, text)
def run_research_pipeline(topic : str) -> dict:

    state = {}

    print("\n"+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
    "messages": [(
        "user",
        f"""
You MUST use the web_search tool.

Search for:

{topic}

IMPORTANT:

Do NOT summarize.

Return the tool output exactly as received.

Every search result must include:

Title:
URL:
Snippet:

Do not rewrite.
Do not explain.
Do not remove URLs.
"""
    )]
})
    state["search_results"] = search_result['messages'][-1].content
    state["urls"] = extract_urls(str(state["search_results"]))[:3]

    print("\nTop 3 URLs:")
    for i, url in enumerate(state["urls"], start=1):
        print(f"{i}. {url}")
    print("\n search result ",state['search_results'])
    
    #step 2 - reader agent
    print("\n"+" ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    scraped_contents = []

    for i, url in enumerate(state["urls"], start=1):
        print(f"\nScraping ({i}/3): {url}")

        try:
            content = scrape_url.invoke(url)

            if content and "Could not scrape" not in content:
                scraped_contents.append(content)
            else:
                print(f"Skipping {url}")

        except Exception as e:
            print(f"Error scraping {url}")
            print(e)

    state["scraped_content"] = "\n\n".join(scraped_contents)

    print("\nScraped Content:\n")
    print(state["scraped_content"][:2000])

    print("\nScraped Content:\n")
    print(state["scraped_content"][:2000])

    print("\nscraped content: \n", state['scraped_content'])

    #step 3 - writer chain 

    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("\n Final Report\n",state['report'])
    
    #critic report 

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report":state['report']
    })

    print("\n critic report \n", state['feedback'])

    return state
if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)


    