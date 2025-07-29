# Tool: Web Search
from langchain.utilities import SerpAPIWrapper
def get_web_search_tool():
   return {
       "name": "Web Search",
       "func": SerpAPIWrapper().run,
       "description": "Useful for answering questions about current events or general knowledge using SerpAPI."
   }