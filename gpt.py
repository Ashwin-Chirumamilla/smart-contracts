import openai
import os
import asyncio
import websockets

# Set up OpenAI API credentials
openai.api_key = "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"

# Define function to generate response from GPT
async def process_data(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message



async def handler(websocket, path):
    async for message in websocket:
        response = await process_data(message)
        await websocket.send(response)

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()




