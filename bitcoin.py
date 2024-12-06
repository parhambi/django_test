#https://api.coindesk.com/v1/bpi/currentprice.
#https://api.coincap.io/v2/assets
import requests
def get_crypto_price(asset):
    request = requests.get("https://api.coincap.io/v2/assets")
    response = request.json()
    for i in response["data"]:
        if i["id"] == asset:
            price = float(i["priceUsd"])
            break
    return f"${price:,.4f}"
