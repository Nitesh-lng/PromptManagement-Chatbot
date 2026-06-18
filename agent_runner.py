from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts.registry import get_prompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model='openai/gpt-oss-120b')

def run_agent(agent_name:str, user_query:str) -> str:
    agent_prompt=ChatPromptTemplate.from_messages([
        ('system', get_prompt(agent_name)),
        ('human', user_query)
    ])
    
    agent_chain = agent_prompt | model | StrOutputParser()
    
    return agent_chain.invoke({'query': user_query})