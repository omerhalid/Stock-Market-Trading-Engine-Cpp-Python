# this is the FastAPI interface for the model

# import libraries
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd
from dependecies import get_current_and_average_price, mean_reversion, lstm_predict

app = FastAPI()

# get the API key from the environment variable
# ALPHA_API_KEY = os.environ['ALPHA_API_KEY']
ALPHA_API_KEY = "L29QA85ZBJFL9KIL"

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

@app.get("/short_long_avg/{symbol}")
async def short_long_avg(symbol: str):
    return await get_current_and_average_price(symbol)

@app.get("/mean_reversion/{symbol}")
async def meanReversion(symbol: str):
    return await mean_reversion(symbol)

@app.get("/lstm/{symbol}")
async def lstm(symbol: str):
    # do we need to add the date?
    return await lstm_predict(symbol)