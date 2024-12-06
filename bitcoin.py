#https://api.coindesk.com/v1/bpi/currentprice.
import requests
def get_bitcoin_price():
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = request.json()
    bitcoin_price = response["bpi"]["USD"]["rate_float"]
    return bitcoin_price
if __name__ == "__main__":
    get_bitcoin_price