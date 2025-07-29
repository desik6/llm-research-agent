# 🧠 LLM Research Agent
This project is a multi-tool intelligent research assistant powered by OpenAI's LLMs, LangChain, and LangGraph-style planning. It allows users to ask research questions and receive responses derived from real-time web search, mathematical reasoning, and PDF content parsing.
---
## 🚀 Features
- 🧠 **LangChain Agent** powered by OpenAI
- 🔍 **Web Search Tool** using SerpAPI
- 🧮 **Math Evaluator** with built-in calculator
- 📄 **PDF Reader** for extracting information from research papers
- 💻 **Streamlit UI** for easy interaction
- 📦 Modular project structure for scalability
- 🔐 `.env` support with `python-dotenv`
---
## 📁 Folder Structure
```
llm-research-agent/
├── app/
│   ├── tools/
│   │   ├── web_search.py          # Uses SerpAPI
│   │   ├── calculator.py          # Safe math eval
│   │   └── pdf_reader.py          # Reads PDFs using LangChain loaders
│   ├── agents/
│   │   └── research_agent.py      # Combines tools into a LangChain agent
│   └── chains/
│       └── reasoning_graph.py     # Placeholder for LangGraph planning
├── ui/
│   └── streamlit_app.py           # Streamlit UI
├── data/
│   └── sample_papers/             # Add PDFs here for testing
├── .env                           # API keys config
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```
---
## 🛠️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/llm-research-agent.git
cd llm-research-agent
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Add Your API Keys
Create a `.env` file in the root folder:
```env
OPENAI_API_KEY=your-openai-key
SERPAPI_API_KEY=your-serpapi-key
```
You can get keys from:
- OpenAI: https://platform.openai.com/account/api-keys
- SerpAPI: https://serpapi.com/
---
## 🚦 Run the App
```bash
streamlit run ui/streamlit_app.py
```
Use PowerShell if you're on Windows:
```bash
$env:PYTHONPATH="."; streamlit run ui/streamlit_app.py
```
---
## 🧪 Example Use Cases
- "Summarize the recent applications of LangGraph in LLM agents."
- "What is the current stock price of NVIDIA + (2^10)?”
- "Read and explain the first page of `sample_papers/ai_paper.pdf`."
---
## 🔒 Security Note
The calculator tool uses `eval()` for simplicity — **only use trusted input** in production or replace with a math parser like `sympy`.
---
## 📬 Contributions Welcome!
If you'd like to contribute tools, add LangGraph planning, or improve UI, feel free to fork and open a PR!
---
