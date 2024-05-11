from environments import ALPHAVANTAGE_KEY
import requests
from fastapi import HTTPException
import traceback


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={
        from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_KEY}'

    try:
        response = requests.get(url)
    except Exception:
        raise HTTPException(status_code=400, detail=traceback.format_exc())

    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        print(url)
        print(data)
        raise HTTPException(
            status_code=400, detail='Realtime Currency Exchange Rate not in response')

    exchange_rate = float(
        data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    return price * exchange_rate
