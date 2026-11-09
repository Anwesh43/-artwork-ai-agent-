from agents.artwork_agent import recommendArt 
import asyncio 
import sys 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(recommendArt(prompt=prompt))