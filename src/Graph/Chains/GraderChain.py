from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from pydantic import BaseModel, Field

import os

load_dotenv()

class GraderDTO(BaseModel):
    documentGraded:bool =Field(description='assign boolean value '
    'if document is relevant to user question')

graderPrompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a smart analyst, please grade 
    the documnets below, if they aling with the user question or not."""),
    MessagesPlaceholder("question"),
    MessagesPlaceholder("document")
]) 
llm = ChatOpenAI(model=os.environ.get('MINI_MODEL', ''))
llmgrader = llm.with_structured_output(schema=GraderDTO)

graderChain = graderPrompt | llmgrader

def main():
    print("Hello from doot!")



if __name__ == "__main__":
    main()
