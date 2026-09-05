from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

MODEL  = os.environ.get('MINI_MODEL','')
generationPrompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a smart writer. Please answer the 
    users question form the documnets provided below"""),
    MessagesPlaceholder('humanQuestion'),
])
llm = ChatOpenAI(model=MODEL)
generationChain = generationPrompt | llm

def main():
    pass

if __name__ == '__main__':
    main()