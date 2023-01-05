import os
import requests
import pandas as pd
from ta.trend import EMAIndicator
import websocket, json, numpy, talib

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
slowEmaValue = 9
fastEmaValue = 14
in_position = False
closes = []


def check_sell_or_buy(last_rsi, closes, df):
    print(2)
    global in_position
    slowEma = EMAIndicator(df["close"], float(slowEmaValue))
    df["Slow Ema"] = slowEma.ema_indicator()

    # LOAD FAST EMA
    FastEma = EMAIndicator(df["close"], float(fastEmaValue))
    df["Fast Ema"] = FastEma.ema_indicator()
    if (df["Fast Ema"][len(df.index) - 3] < df["Slow Ema"][len(df.index) - 3] and df["Fast Ema"][len(df.index) - 2] >
        df["Slow Ema"][len(df.index) - 2]) or (
            df["Fast Ema"][len(df.index) - 3] > df["Slow Ema"][len(df.index) - 3] and df["Fast Ema"][
        len(df.index) - 2] < df["Slow Ema"][len(df.index) - 2]):
        kesisim = True
    else:
        kesisim = False

    if kesisim and df["Fast Ema"][len(df.index) - 2] > df["Slow Ema"][len(df.index) - 2]:
        print(3)
        if in_position:
            message = "EMA Overbought! SELL!"
            print(4)
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            in_position = False
            closes.clear()

        else:
            message = "EMA It is overbought but we dont't own any"
            print(5)
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            print(5.1)
            closes.clear()

    if kesisim and df["Fast Ema"][len(df.index) - 2] < df["Slow Ema"][len(df.index) - 2]:
        print(6)
        if in_position:
            message = "EMA It is oversold but we already own it"
            print(7)
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            print(8)
            closes.clear()

        else:
            print(9)
            message = "EMA Oversold! BUY!"
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            print(10)
            in_position = True
            closes.clear()
    # -------------------------------------------------------------------------------------------------------------------------------------
    if last_rsi > RSI_OVERBOUGHT:
        print(3)
        if in_position:
            message = "RSI Overbought! SELL!"
            print(4)
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            in_position = False
            closes.clear()

        else:
            message = "RSI It is overbought but we dont't own any"
            print(5)
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            print(5.1)
            closes.clear()

    if last_rsi < RSI_OVERSOLD:
        print(6)
        if in_position:
            message = "RSI It is oversold but we already own it"
            print(7)
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            print(8)
            closes.clear()

        else:
            print(9)
            message = "RSI Oversold! BUY!"
            requests.post(url="https://api.telegram.org/bot5973409961:AAG6YaScFmBseczmNJl9qGcYxNywzP6lZ5Y/sendMessage",
                          data={"chat_id": "-1001884488798", "text": message}).json()
            print(10)
            in_position = True
            closes.clear()


def on_open(ws):
    print("opened")


def on_close(ws):
    print("closed")
    ws.close()


def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']

    if is_candle_closed:

        print("candle closed at: ", close)
        closes.append(float(close))
        df = pd.DataFrame(closes, columns=["close"])
        print(df)

        a = []
        if not os.path.isfile('information.json'):
            a.append(candle)
            with open('information.json', mode='w') as f:
                f.write(json.dumps(a, indent=2))
        else:
            with open('information.json') as feedsjson:
                feeds = json.load(feedsjson)

            feeds.append(candle)
            with open('information.json', mode='w') as f:
                f.write(json.dumps(feeds, indent=2))

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all RSIs calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("The current rsi value is", last_rsi)

            check_sell_or_buy(last_rsi, closes, df)


def start():
    global ws
    ws.run_forever()


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
