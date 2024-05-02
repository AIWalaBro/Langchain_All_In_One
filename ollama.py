from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# PromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful assistant.Please respond to this message"),
        ("user", "Question:{question}")
    ]
                                 )

# Streamlit 

st.title('Langchain-Ollama Question Answering demo')
input_text = st.text_input('ask me anything ..!')


# OpenAI LLM
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question': input_text}))
    



