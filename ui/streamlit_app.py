# Streamlit app
import streamlit as st
import os
import sys
from dotenv import load_dotenv
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.agents.research_agent import create_research_agent

load_dotenv()
st.set_page_config(page_title="LLM Research Agent", layout="wide")
st.title("LLM Research Assistant")
query = st.text_input("Enter your research question")
if query:
   with st.spinner("Thinking with tools..."):
       try:
           agent = create_research_agent()
           result = agent.run(query)
           st.success(result)
       except Exception as e:
           st.error(f"Failed: {str(e)}")