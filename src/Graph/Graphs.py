from langgraph.graph import StateGraph
from langgraph.constants import END
from Graph.State import GraphState
from Graph.Nodes.Retriver import retriverNode
from Graph.Nodes.GraderNode import graderNode
from Graph.Nodes.GenerationNode import generationNode
from Graph.Nodes.WebSearchNode import websearchNode


GENERATIONNODE = 'generation_node'
GRADERNODE= 'grader_node'
RETRIVERENODE= 'retriver_node'
WEBSEARCHNODE= 'websearch_node'


def routeDecider(state:GraphState):
    if not len(state['documents']) or  state['webSearch']:
        return WEBSEARCHNODE
    return GENERATIONNODE

flowGraph  = StateGraph(GraphState)
flowGraph.add_node(GENERATIONNODE, generationNode)
flowGraph.add_node(GRADERNODE, graderNode)
flowGraph.add_node(RETRIVERENODE, retriverNode)
flowGraph.add_node(WEBSEARCHNODE, websearchNode)

flowGraph.set_entry_point(RETRIVERENODE)
flowGraph.add_edge(RETRIVERENODE, GRADERNODE)
flowGraph.add_conditional_edges(GRADERNODE, routeDecider)
flowGraph.add_edge(WEBSEARCHNODE, GENERATIONNODE)
flowGraph.add_edge(GENERATIONNODE, END)

graph = flowGraph.compile()

def main():
    st = GraphState(
        documents=[],
        webSearch=False,
        generation='',
        question='',
    )
    st['question'] = 'What is LLM' 
    result = graph.invoke(st)
    print(result['generation'])

if __name__ == '__main__':
    main()