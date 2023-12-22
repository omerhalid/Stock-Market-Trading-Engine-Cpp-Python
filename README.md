# Stock Market Trading Engine

## Overview
This project integrates a C++ trading engine with a FastAPI backend to create a stock market trading system. The FastAPI server fetches stock data and calculates moving averages, while the C++ engine monitors this data and executes trades based on a simple moving average crossover strategy.

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
