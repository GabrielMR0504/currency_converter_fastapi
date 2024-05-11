from environments import ALPHAVANTAGE_KEY
import requests
from fastapi import HTTPException
import traceback
import aiohttp


def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={
        from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_KEY}'

    try:
        response = requests.get(url)
    except Exception:
        raise HTTPException(status_code=400, detail=traceback.format_exc())

    data = response.json()

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(
            status_code=400, detail=f'Realtime Currency Exchange Rate not in response {data}')

    exchange_rate = float(
        data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    return price * exchange_rate


async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={
        from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_KEY}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

    except Exception:
        raise HTTPException(
            status_code=400, detail=traceback.format_exc(limit=1))

    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(
            status_code=400, detail=f'Realtime Currency Exchange Rate not in response {data}')

    exchange_rate = float(
        data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    return {to_currency: price * exchange_rate}
