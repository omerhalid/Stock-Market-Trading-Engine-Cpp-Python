# this is the FastAPI interface for the model

# import libraries
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd

app = FastAPI()

# get the API key from the environment variable
ALPHA_API_KEY = os.environ['ALPHA_API_KEY']

@app.get("/")
async def show_stock_names():
    stocks = {
        '1': 'Apple Inc. - AAPL',
        '2': 'Microsoft Corporation - MSFT',
        '3': 'Amazon.com, Inc. - AMZN',
        '4': 'Facebook, Inc. - FB',
        '5': 'Alphabet Inc. (Google) - GOOGL',
        '6': 'Tesla, Inc. - TSLA',
        '7': 'NVIDIA Corporation - NVDA',
        '8': 'PayPal Holdings, Inc. - PYPL',
        '9': 'Netflix, Inc. - NFLX',
        '10': 'Adobe Inc. - ADBE',
        '11': 'Intel Corporation - INTC',
        '12': 'Cisco Systems, Inc. - CSCO',
        '13': 'Comcast Corporation - CMCSA',
        '14': 'PepsiCo, Inc. - PEP',
        '15': 'Adobe Inc. - ADBE',
        '16': 'Broadcom Inc. - AVGO',
        '17': 'Texas Instruments Incorporated - TXN',
        '18': 'QUALCOMM Incorporated - QCOM',
        '19': 'Costco Wholesale Corporation - COST',
        '20': 'Starbucks Corporation - SBUX',
        '21': 'Amgen Inc. - AMGN',
        '22': 'Charter Communications, Inc. - CHTR',
        '23': 'Gilead Sciences, Inc. - GILD',
        '24': 'Mondelez International, Inc. - MDLZ',
        '25': 'Automatic Data Processing, Inc. - ADP'
    }
    return stocks

@app.get("/{symbol}")
async def get_current_and_average_price(symbol: str):
    ts = TimeSeries(key=ALPHA_API_KEY, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    data['date'] = data.index
    data_last_50_days = data.sort_values('date', ascending=False).head(50)
    data_last_10_days = data_last_50_days.head(10)
    avg_price_last_10_days = data_last_10_days['4. close'].mean()
    avg_price_last_50_days = data_last_50_days['4. close'].mean()
    current_price = data_last_50_days['4. close'].iloc[0]
    
    with open('monitor.txt', 'a') as f:
        f.write(f"{symbol}, {avg_price_last_10_days}, {avg_price_last_50_days}\n")
    
    return {"symbol": symbol, "current_price": current_price, "avg_price_last_10_days": avg_price_last_10_days, "avg_price_last_50_days": avg_price_last_50_days}