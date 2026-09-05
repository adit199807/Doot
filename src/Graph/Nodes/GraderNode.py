from Graph.State import GraphState
from Graph.Chains.GraderChain import graderChain
from Schemas import GraderDTO


from typing import Dict, Any


def graderNode(state:GraphState) -> Dict[str, Any]:
    for doc in state['documents']:
        gradedDocs = graderChain.invoke({'question': f'Question: {state['question']}', 'documents':f'Document: {doc.page_content}'})
        if not gradedDocs.documentGraded:
            return{'webSearch' : True}
        else:
            state['documents'].append(doc)
    return {'documents':state['documents'], 'webSearch':False}
