# import streamlit as st
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.graph import START, END, StateGraph
from dotenv import load_dotenv, find_dotenv
from typing import TypedDict, Annotated, List, Sequence
from langchain_core.output_parsers import StrOutputParser
import os

_=load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

class AgentState(TypedDict):
    messages: List[HumanMessage]

def llm_model(model="moonshotai/kimi-k2-instruct-0905"):
    return ChatGroq(model = model) | StrOutputParser()

# write node functions
def question_answer_node(state: AgentState) -> AgentState:
    """ This node takes an input and redirect it """
    llm = llm_model()
    response = llm.invoke(state["messages"])
    print(f"AI: {response}")
    return state

# def should_continue(state: AgentState) -> AgentState:
#     """ Make a decision to continue or not the Q&Q session"""
#     if state["messages"] not in ["quit", "bye"] :
#         return "continue"
#     else: 
#         return "end"

# graph
graph = StateGraph(AgentState)
graph.add_node("question_answer", question_answer_node)
graph.add_edge(START, "question_answer")
graph.add_edge("question_answer", END)

# graph.add_conditional_edges(
#     "question_answer",
#     should_continue,
#     {
#         "continue": "question_answer",
#         "end": END
#     }
# )

app = graph.compile()

question = input("User: ")
while question not in ["quit", "bye"]:
    app.invoke({"messages": [HumanMessage(content=question)]})
    question = input("User: ")

