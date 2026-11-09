from pydantic_ai import Agent 
from dotenv import load_dotenv 
from tools.artwork_tools import getTools 
from prompts.artwork_prompt import SYSTEM_PROMPT

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    system_prompt = SYSTEM_PROMPT,
    tools = getTools()
)

async def recommendArt(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')