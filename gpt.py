import os
import envdata
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain import VectorDBQA
from langchain.chains import RetrievalQA
from langchain import ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake, Chroma
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter 
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)

from langchain.agents.agent_toolkits import (
    create_vectorstore_router_agent,
    VectorStoreRouterToolkit,
)




os.environ["OPENAI_API_KEY"] =f"{envdata.openai_api}"
os.environ['ACTIVELOOP_TOKEN'] = f"{envdata.activeloop}"
embeddings = OpenAIEmbeddings(disallowed_special=())
llm = OpenAI(temperature=0)

html_dir =r'C:\pr0\bidzen'
root_dir = './the-algorithm'
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


biden_html_store = Chroma.from_documents(texts, embeddings, collection_name="biden-html")

vectorstore_info = VectorStoreInfo(
    name="html_template",
    description="HTML template for NFT Marketplace",
    vectorstore=biden_html_store
)

toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)


agent_executor.run("give me the code belonging to the div with class admin_active")