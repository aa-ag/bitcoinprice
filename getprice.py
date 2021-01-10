###--- IMPORTS ---###
import requests
import json
import pandas as pd
import shrimpy
import plotly.graph_objects as go
import settings


###--- GLOBAL VARIABLES ---###
shrimpy_public_key = settings.SHRIMPY_PUBLIC_KEY
shrimpy_private_key = settings.SHRIMPY_PRIVATE_KEY

client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_private_key)

###--- FUNCTIONS ---###


def draw_chart():
    '''
     using API key, create get data, and draw chart
    '''
    candles = client.get_candles(
        'binance',  # exchange
        'XLM',      # base_trading_symbol
        'BTC',      # quote_trading_symbol
        '15m'       # interval
    )

    dates = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []

    for candle in candles:
        dates.append(candle['time'])
        open_data.append(candle['open'])
        high_data.append(candle['high'])
        low_data.append(candle['low'])
        close_data.append(candle['close'])

    fig = go.Figure(data=[go.Candlestick(x=dates,
                                         open=open_data, high=high_data,
                                         low=low_data, close=close_data)])

    fig.show()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    draw_chart()
