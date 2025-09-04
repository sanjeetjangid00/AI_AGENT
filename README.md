# AI_Agent
# 🧠 Ask Something — AI Agent Chat App with LangChain + Gemini

A conversational AI agent powered by **LangChain**, **Google Gemini (via ChatGoogleGenerativeAI)**, and **Streamlit**. This project lets users ask natural language questions — and the agent will use **live web search** and **real-time weather data** to answer!

## 🚀 Demo

Ask things like:

> "What's the weather like in Bangalore?"  
> "3 ways to travel from Delhi to Goa"  
> "Latest news about AI regulations"

The agent:
- Understands your query
- Decides what tools to use (web search, weather API, etc.)
- Replies in natural language

---

## 🧰 Tech Stack

| Technology        | Role                                    |
|-------------------|------------------------------------------|
| `LangChain`       | Framework for LLM agents & tools         |
| `Google Gemini`   | LLM for reasoning (via `langchain_google_genai`) |
| `Streamlit`       | Web app interface                        |
| `DuckDuckGo`      | For live web search                      |
| `Open-Meteo API`  | For real-time weather info               |
| `dotenv`          | Load API keys from `.env`                |

```bash
git clone https://github.com/your-username/ai-agent-chat-app.git
cd ai-agent-chat-app
