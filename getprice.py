###--- IMPORTS ---###
import requests


###--- FUNCTIONS ---###

def get_price():
    res = requests.get('https://api.coingecko.com/api/v3/ping')
    print(res.url)
    print(res.status_code)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    get_price()
