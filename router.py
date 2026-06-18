from prompts.registry import get_prompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

router_prompt = ChatPromptTemplate.from_messages([
    ('system', get_prompt('router')),
    ('human', '{query}'),                    # <- 'user_input' se 'query' kiya
])
router_chain = router_prompt | model | StrOutputParser()    # <- model_2 se model kiya

def route(query: str) -> str:
    decision = router_chain.invoke({"query": query})
    return decision.strip().upper()

if __name__ == "__main__":
    q = input("Enter your query: ")
    print(route(q))