import os
import sys

from flask import Flask, request
app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
  query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  loader = TextLoader("data/dump.txt") # Use this line if you only need data.txt
  #loader = DirectoryLoader("data/")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

considerations =''''
Ps: If the question is not in portuguese please translate the answer to ptbr (brazilian portuguese)
'''

@app.route("/")
def home():
    return "<p>Hello, World!!!!</p>"

@app.route("/query", methods=['POST'])
def hello_world():
    assert request.method == 'POST'
    question = request.get_json()['question']
    text = f'{question}.\n\n{considerations}'
    return index.query(text, llm=ChatOpenAI())