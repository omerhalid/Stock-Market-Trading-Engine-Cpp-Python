# this is the FastAPI interface for the model

# import libraries
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from alpha_vantage.timeseries import TimeSeries
import os
import pandas as pd
from dependecies import get_current_and_average_price, mean_reversion, lstm_predict
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import stripe
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

STRIPE_API_KEY = os.environ['STRIPE_API_KEY']

# get the API key from the environment variable
# ALPHA_API_KEY = os.environ['ALPHA_API_KEY']
ALPHA_API_KEY = ""

# !!This is a terrible idea, only used for demo purposes!!
app.state.stripe_customer_id = None

@app.get("/payment_landing_page")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "hasCustomer": app.state.stripe_customer_id is not None})

@app.get("/success")
async def success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


@app.get("/cancel")
async def cancel(request: Request):
    return templates.TemplateResponse("cancel.html", {"request": request})


@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    data = await request.json()

    if not app.state.stripe_customer_id: 
        customer = stripe.Customer.create(
            description="Demo customer",
        )
        app.state.stripe_customer_id = customer["id"]

    checkout_session = stripe.checkout.Session.create(
        customer=app.state.stripe_customer_id, # !! to be fixed
        success_url="http://localhost:8000/success?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://localhost:8000/cancel",
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": data["priceId"],
            "quantity": 1
        }],
    )
    return {"sessionId": checkout_session["id"]}


@app.post("/create-portal-session")
async def create_portal_session():
    session = stripe.billing_portal.Session.create(
        customer=app.state.stripe_customer_id,
        return_url="http://localhost:8000"
    )
    return {"url": session.url}

@app.get("/")
async def root():
    message = "Hello world!"
    return {"message": message}

@app.get("/all_stocks")
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