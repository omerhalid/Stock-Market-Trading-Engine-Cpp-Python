# Strategy for the trading system

from fastapi import FastAPI
from pydantic import BaseModel
from alpha_vantage.timeseries import TimeSeries
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

ALPHA_API_KEY = "" # Put your API key here

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
    
async def mean_reversion(symbol: str):
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

async def lstm_predict(symbol: str):
    """
    Predict the price of a stock using LSTM with using 20 years of data
    """
    # we need the date and the closing price
    ts = TimeSeries(key=ALPHA_API_KEY, output_format='pandas')
    try:
        data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    except ValueError:
        print(f"Error getting data for symbol: {symbol}")
        raise
    data.reset_index(inplace=True)
    data.rename(columns={data.columns[0]: 'index'}, inplace=True)
    data['date'] = data['index']
    data['date'] = pd.to_datetime(data['date'])
    current_closing = float(data['4. close'].iloc[0])
    data_last_20_years = data.sort_values('date', ascending=False).head(7305)
    year = data['date'].iloc[0].year
    month = data['date'].iloc[0].month
    day = data['date'].iloc[0].day
    
    # Preprocess data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data_last_20_years['4. close'].values.reshape(-1,1))

    # Create time series data
    X_train = []
    y_train = []
    for i in range(3, len(scaled_data)):
        X_train.append(scaled_data[i-3:i, 0])
        y_train.append(scaled_data[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    # Build LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))

    # Compile and fit the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=25, batch_size=32)
    
    # Select the last 3 days of data
    last_3_days = scaled_data[-3:]

    # Reshape it to match the input shape of the model
    X_test = np.array([last_3_days])
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # Predict future prices
    # For actual prediction, you need to prepare the input data in the same way as training data
    # For example, you can use the last 3 days' data to predict the next day's price
    predicted_stock_price = model.predict(X_test)
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price)
    
    with open('monitor.txt', 'a') as f:
        f.write("STRATEGY: LSTM PREDICTION\n")
        f.write(f"{symbol}, {current_closing}, {predicted_stock_price}\n")
        f.write("--------------------\n")

    # Return the predicted price (this is just a placeholder for now)
    return f"Tomorrow's predicted price for {symbol} is: {predicted_stock_price[0][0]} and current price is {data['4. close'].iloc[0]}"
