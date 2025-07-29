# LangGraph-powered research agent
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from app.tools.web_search import get_web_search_tool
from app.tools.calculator import get_calculator_tool
from app.tools.pdf_reader import get_pdf_reader_tool
def create_research_agent():
   tools = [
       Tool(**get_web_search_tool()),
       Tool(**get_calculator_tool()),
       Tool(**get_pdf_reader_tool()),
   ]
   llm = OpenAI(temperature=0)
   return initialize_agent(
       tools, llm, agent="zero-shot-react-description", verbose=True
   )