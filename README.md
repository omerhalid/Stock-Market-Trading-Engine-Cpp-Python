# Stock Market Trading Engine

## Overview
This project integrates a C++ trading engine with a FastAPI backend to create a stock market trading system. The FastAPI server fetches stock data and calculates moving averages, while the C++ engine monitors this data and executes trades based on a simple moving average crossover strategy.

The system offers two subscription options: Basic and Premium. The Basic subscription provides access to a limited set of features, including basic trading strategies and data analysis tools. The Premium subscription unlocks additional features, such as advanced trading strategies and priority customer support.

Payments for both subscription options are processed securely via Stripe, a leading online payment processing platform. Stripe's robust API allows us to offer a seamless checkout experience to our users while ensuring that their payment information is handled with the highest level of security.

## Trading System Strategy

The trading system uses three strategies: Short Long Average, Mean Reversion, and LSTM Prediction. 

1. **Short Long Average**: This strategy calculates the average closing price for the last 10 and 50 days. If the average price for the last 10 days is higher than the average price for the last 50 days, it signals to buy. Otherwise, it signals to sell.

2. **Mean Reversion**: This strategy calculates the average closing price for the last 50 days. If the current price is higher than the average price for the last 50 days, it signals to sell, assuming that the price will revert to the mean. Otherwise, it signals to buy.

3. **LSTM Prediction**: This strategy uses a Long Short-Term Memory (LSTM) model to predict the next day's closing price based on the last 20 years of data. The LSTM model is a type of Recurrent Neural Network (RNN) that is capable of learning long-term dependencies, which makes it suitable for time-series data like stock prices.

The system fetches the stock data from the Alpha Vantage API, calculates the signals based on the strategies, and writes the signals to a file named 'monitor.txt'. 

A C++ trading engine then reads the signals from the 'monitor.txt' file and executes the corresponding orders. The orders are written to a file named 'orders.txt'. 

Please note that stock trading involves risk, and these strategies do not guarantee profits. Always consider other factors and do your own research.

## LSTM Stock Prediction

The system includes a Long Short-Term Memory (LSTM) model for predicting future stock prices. LSTM is a type of Recurrent Neural Network (RNN) that is capable of learning long-term dependencies, which makes it suitable for time-series data like stock prices.

The LSTM model is trained on 20 years of historical stock data fetched from the Alpha Vantage API. The model takes the closing prices for the last 3 days as input and predicts the closing price for the next day.

Here's a high-level overview of how the LSTM stock prediction function works:

1. Fetch 20 years of historical stock data from the Alpha Vantage API.
2. Preprocess the data to create a time-series dataset where each instance consists of the closing prices for the last 3 days and the target is the closing price for the next day.
3. Train an LSTM model on this dataset.
4. To predict the closing price for the next day, take the closing prices for the last 3 days, feed them into the LSTM model, and output the prediction.

Please note that stock price predictions are inherently uncertain and should not be used as the sole basis for trading decisions. Always consider other factors and do your own research.

## Components
- `TradingEngine`: A C++ application that monitors for stock data and executes trading decisions.
- `FastAPI Server`: Python-based server fetching stock data and writing it to a file for the C++ engine.

## Setup and Installation
### Prerequisites
- Python 3.x
- C++ compiler (e.g., g++, clang)
- FastAPI
- Alpha Vantage API Key

### Running the FastAPI Server
1. Install required Python libraries:
   ```bash
   pip install fastapi uvicorn alpha_vantage pandas
   ```
2. Run the server:
  ```bash
  uvicorn main:app --reload
  ```
### Running the C++ Trading Engine
Compile the C++ code:
```bash
g++ -o trading_engine TradingEngine.cpp
```
Run the compiled program:
```bash
./trading_engine
```
### Usage
Access the FastAPI server at http://localhost:8000.
Choose a stock symbol to fetch data.
The FastAPI server will write the data to monitor.txt.
The C++ engine reads this data, processes it, and decides on trading actions.

### Contributing
Feel free to fork the project and submit pull requests.

### License
MIT License
