import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith Tracking

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}"),
    ]
)

def generate_response(question, api_key, llm, temprature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm)
    output_parser = StrOutputParser()
    chain=prompt|llm|output_parser
    answer = chain.invoke({'question': question })
    return answer

## Title of the app
st.title("Q&A Chatbot with OpenAI")

## Sidebar
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your open AI API Key: ",type="password")

## Dropdown to select models
llm = st.sidebar.selectbox("Select an OpenAI Model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)

## Define main interface
st.write("Go ahead and ask your question")
user_input = st.text_input("You:")

if user_input:
    respone=generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(respone)
else:
    st.write("Please enter your question in the input box")
