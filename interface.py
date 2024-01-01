# this is the FastAPI interface for the model

# import libraries
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd
from dependecies import calc_short_long_avg_price

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
async def get_current_and_average_price(symbol: str):
    ts = TimeSeries(key=ALPHA_API_KEY, output_format='pandas')
    try:
        data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    except ValueError:
        print(f"Error getting data for symbol: {symbol}")
        raise
    data.reset_index(inplace=True)
    data.rename(columns={data.columns[0]: 'index'}, inplace=True)
    data['date'] = data['index']
    data_last_50_days = data.sort_values('date', ascending=False).head(50)
    data_last_10_days = data_last_50_days.head(10)
    avg_price_last_10_days = data_last_10_days['4. close'].mean()
    avg_price_last_50_days = data_last_50_days['4. close'].mean()
    current_price = data_last_50_days['4. close'].iloc[0]
    
    with open('monitor.txt', 'a') as f:
        f.write("STRATEGY: SHORT LONG AVERAGE\n")
        f.write(f"{symbol}, {avg_price_last_10_days}, {avg_price_last_50_days}\n")
        f.write("--------------------\n")
    
    # return {"symbol": symbol, "current_price": current_price, "avg_price_last_10_days": avg_price_last_10_days, "avg_price_last_50_days": avg_price_last_50_days}
    
    return {
        "signal": "buy" if avg_price_last_10_days > avg_price_last_50_days else "sell",
        "current_price": current_price,
        "avg_price_last_10_days": avg_price_last_10_days,
        "avg_price_last_50_days": avg_price_last_50_days
    }

@app.get("/mean_reversion/{symbol}")
def mean_reversion(symbol: str):
    ts = TimeSeries(key=ALPHA_API_KEY, output_format='pandas')
    try:
        data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    except ValueError:
        print(f"Error getting data for symbol: {symbol}")
        raise
    data.reset_index(inplace=True)
    data.rename(columns={data.columns[0]: 'index'}, inplace=True)
    data['date'] = data['index']
    
    data_last_50_days = data.sort_values('date', ascending=False).head(50)
    print(data_last_50_days)
    avg_price_last_50_days = data_last_50_days['4. close'].mean()
    
    current_price = data_last_50_days['4. close'].iloc[0]
    
    
    with open('monitor.txt', 'a') as f:
        f.write("STRATEGY: MEAN REVERSION\n")
        f.write(f"{symbol}, {current_price}, {avg_price_last_50_days}\n")
        f.write("--------------------\n")
    
    return {
        "signal": "sell" if current_price > avg_price_last_50_days else "buy",
        "current_price": current_price,
        "avg_price_last_50_days": avg_price_last_50_days
    }