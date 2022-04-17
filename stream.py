import websocket,json
from config import *

socket="wss://alpaca.socket.polygon.io/stocks"

# connecting to the socket

def on_open(ws):
    print("opened")
    auth_data={
        "action":"auth",
        "params":API_KEY
    }
    ws.send(json.dumps(auth_data))

def on_message(ws,message):
    print("recieved message")
    print(message)


ws=websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)

ws.run_forever()