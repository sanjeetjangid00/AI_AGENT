import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
import requests


load_dotenv()

st.title("ASK SOMETHING to AI AGENT")

@tool
def get_wether_data(city : str)->str:
    """
  This function fetches the current weather data for a given city
  """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()
    if "results" in data and data["results"]:
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
    else:
        lat = None, 
        lon =None
    
    if lat is None or lon is None:
        return f"City '{city}' not found."

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    temp = weather_data["current_weather"]["temperature"]
    wind = weather_data["current_weather"]["windspeed"]
    code = weather_data["current_weather"]["weathercode"]

    return weather_data

search_tool = DuckDuckGoSearchRun()

prompt = hub.pull("hwchase17/react")

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')

agent = create_react_agent(
    llm = llm,
    prompt = prompt,
    tools = [search_tool, get_wether_data]
)

agent_executor = AgentExecutor(
    agent = agent,
    tools = [search_tool, get_wether_data],
    verbose = True
)

query = st.chat_input("Enter Your Query :")
if query:
    response = agent_executor.invoke({"input": query})
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        st.write(response['output'])