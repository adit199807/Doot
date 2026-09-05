from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from Schemas import GraderDTO
from dotenv import load_dotenv
import os

load_dotenv()
graderPrompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a smart analyst, please grade 
    the documnets below, if they aling with the user question or not."""),
    MessagesPlaceholder("question"),
    MessagesPlaceholder("document")
]) 
llm = ChatOpenAI(model=os.environ.get('MINI_MODEL', ''))

graderChain = graderPrompt | llm.with_structured_output(GraderDTO)

def main():
    print("Hello from doot!")



if __name__ == "__main__":
    main()
