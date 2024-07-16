#Basic Introduction to setup Ollama into the Process
from langchain.community.llms import Ollama

llm = Ollama(model="llama3")
response = llm.invoke("Tell me Why is sky blue?")
print(response)
