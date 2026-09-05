import os
from langchain_firecrawl import FirecrawlCrawl, FirecrawlMap, FirecrawlExtract
from firecrawl import Firecrawl
import markdown
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from Graphs.State import GraphState
from langchain_core.documents import Document



load_dotenv()

tavily_crawl = FirecrawlCrawl()
firecrawl  = Firecrawl(api_key=os.environ.get('FIRECRAWL_API_KEY', ''))
bs = BeautifulSoup()

def websearchNode(state: GraphState):
    results = firecrawl.search(query=state['question'], limit=3)
    docs = []
    datas = None
    if results.web:
        datas = results.web
    elif results.images:
        datas = results.images
    else:
        datas = results.news
    for data in datas:
        docs.append( 
            Document(
                page_content = data.description,
                metadata = {'title':data.title, 'url':data.url}
            )
        )
    state['documents'].extend(docs)
    return {'documents':state['documents']}


def main():
    st = GraphState(documents = [],webSearch = False,generation = '',question = '')
    st['question']='What is the LLM'
    ans = websearchNode(st)


if __name__ == "__main__":
    main()
