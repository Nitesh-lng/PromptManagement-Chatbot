from prompts.agents import COMPLAINTS, TRACKING, GENERAL, FINANCE, ROUTER

PROMPT_REGISTRY={
    'router': ROUTER,
    'finance':FINANCE,
    'general':GENERAL,
    'tracking':TRACKING,
    'complaints':COMPLAINTS
}

def _get(agent_name:str):
    '''Fetch the prompt configuration for a given agent name.'''
    name = agent_name.lower() 
    if agent_name not in PROMPT_REGISTRY:
        raise ValueError(f"Agent '{agent_name}' not found in the registry.")
    return PROMPT_REGISTRY[agent_name]

def get_prompt(agent_name:str):
    '''Get the prompt text for a specific agent.'''
    agent_config = _get(agent_name)
    return agent_config['text']