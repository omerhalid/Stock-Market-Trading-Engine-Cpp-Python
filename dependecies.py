# Strategy for the trading system

from fastapi import FastAPI
from pydantic import BaseModel
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd

ALPHA_API_KEY = "" # Put your API key here

def calc_short_long_avg_price(symbol: str):
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
    
    return avg_price_last_10_days, avg_price_last_50_days, current_price