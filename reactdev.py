import streamlit as st
import os
import envdata
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)
from typing import Dict, List, Optional, Any
from langchain.chains import RetrievalQA
from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.llms import BaseLLM
from langchain.chains.base import Chain
from langchain.experimental import BabyAGI
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor, initialize_agent,AgentType


os.environ["OPENAI_API_KEY"] = f"{envdata.openai_api}"
os.environ['ACTIVELOOP_TOKEN'] = f"{envdata.activeloop}"
embeddings = OpenAIEmbeddings(disallowed_special=())
# embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
llm = OpenAI(temperature=0)

html_dir =r'C:\pr0\bidzen'
root_dir = './the-algorithm'
persist_directory = 'db'

docs = []
for dirpath, dirnames, filenames in os.walk(html_dir):
    for file in filenames:
        try: 
            loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
            docs.extend(loader.load_and_split())
        except Exception as e: 
            pass

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)


biden_html_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings, collection_name="biden-html", )

# vectorstore_info = VectorStoreInfo(
#     name="html_template",
#     description="HTML template for NFT Marketplace",
#     vectorstore=biden_html_store
# )

# toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# agent_store_retriver = create_vectorstore_agent(
#     llm=llm,
#     toolkit=toolkit,
#     verbose=True
# )


# st.title('React GPT')
# prompt = st.text_area("input your prompt here")


# if st.button('submit'):
#     if prompt:
#         response = agent_executor.run(prompt)
#         st.write(response)

#     with st.expander("Document Similarity Search"):
#         search = biden_html_store.similarity_search_with_score(prompt)

#         st.write(search[0][0].page_content)

# agent_store_retriver = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=biden_html_store.as_retriever())

# OBJECTIVE = "convert the div with classes admin_active active on the connect-wallet.html"
# # html_snippet = biden_html_store.similarity_search_with_score(OBJECTIVE)
# # css_snippet = biden_html_store.similarity_search_with_score(OBJECTIVE)
# # js_snippet = biden_html_store.similarity_search_with_score(OBJECTIVE)

# code_snippet_prompt = PromptTemplate.from_template(
#     "As a React/Next.js expert, convert the provided HTML/CSS/JS code snippet into a functional React/Next.js component. Use the search tool to find the necessary code. Task: {objective}"
# )

# code_snippet_chain = LLMChain(llm=OpenAI(temperature=0), prompt=code_snippet_prompt)
# tools = [
#     Tool(
#         name="Search",
#         func=agent_store_retriver.run,
#         description="useful for getting the HTML/CSS/JS code snippet to be converted to a react/next.js components. Input should be the page and classes belonging to the code snippet requesting for",
#     ),
#     Tool(
#         name="Convert",
#         func=code_snippet_chain.run,
#         description="useful for converting HTML/CSS/JS snippets into functional React/Next.js components. Input should be HTML/CSS/JS snippet from a webpage. Output: A React/Next.js component mirroring the original snippet's design, functionality, and style, with necessary CSS and converted JS functionality. The tool should also identify any additional Node.js packages required. The goal is to preserve the original's attributes while leveraging React/Next.js's modular structure.",
#     ),
# ]


# prefix = """As an AI, transform the obtained code snippet into a React/Next.js component, considering the styling and behavior of the snippet and previous context. Task: {objective}."""
# suffix = """Begin!
# {agent_scratchpad}"""
# prompt = ZeroShotAgent.create_prompt(
#     tools,
#     prefix=prefix,
#     suffix=suffix,
#     input_variables=["objective","agent_scratchpad"],
# )
# llm = OpenAI(temperature=0)
# llm_chain = LLMChain(llm=llm, prompt=prompt)
# tool_names = [tool.name for tool in tools]
# agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)
# agent_executor = AgentExecutor.from_agent_and_tools(
#     agent=agent, tools=tools, verbose=True, max_iterations=2
# )

# Logging of LLMChains
# verbose = False
# If None, will keep on going forever
# max_iterations: Optional[int] = 3
# baby_agi = BabyAGI.from_llm(
#     llm=llm, vectorstore=biden_html_store, task_execution_chain=agent_executor, verbose=verbose, max_iterations=max_iterations
# )
# baby_agi({"objective": OBJECTIVE, "task":''})


# agent_executor.run({"objective": OBJECTIVE})
retriever = biden_html_store.as_retriever(search_type="mmr")

st.title('React GPT')
prompt = st.text_area("input your prompt here")
prompt_mmr = st.text_area("input your prompt here", key='mmr')


if st.button('submit'):
    if prompt:
        search = biden_html_store.similarity_search_with_score(prompt)
        st.write(search[0][0].page_content)



    if prompt_mmr:
        search_mmr = retriever.get_relevant_documents(prompt_mmr)[0]
        st.write(search_mmr[0])

        

       

