import ssl
from json import loads

import websocket


def open(ws):
    print('Conectado ao servidor BitStamp')

    subscribe = '''
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    '''

    ws.send(subscribe)


def close(ws):
    print('Desconectado do servidor BitStamp')


def error(ws, error):
    print('Something go wrong')
    print(error)


def message(ws, message):
    response = loads(message)
    if response["data"]["type"] == 0:
        type = 'buy'
    else:
        type = 'sell'
    print(f'ID:{response["data"]["id"]} PRICE: {response["data"]["price"]} TYPE: {type}')


if __name__ == '__main__':
    ws = websocket.WebSocketApp('wss://ws.bitstamp.net',
                                on_open=open,
                                on_close=close,
                                on_error=error,
                                on_message=message)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})