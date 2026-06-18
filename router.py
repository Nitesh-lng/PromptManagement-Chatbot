from prompts.registry import get_prompt, _get
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(
    model='openai/gpt-oss-120b'
)

router_prompt=ChatPromptTemplate.from_messages([
    ('system', get_prompt('router')),
    ('human', '{user_input}')
])
parser=StrOutputParser()

user_query=input("Enter your query: ")

router_chain= router_prompt | model | parser

res=router_chain.invoke(user_input=user_query)

print(res)