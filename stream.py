from matplotlib.font_manager import json_dump
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

    channel_data={
        "action":"subscribe",
        "params":TICKERS
    }

    ws.send(json.dumps(channel_data))

def on_message(ws,message):
    print("recieved message")
    print(message)

def on_close(ws):
    print("Closing connection")


ws=websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message,on_close=on_close)

ws.run_forever()