from typing import Annotated, TypedDict
from langchain_openai import AzureChatOpenAI

from langgraph.graph.message import add_messages

from config import load_api_key
from tools import tools

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = AzureChatOpenAI(
    api_key=load_api_key(), 
    api_version="2024-02-01", 
    azure_endpoint="https://models.inference.ai.azure.com",
    model="gpt-4o", 
)

llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    last_message = state["messages"][-1]  
    response = llm_with_tools.invoke(last_message.content)  
    return {"messages": [response]}