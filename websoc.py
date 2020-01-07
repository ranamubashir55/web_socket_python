import asyncio
import websockets

# async def handle_message(message):
#     print(message)

# async def consumer_handler(websocket, path):
#     while True:
#         message = await websocket.recv()
#         await handle_message(message)

# start_server = websockets.serve(consumer_handler, 'localhost', 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()


import time, json
import asyncio
import datetime
import random
import websockets

def test():
    c=0
    while True:
        time.sleep(3)
        print("im genrator")
        c=c+1
        if c==2:
            break
        yield {"data":c}
    

async def time2(websocket, path):
    while True:
        print("socket opened")
        message = await websocket.recv()
        print(message)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        for x in test():
            await websocket.send(json.dumps(x))
        print("end genrator")
        await asyncio.sleep(random.random() * 3)

print("start websocket")
start_server = websockets.serve(time2, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
