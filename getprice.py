###--- IMPORTS ---###
import requests
from pprint import pprint


###--- FUNCTIONS ---###

def get_price():
    # res = requests.get('https://api.coingecko.com/api/v3/ping')
    # print(res.url) # 200
    # print(res.status_code)

    res = requests.get('https://api.coingecko.com/api/v3/coins/list').json()

    cryptos = [i['name'] for i in res]

    # print(cryptos)
    print(len(cryptos))  # 6126


###--- DRIVER CODE ---###
if __name__ == "__main__":
    get_price()
