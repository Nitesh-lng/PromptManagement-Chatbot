from router import route
from agent_runner import run_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import MessagesPlaceholder

chat_history=[]
    
def main():
    while True:
        user_input=input("Enter your query (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break
        
        agent=route(user_input)
        print(f"Routed to agent: {agent}")
        
        result=run_agent(agent, user_input,chat_history)
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=result))
        
        print(f"Agent Response:\n{result}\n")
        
if __name__ == "__main__":  
    main()