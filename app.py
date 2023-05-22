import streamlit as st
from langchain.llms import OpenAI
import os
import envdata
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import ConversationBufferMemory



os.environ["OPENAI_API_KEY"] = f"{envdata.openai_api}"

# st.write()
st.title("🦜️🔗 React Developer")
prompt = st.text_input("Describe your Project")

title_template = PromptTemplate(
    input_variables= ['topic'],
    template= "Give me a react project guild  on {topic}"
)

script_template = PromptTemplate(
    input_variables= ['title'],
    template= "Give me a websit name for this project: {title}"
)

memory = ConversationBufferMemory(input_key='topic', memory_key='chat_memory')

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title' , memory=memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='name', memory=memory )

sequential_chain = SequentialChain(chains=[title_chain,script_chain],input_variables=['topic'], output_variables=['title', 'name'], verbose=True)

if prompt:
    response = sequential_chain({'topic':prompt})
    st.write(response['title'])
    st.write(response['name'])

    with st.expander('Message History'):
        st.info(memory.buffer)
