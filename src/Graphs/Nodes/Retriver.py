from Graphs.State import GraphState
from Ingestion import retriever
from typing import Dict, Any
from dotenv import load_dotenv
import os

load_dotenv()

def retriverNode(state:GraphState) -> Dict[str, Any]:
    documents = retriever.invoke(state['question'])

    # both below return are valid. You may add question or not would not matter as
    # graph return alwyas uses a reducer fucntion, that will update the
    # attirbute in the exisiting one
    # return {'documents':documents}
    return {'documents':documents, 'question': state['question']}


def main():
    st = GraphState(documents = [],webSearch = False,generation = '',question = '')
    st['documents']=[]
    ans = retriverNode(st)

if __name__ == "__main__":
    main()
