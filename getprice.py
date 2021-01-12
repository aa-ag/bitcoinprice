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
     using API key, create get data, and draw/plotadd chart
    '''

    # candles = client.get_candles(
    #     'bittrex',  # exchange
    #     'XLM',      # base_trading_symbol
    #     'BTC',      # quote_trading_symbol
    #     '15m'       # interval
    # )

    re = requests.get(
        'https://dev-api.shrimpy.io/v1/exchanges/coinbasepro/candles?quoteTradingSymbol=BTC&baseTradingSymbol=XLM&interval=1H').json()

    print(re)

    '''
    [
    {
        "open": "0.0000157300000000",
        "high": "0.0000157800000000",
        "low": "0.0000155800000000",
        "close": "0.0000157100000000",
        "volume": "219444.0000000000000000",
        "quoteVolume": 3.44176145,
        "btcVolume": 3.44176145,
        "usdVolume": 27437.297915762,
        "time": "2019-05-24T23:00:00.000Z"
    }, ...
    ]
    '''

    # dates = []
    # open_data = []
    # high_data = []
    # low_data = []
    # close_data = []

    # for candle in candles:
    #     dates.append(candle['time'])
    #     open_data.append(candle['open'])
    #     high_data.append(candle['high'])
    #     low_data.append(candle['low'])
    #     close_data.append(candle['close'])

    # fig = go.Figure(data=[go.Candlestick(x=dates,
    #                                      open=open_data, high=high_data,
    #                                      low=low_data, close=close_data)])

    # fig.show()


def available_data():
    '''
     Lists all available data in API
    '''
    # SUPPORTED EXCHANGES
    supported_exchanges = client.get_supported_exchanges()

    exchanges_names = [exchange_name for exchange_name in supported_exchanges]

    # print(
    #     f"\nThere are {len(exchanges_names)} available exchanges, and they are:")

    # for i, x in enumerate(exchanges_names):
    #     print(f" {i + 1} {x['exchange']}")

    # ASSETS
    exchange_assets = client.get_exchange_assets('bittrex')

    df = pd.DataFrame(exchange_assets)

    print(f"Number of columns: {df.columns}")
    # Number of columns: Index(['id', 'name', 'symbol', 'tradingSymbol'], dtype='object')
    print(f"Number of rows: {df.index}")
    # Number of rows: RangeIndex(start=0, stop=107, step=1)

    # [!] to display entire dataframe with no truncation
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', -1)
    print(df)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    draw_chart()
    # available_data()
