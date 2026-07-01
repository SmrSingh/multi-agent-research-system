import streamlit as st
from pipeline import run_research_pipeline

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.title("🤖 AI Research Assistant")

    st.markdown("### Tech Stack")
    st.markdown("""
- Gemini 2.5 Flash
- LangChain
- Tavily Search
- BeautifulSoup
""")

    st.divider()

    st.markdown("### Workflow")
    st.markdown("""
1. Search Agent
2. Web Search
3. Web Scraping
4. Writer Agent
5. Critic Agent
""")

# ----------------------------
# Main UI
# ----------------------------

st.title(" AI Multi-Agent Research Assistant")
st.write("Generate detailed research reports using multiple AI agents.")

topic = st.text_input(
    "Enter a Research Topic",
    placeholder="Example: Latest AI Breakthroughs"
)

if st.button("Generate Report", use_container_width=True):

    if topic.strip() == "":
        st.warning("Please enter a research topic.")

    else:

        with st.spinner("Running Multi-Agent Pipeline..."):

            result = run_research_pipeline(topic)

        st.success("Research Completed Successfully!")

        # ---------------- Report ----------------

        st.header("Research Report")

        st.markdown(result["report"])

        st.download_button(
            "⬇ Download Report",
            result["report"],
            file_name="research_report.md",
            mime="text/markdown"
        )

        # ---------------- Critic ----------------

        with st.expander("Critic Feedback"):

            st.markdown(result["feedback"])

        # ---------------- Sources ----------------

        st.header("Sources")

        if len(result["urls"]) == 0:

            st.warning("No URLs Found.")

        else:

            for url in result["urls"]:

                st.link_button(url, url)