from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from ..Chains.GenerationChain import generationChain
from State import GraphState


def generationNode(state:GraphState):
    documnetContext = ''
    for doc in state['documents']:
        documnetContext +=  '\n\n' + doc.page_content

    result = generationChain.invoke(
        {
            'humanQuestion': 
            [
                HumanMessage(content=state['question']),
                SystemMessage(content=f"""Document context: {documnetContext}""")
            ],
        }
    )
    return {'generation':result.content}

def main():
    pass

if __name__ == '__main__':
    main()