import requests
import time

FMP_API_KEY = "becda64896abed95e027f6df4b8d13c1"

IFTT_WEBHOOK_KEY = "jYf4ycDEDmCJ8a0aGPQz1no7EXG5f_QYCiwHETGUOVM"

stock_symbols = ["AAPL", "TSLA", "MSFT", "GOOGL", "NKE"]

price_change_threshold = 0.25
interval_seconds = 60

IFTT_WEBHOOK_EVENT = "stock_price_drop"

def get_stock_price(symbol):
    url = "https://financialmodelingprep.com/api/v3/quote/{syymbol}?apikey={becda64896abed95e027f6df4b8d13c1}"
    response = requests.get(url)
    data = response.json()
    return float(data[0]['price'])

def send_notification(stock_symbol, current_price, price_change):
    IFTT_WEBHOOK_EVENT = {
        "value1":stock_symbol,
        "value2":current_price,
        "value3":price_change
    }

url = "https://maker.ifttt.com/trigger/stock_price_drop/with/key/jYf4ycDEDmCJ8a0aGPQz1no7EXG5f_QYCiwHETGUOVM"
response = requests.post(url, json=IFTT_WEBHOOK_EVENT)
if response.status_code == 200:
    print("notification sent successfully")
else:
    print("notification sending failed")

while True:
   for symbol in stock_symbols:
       current_price = get_stock_price
       prev_price = current_price
       price_change = current_price - prev_price

   if price_change_threshold <= -price_change_threshold:
    send_notification(symbol, current_price, price_change)
    
    seven_day_average = get_stock_price(symbol)
   if current_price < seven_day_average:
            send_notification(symbol, current_price, seven_day_average)
            
   




